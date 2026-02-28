import os
import pickle
import numpy as np
import flopy
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

# ============================================================
# USER INPUTS
# ============================================================

pkl_file = r"../imported_models/SES_example/model.pkl"
head_file = r"../imported_models/SES_example/output/output.SES_ss/SES_ss.hds"

target_layer_num = 6  # layer number (1-based)
# Plot cross-section along row or column
x_sect = "row" # row or col
plot_row = 170 # plot along row number
plot_col = 223 # plot along column number
# Color mode for the cross-section:
#   "layer" -> color by layer index
#   "hk"    -> color by horizontal hydraulic conductivity
color_mode = "layer"
zmin_plot = -1800.0
zmax_plot = 1400.0
show_grid = True  # draw cell boundaries on cross-section?
col_max = 432 # zero based
row_max = 415 # zero based

out_png = "../script_output/cross_section.png"

# Cross-section end points in (row, col), 0-based indices
if x_sect == "row":
    rc_start = (plot_row, 0)
    rc_end   = (plot_row, col_max)
elif x_sect == "col":
    rc_start = (row_max, plot_col)
    rc_end = (0, plot_col)

# ============================================================
# LOAD MODEL, HEADS, AND ACTIVE CELLS
# ============================================================

with open(pkl_file, "rb") as f:
    m = pickle.load(f)

if isinstance(m, flopy.modflow.mf.Modflow):
    ml = m
else:
    raise TypeError("Pickle does not contain a flopy Modflow model.")

dis = ml.dis
nlay, nrow, ncol = dis.nlay, dis.nrow, dis.ncol

if not os.path.isfile(head_file):
    raise FileNotFoundError(f"Head file not found: {head_file}")

hds = flopy.utils.HeadFile(head_file)
head = hds.get_data()  # last time step; shape (nlay, nrow, ncol)

k_target = target_layer_num - 1
if not (0 <= k_target < nlay):
    raise ValueError(f"target_layer_num={target_layer_num} outside 1–{nlay}")

# Active model cells: IBOUND != 0 anywhere in the column
if getattr(ml, "bas6", None) is not None and ml.bas6.ibound is not None:
    ibound = ml.bas6.ibound.array  # shape (nlay, nrow, ncol)
    active_3d = ibound != 0
else:
    # Fallback: treat any cell with finite head as active
    active_3d = np.isfinite(head)

active_2d = np.any(active_3d, axis=0)  # shape (nrow, ncol)

def active_outline_polygon(active_2d, modelgrid):
    """
    Build a polygon that traces the outer boundary of active cells.
    Returns a matplotlib PathPatch.
    """
    nrow, ncol = active_2d.shape
    verts = []
    codes = []

    xverts = modelgrid.xvertices
    yverts = modelgrid.yvertices

    # March around grid edges, adding edges where active cell borders an inactive cell
    # Top edges
    for r in range(nrow):
        for c in range(ncol):
            if active_2d[r, c] and (r == 0 or not active_2d[r - 1, c]):
                x0, x1 = xverts[r, c], xverts[r, c + 1]
                y0 = yverts[r, c]
                if not verts:
                    verts.append((x0, y0))
                    codes.append(Path.MOVETO)
                verts.append((x1, y0))
                codes.append(Path.LINETO)

    # Right edges
    for r in range(nrow):
        for c in range(ncol - 1, -1, -1):
            if active_2d[r, c] and (c == ncol - 1 or not active_2d[r, c + 1]):
                x1 = xverts[r, c + 1]
                y0, y1 = yverts[r, c], yverts[r + 1, c]
                if not verts:
                    verts.append((x1, y0))
                    codes.append(Path.MOVETO)
                verts.append((x1, y1))
                codes.append(Path.LINETO)

    # Bottom edges
    for r in range(nrow - 1, -1, -1):
        for c in range(ncol - 1, -1, -1):
            if active_2d[r, c] and (r == nrow - 1 or not active_2d[r + 1, c]):
                x0, x1 = xverts[r, c + 1], xverts[r, c]
                y1 = yverts[r + 1, c]
                if not verts:
                    verts.append((x0, y1))
                    codes.append(Path.MOVETO)
                verts.append((x1, y1))
                codes.append(Path.LINETO)

    # Left edges
    for r in range(nrow - 1, -1, -1):
        for c in range(ncol):
            if active_2d[r, c] and (c == 0 or not active_2d[r, c - 1]):
                x0 = xverts[r, c]
                y0, y1 = yverts[r + 1, c], yverts[r, c]
                if not verts:
                    verts.append((x0, y0))
                    codes.append(Path.MOVETO)
                verts.append((x0, y1))
                codes.append(Path.LINETO)

    if verts:
        codes[-1] = Path.CLOSEPOLY
        verts.append(verts[0])
        codes.append(Path.CLOSEPOLY)
        path = Path(verts, codes)
        patch = PathPatch(path, fill=False, edgecolor="k", linewidth=2.0, label="Active model extent")
        return patch
    else:
        return None

