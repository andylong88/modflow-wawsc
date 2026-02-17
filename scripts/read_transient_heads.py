# Read a binary file of modflow output heads.
# Save an output file containing heads and time for a selected model cells.

import flopy.utils.binaryfile as bf
import csv

# ---- USER INPUTS -----
headfile = '../imported_models/SES_example/output/output.SES_tr/SES_tr.hds'

# List of points as (layer, row, col) as indexed in MODFLOW (1 based).
# Python indices are zero based
# The code will subtract one from these indicies, converting to Python indices.
points = [
    (6, 199, 199),  
    (7, 199, 199),
    (9, 140, 135),      
]

# ---- EXTRACT & SAVE TIME SERIES FOR EACH CELL -----
head_obj = bf.HeadFile(headfile)

with open('../script_output/head_timeseries.csv', mode='w', newline='') as tsfile:
    tswriter = csv.writer(tsfile)
    tswriter.writerow(['Layer', 'Row', 'Column', 'Time', 'Head'])  # Header
    for (lay, row, col) in points:
        try:
            ts = head_obj.get_ts(idx=(lay - 1, row - 1, col - 1))  # timeseries: [[time, head]]
            for time, h in ts:
                tswriter.writerow([lay, row, col, time, h])  # MODFLOW-based indexing for output
        except Exception as e:
            print(f"Could not extract data for cell (layer={lay}, row={row}, col={col}): {e}")

print('Head time series saved to head_timeseries.csv')
