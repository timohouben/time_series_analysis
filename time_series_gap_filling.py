# -*- coding: utf-8 -*-
"""
Script to fill gaps in time series.
Written: March 2020, Timo Houben

version 1.0.0

Parameter
---------

path : string
    Path to the directory of multiple input files.

Yields
------

A folder called "time_series_TIME_NOW" with subfolders:
    - plots: plots for every time series and the interpolation
    - output: interpolated time series with different methods
    - log: file containing information about the input time series

This script is tailored to the following file type:

6335820  ID from GRDC discharge database; (Abfluss) DAILY
nodata   -9999.000
n       1 measurement per day [1, 1440]
start   1951 01 01 00 00 (YYYY MM DD HH MM)
end     2017 12 31 00 00 (YYYY MM DD HH MM)
1951 01 01 00 00       1.290
1951 01 02 00 00       1.140
1951 01 03 00 00       1.090
1951 01 04 00 00       1.090
1951 01 05 00 00       1.090
1951 01 06 00 00       1.180
1951 01 07 00 00       1.230
1951 01 08 00 00       1.720
1951 01 09 00 00       1.670
1951 01 10 00 00       1.280
1951 01 11 00 00       1.180
"""
###############################################################################
# module import
###############################################################################
# python 2 and 3 compatible
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
import glob
from itertools import islice
from datetime import datetime, timedelta
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
plt.style.use("fivethirtyeight")
plt.tight_layout()
# get the path from first argument
try:
    path = sys.argv[1]
except IndexError:
    # or insert path after starting the script
    path = input("Please insert the path to multiple input files: ")

# get the list of files in directory
listdir = glob.glob(os.path.join(path, "*"))

# get the time
time_now = datetime.now()
time_now_hr = time_now.strftime("%Y %b %d, %H:%M h")
time_now_log = time_now.strftime("%Y%m%d%H%M")
logfilename = time_now_log + ".log"

# set some output folders
dirname = os.path.dirname(path)
result_folder = "time_series_" + time_now_log
output_folders = [result_folder] + [
    os.path.join(result_folder, folder) for folder in ["plots", "data"]
]
# make result and output folders
for folder in output_folders:
    if not os.path.exists(os.path.join(dirname, folder)):
        os.mkdir(os.path.join(dirname, folder))

# create a log file with current time
log = open(os.path.join(dirname, result_folder, logfilename), "w")
print("Time series analysis: Time " + time_now_hr, file=log)
print(
    "###############################################################################",
    file=log,
)

###############################################################################
# The following variables can be adjusted according to the needs
###############################################################################
# specifiy the number of lines of the header
header_length = 5
no_data_value = [
    -9999,
    -9999.0,
    -9999.00,
    -9999.000,
    -9999.0000,
    -9999.00000,
    "nan",
    "NAN",
    "Nan",
    "naN",
    "NaN",
]

# specify the interpolation
interpolation = [
    "slinear",
    "quadratic",
    #    "cubic",
    #    "barycentric",
    "piecewise_polynomial",
    #    "pchip",
]

###############################################################################
# script starts here
###############################################################################

# how many files
n_files = len(listdir)

print("Starting time series analysis " + time_now_hr)
print("Found " + str(n_files) + " to process.")

# iterate over the files
for index, filepath in enumerate(listdir):
    filename = os.path.basename(filepath)
    print(
        "###############################################################################"
    )
    print("Currently processing file " + filename + "... " + str(index + 1) + " of " + str(n_files))

    # empty lists for data columns
    dateobj_list = []
    value_list = []

    with open(os.path.join(path, filename)) as file:
        for line in islice(file, header_length, None):
            # split the line with spacings
            line_split = line.split()
            # combine first 3 entries to the date
            datestr = "-".join(line_split[0:3])
            try:
                dateobj = datetime.strptime(datestr, "%Y-%m-%d")
            except ValueError("Skipping line " + line + " due to wrong format."):
                break
            dateobj_list.append(dateobj)
            # assign value
            value = line_split[-1]
            value_list.append(value)

    # make pandas df from dict
    timeseries_df = pd.DataFrame()
    timeseries_df["date"] = dateobj_list
    timeseries_df["value"] = value_list
    # format column "value" as float64
    timeseries_df.value = timeseries_df.value.astype("float64")
    # no data values with nans
    timeseries_df = timeseries_df.replace(no_data_value, np.nan)

    # function to identify gaps and Nans and interpolate with different methds
    # set start and end and delta in days
    start = timeseries_df.date.min()
    end = timeseries_df.date.max()
    delta = end - start
    gaps = []
    checklist = timeseries_df.date.tolist()
    # check for gaps in time series
    for i in range(delta.days + 1):
        day = start + timedelta(days=i)
        # print(day, checklist[0])
        if day in checklist:
            pass
        else:
            gaps.append(day)

    # print results
    print("Filename: " + filename, file=log)
    print(
        "###############################################################################",
        file=log,
    )
    print("Start of time series: " + str(start), file=log)
    print("End of time series: " + str(end), file=log)
    print("Length of time series: " + str(delta), file=log)
    print("Number of data points: " + str(len(timeseries_df.values)), file=log)
    print("Number of missing data: " + str(len(gaps)), file=log)
    print("Number of np.nan:\n " + str(np.sum(timeseries_df.isna())), file=log)
    print("Missing data points: ", file=log)
    print([str(i) for i in gaps], file=log)

    # defining time series from min and max wihtout gaps
    date_range = pd.date_range(
        start=timeseries_df.date.min(), end=timeseries_df.date.max()
    )

    # adding missing dates to time series
    timeseries_df_new = (
        timeseries_df.set_index("date")
        .reindex(date_range)
        .fillna(np.nan)
        .rename_axis("date")
        .reset_index()
    )

    print("Added NaN for missing dates.", file=log)
    print("New number of np.nan:\n " + str(np.sum(timeseries_df_new.isna())), file=log)

    # Plot and interpolate the timeseries
    plt.figure(figsize=(16, 10))
    for method in interpolation:
        print("    Currently running interpolation: " + method)
        timeseries_interp = timeseries_df_new.interpolate(method=method, inplace=False)
        timeseries_interp.to_csv(
            os.path.join(
                dirname, result_folder, "data", filename[:-4] + "_" + method + ".txt"
            ),
            columns=["date", "value"],
            header=False,
            sep=" ",
            index=False,
            na_rep=np.nan
        )
        plt.plot(
            timeseries_interp.date,
            timeseries_interp.value,
            marker=".",
            linestyle=" ",
            label=method,
        )
    plt.plot(timeseries_df.date, timeseries_df.value, marker=".", linestyle=" ")
    x_vlines = timeseries_df_new.date[timeseries_df_new.value.isna()].tolist()

    min_vlines = (
        timeseries_df_new.value.max()
        - (timeseries_df_new.value.max() - timeseries_df_new.value.min()) * 0.2
    )
    plt.vlines(x=x_vlines, ymin=min_vlines, ymax=timeseries_df_new.value.max())
    plt.xticks(rotation=0)
    plt.ylabel("value")
    plt.xlabel("date")
    plt.legend(loc="best")
    plt.savefig(
        os.path.join(dirname, result_folder, "plots", filename[:-4] + ".png"), dpi=300
    )

    del timeseries_df
    plt.close()

time_then = datetime.now()
time_delta = time_then - time_now
time_delta_hr = "{:0.0f}".format(time_delta.seconds / 60)
print("Finished time series analysis. Time elapsed: " + time_delta_hr + " min")
print(
    "Finished time series analysis. Time elapsed: " + time_delta_hr + " min", file=log
)
log.close()