# ============================================================
# BRESENHAM LINE IN (ROW, COL) SPACE
# ============================================================

def bresenham_rc(r0, c0, r1, c1):
    """Return list of (row, col) along line from (r0,c0) to (r1,c1)."""
    r0, c0, r1, c1 = int(r0), int(c0), int(r1), int(c1)
    dr = abs(r1 - r0)
    dc = abs(c1 - c0)
    s_r = 1 if r1 >= r0 else -1
    s_c = 1 if c1 >= c0 else -1

    pts = []
    if dc > dr:
        err = dc / 2
        r = r0
        for c in range(c0, c1 + s_c, s_c):
            pts.append((r, c))
            err -= dr
            if err < 0:
                r += s_r
                err += dc
    else:
        err = dr / 2
        c = c0
        for r in range(r0, r1 + s_r, s_r):
            pts.append((r, c))
            err -= dc
            if err < 0:
                c += s_c
                err += dr
    return pts

r0, c0 = rc_start
r1, c1 = rc_end

# Clamp to model bounds
r0 = int(np.clip(r0, 0, nrow - 1))
c0 = int(np.clip(c0, 0, ncol - 1))
r1 = int(np.clip(r1, 0, nrow - 1))
c1 = int(np.clip(c1, 0, ncol - 1))

rc_path = bresenham_rc(r0, c0, r1, c1)

# Convert (row, col) path to map coordinates for plotting/mapview
mg = ml.modelgrid
xs_path = np.array([mg.xcellcenters[r, c] for r, c in rc_path])
ys_path = np.array([mg.ycellcenters[r, c] for r, c in rc_path])

# Define line for PlotCrossSection as endpoints in map coords
xs_line = [(xs_path[0], ys_path[0]), (xs_path[-1], ys_path[-1])]

# Distance along section for heads
dxs = np.diff(xs_path)
dys = np.diff(ys_path)
dist = np.concatenate(([0.0], np.cumsum(np.sqrt(dxs**2 + dys**2))))

# ============================================================
# CLEAN HEADS
# ============================================================

head_clean = head.astype(float)
hnoflo = ml.bas6.hnoflo
hdry = None
if getattr(ml, "lpf", None) is not None:
    try:
        hdry = ml.lpf.hdry
    except AttributeError:
        hdry = None

head_clean[head_clean == hnoflo] = np.nan
if hdry is not None:
    head_clean[head_clean == hdry] = np.nan

h9 = head_clean[k_target, :, :]

# Heads along the path (one per (row, col))
h_line = np.array([h9[r, c] for r, c in rc_path], dtype=float)
valid = np.isfinite(h_line)
dist_clean = dist[valid]
h_line_clean = h_line[valid]

# ============================================================
# FIGURE WITH CROSS-SECTION + PLAN VIEW
# ============================================================

fig, (ax_xs, ax_map) = plt.subplots(
    2, 1, figsize=(11, 9), gridspec_kw={"height_ratios": [2.2, 1]}
)

