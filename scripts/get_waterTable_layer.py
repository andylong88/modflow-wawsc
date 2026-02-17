"""
Find, for each vertical column, the highest model layer (closest to land surface)
in which the simulated head is above the cell bottom.

Result:
    A 2D array (rows x cols) of layer numbers (1 = uppermost layer).
    Columns with no valid head or all no-flow cells get NaN.

Requirements:
    - Run import_model.py once so model.pkl exists.
    - Adjust paths and filenames (model_ws, headfile) as needed.
"""

import os
import pickle
import numpy as np
import flopy

# -------------------------------------------------------------------
# 1. Load the imported model
# -------------------------------------------------------------------

with open("../imported_models/SES_example/model.pkl", "rb") as f:
    ml = pickle.load(f)

# Get DIS package to access cell bottoms, ibound, etc.
dis = ml.dis
nlay, nrow, ncol = dis.nlay, dis.nrow, dis.ncol

# Cell bottom elevations: shape (nlay, nrow, ncol)
# For DIS, botm typically has shape (nlay, nrow, ncol)
botm = dis.botm.array

# Cell top for layer 1 (optional; not strictly needed for the criterion)
top = dis.top.array  # shape (nrow, ncol)

# IBOUND or idomain-like mask for active/no-flow cells (if present)
# Prefer BAS6 (ibound); if not present, fall back to idomain if available.
ibound = None
if hasattr(ml, "bas6"):
    ibound = ml.bas6.ibound.array  # shape (nlay, nrow, ncol)
elif hasattr(dis, "idomain"):
    ibound = dis.idomain.array
else:
    # If nothing is available, treat all cells as potentially active
    ibound = np.ones((nlay, nrow, ncol), dtype=int)

# -------------------------------------------------------------------
# 2. Load heads from the MODFLOW binary head file
# -------------------------------------------------------------------

# Adjust these to match your existing structure (mirrors plot_headsV3.py)
hds_path = os.path.join("../imported_models/SES_example/output/output.SES_ss", "SES_ss.hds")
hds = flopy.utils.HeadFile(hds_path)

times = hds.get_times()
print("Available times:", times)

# Use last time step (or change totim as desired)
head = hds.get_data(totim=times[-1])  # shape (nlay, nrow, ncol)
print("Head array shape:", head.shape)

# -------------------------------------------------------------------
# 3. Compute highest layer with head > cell bottom in each column
# -------------------------------------------------------------------

# Initialize output as NaN (float) so we can store NaN and integer layer numbers.
# This is a 2D array (nrow, ncol) of layer indices (1-based) or NaN.
col_layer = np.full((nrow, ncol), np.nan, dtype=float)

for irow in range(nrow):
    for icol in range(ncol):
        # Skip columns where all cells are no-flow or no head
        # We'll check within layers, but we need a flag to see if any valid cell exists.
        any_valid = False

        # Loop from top layer (0) downward to bottom (nlay-1)
        for ilay in range(nlay):
            # Skip if no-flow / inactive cell
            if ibound[ilay, irow, icol] <= 0:
                continue

            h = head[ilay, irow, icol]
            b = botm[ilay, irow, icol]

            # Skip if head is NaN
            if np.isnan(h):
                continue

            any_valid = True

            # Check criterion: head above cell bottom
            if h > b:
                # Store 1-based layer index and break (highest layer that meets criterion)
                col_layer[irow, icol] = ilay + 1
                break

        # If no valid cell in the column or no cell meets criterion, col_layer remains NaN
        if not any_valid:
            col_layer[irow, icol] = np.nan

# -------------------------------------------------------------------
# 4. Save result as human-readable text
# -------------------------------------------------------------------

out_dir = "../script_output"
os.makedirs(out_dir, exist_ok=True)

out_txt = os.path.join(out_dir, "highest_saturated_layer.txt")

header_lines = [
    f"2D array of highest model layer (1 = uppermost) where head > cell bottom.",
    f"Shape: rows = {nrow}, cols = {ncol}",
    "Cells with no valid head or all no-flow cells are NaN.",
    "Values are layer numbers (1-based)."
]
header = "\n".join(header_lines)

np.savetxt(
    out_txt,
    col_layer,
    fmt="%.1f",   # will print integers as x.0 and NaN as nan
    delimiter=" ",
    header=header,
    comments="# "
)

print(f"Saved highest-layer array to: {out_txt}")

# -------------------------------------------------------------------
# 5. Create 2D head array corresponding to highest saturated layer
# -------------------------------------------------------------------

# col_layer is 1-based; convert to 0-based indices for array lookup
layer_index_2d = col_layer.copy()

# Prepare 2D head array
head2d = np.full((nrow, ncol), np.nan, dtype=float)

for irow in range(nrow):
    for icol in range(ncol):
        lyr = layer_index_2d[irow, icol]
        if np.isnan(lyr):
            # No valid saturated layer in this column
            continue
        ilay = int(lyr) - 1  # 0-based
        h = head[ilay, irow, icol]
        if np.isnan(h):
            continue
        head2d[irow, icol] = h

# Save the head2d array as human-readable text
out_head_txt = os.path.join(out_dir, "heads_highest_saturated_layer.txt")

np.savetxt(
    out_head_txt,
    head2d,
    fmt="%.3f",
    delimiter=" ",
    header=(
        "Head array for highest saturated layer in each column\n"
        f"(rows = {head2d.shape[0]}, cols = {head2d.shape[1]})\n"
        "Values are in model units (e.g., meters). NaN = no saturated cell."
    ),
    comments="# "
)

print(f"Saved head array for highest saturated layers to: {out_head_txt}")

# -------------------------------------------------------------------
# 6. Contour the 2D head array and save PNG
# -------------------------------------------------------------------

import matplotlib.pyplot as plt

# Contour parameters (similar to plot_headsV3.py)
interval = 100      # contour interval
min_threshold = 0   # minimum allowed head for plots
max_threshold = 1800  # maximum allowed head for plots

# Compute plotting range, ignoring NaNs
vmin = np.nanmin(head2d)
vmax = np.nanmax(head2d)
print("Highest saturated heads range:", vmin, vmax)

vmax = min(vmax, max_threshold)
vmin = max(vmin, min_threshold)
print("New head range with thresholds:", vmin, vmax)

if np.isclose(vmin, vmax):
    raise ValueError("Highest saturated head field has uniform value; no contours can be drawn.")

# Set up map view and plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")

# For PlotMapView, choose any representative layer index (e.g., 0),
# because we are providing our own 2D array to plot_array/contour_array.
mapview = flopy.plot.PlotMapView(model=ml, layer=0)

# Filled head colors
cf = mapview.plot_array(head2d, alpha=0.9, cmap="viridis")

# Enforce same limits as contours
cf.set_clim(vmin, vmax)

# Establish the contour levels
start = np.floor(vmin / interval) * interval
end = np.ceil(vmax / interval) * interval
levels = np.arange(start, end + interval, interval)

contours = mapview.contour_array(
    head2d,
    levels=levels,
    colors="white",
    linewidths=1.0
)

plt.colorbar(cf, ax=ax, label="Head (m)")
plt.clabel(contours, inline=1, fontsize=8, colors="white")

ax.set_title("Head contours, highest saturated layer per column")

plt.tight_layout()
#fig.savefig("heads_highest_saturated_layer.png", dpi=300)
fig.savefig("../script_output/heads_highest_saturated_layer.png", dpi=300)

plt.show()