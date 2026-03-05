# Read a binary file of modflow output heads.
# Save an output file containing heads, time, and stress period for selected model cells.

import flopy.utils.binaryfile as bf
import csv

# ---- USER INPUTS -----
headfile = '../imported_models/SES_example/output/output.SES_tr/SES_tr.hds'

# List of points as (layer, row, col) as indexed in MODFLOW (1 based).
# Python indices are zero based
# The code will subtract one from these indices, converting to Python indices.
points = [
    (5, 343, 233),
    (5, 344, 232),
    (5, 337, 233),
]

# ---- EXTRACT & SAVE TIME SERIES FOR EACH CELL -----
head_obj = bf.HeadFile(headfile)

with open('../script_output/head_timeseries_withsp.csv', mode='w', newline='') as tsfile:
    tswriter = csv.writer(tsfile)
    # Added StressPeriod to the header
    tswriter.writerow(['Layer', 'Row', 'Column', 'StressPeriod', 'Time', 'Head'])

    for (lay, row, col) in points:
        try:
            # timeseries: [[time, head]]
            ts = head_obj.get_ts(idx=(lay - 1, row - 1, col - 1))

            # Get (kstp, kper) information for each time record
            kstpkper_list = head_obj.get_kstpkper()

            # Build a mapping from time to stress period (kper)
            # head_obj.times gives times in the same order as kstpkper_list
            time_to_kper = {
                t: kper for (t, (kstp, kper)) in zip(head_obj.times, kstpkper_list)
            }

            for time, h in ts:
                # Look up stress period for this time
                # If for some reason the exact time key is missing, default to None
                kper = time_to_kper.get(time, None)

                # MODFLOW-based indexing for output
                tswriter.writerow([lay, row, col, kper, time, h])

        except Exception as e:
            print(f"Could not extract data for cell (layer={lay}, row={row}, col={col}): {e}")

print('Head time series with stress period saved to head_timeseries.csv')