# ------------------------------------------------------------
# CROSS-SECTION
# ------------------------------------------------------------

xsect = flopy.plot.PlotCrossSection(
    model=ml,
    line={"line": xs_line},
    geographic_coords=True,
)

if color_mode.lower() == "hk":
    hk = None
    if getattr(ml, "lpf", None) is not None:
        hk = ml.lpf.hk.array
    elif getattr(ml, "upw", None) is not None:
        hk = ml.upw.hk.array
    elif getattr(ml, "huf", None) is not None:
        hk = ml.huf.hk.array
    else:
        raise RuntimeError("No LPF, UPW, or HUF package found; cannot retrieve hk.")

    csa = xsect.plot_array(
        hk,
        masked_values=[0.0, ml.bas6.hnoflo],
        cmap="viridis",
        ax=ax_xs,
    )
    cb = plt.colorbar(csa, ax=ax_xs, shrink=0.7)
    cb.set_label("Horizontal hydraulic conductivity (L/T)")

else:
    layer_ids = np.zeros((nlay, nrow, ncol), dtype=int)
    for k in range(nlay):
        layer_ids[k, :, :] = k

    csa = xsect.plot_array(
        layer_ids,
        masked_values=[ml.bas6.hnoflo],
        cmap="tab20",
        ax=ax_xs,
    )
    cb = plt.colorbar(csa, ax=ax_xs, shrink=0.7)
    cb.set_label("Layer index")

if show_grid:
    xsect.plot_grid(color="k", linewidth=0.2, ax=ax_xs)
else:
    xsect.plot_grid(color="k", linewidth=0.0, ax=ax_xs)

# Potentiometric surface along the path (distance vs head)
ax_xs.plot(
    dist_clean,
    h_line_clean,
    "r-",
    linewidth=2.0,
    label=f"Potentiometric surface (Layer {target_layer_num})",
)

ax_xs.set_ylim(zmin_plot, zmax_plot)
ax_xs.set_xlabel("Distance along cross-section (model units)")
ax_xs.set_ylabel("Elevation (ft NAVD88)")
ax_xs.set_title(
    f"Cross-section from (row {r0}, col {c0}) to (row {r1}, col {c1})"
)
ax_xs.legend(loc="best")

# ------------------------------------------------------------
# PLAN VIEW: GRID + SECTION PATH
# ------------------------------------------------------------

# ------------------------------------------------------------
# PLAN VIEW: GRID + SECTION PATH
# ------------------------------------------------------------

# ------------------------------------------------------------
# PLAN VIEW: GRID + SECTION PATH
# ------------------------------------------------------------

mapview = flopy.plot.PlotMapView(model=ml)
mapview.plot_grid(ax=ax_map, linewidth=0.5, color="0.7")

# Cross-section line
ax_map.plot(xs_path, ys_path, "r-", linewidth=2.0, label="Cross-section line")

# Active model extent outline from active_2d mask
xv = ml.modelgrid.xcellcenters[0, :]  # length ncol
yv = ml.modelgrid.ycellcenters[:, 0]  # length nrow
X, Y = np.meshgrid(xv, yv)

ax_map.contour(
    X, Y, active_2d.astype(int),
    levels=[0.5],
    colors="k",
    linewidths=2.0,
)

# Legend handle for active extent (dummy line)
ax_map.plot([], [], "k-", linewidth=2.0, label="Active model extent")

x_min, x_max, y_min, y_max = ml.modelgrid.extent
ax_map.set_xlim(x_min, x_max)
ax_map.set_ylim(y_min, y_max)
ax_map.set_aspect("equal")

ax_map.set_xlabel("X (model / map units)")
ax_map.set_ylabel("Y (model / map units)")
ax_map.set_title("Plan view of model grid and cross-section line")
ax_map.legend(loc="best")

# ============================================================
# SAVE AND SHOW
# ============================================================

plt.tight_layout()
plt.savefig(out_png, dpi=300, bbox_inches="tight")
plt.show()
