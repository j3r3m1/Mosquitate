#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 08:44:38 2021

@author: Jérémy Bernard, University of Gothenburg
"""
import pandas as pd
import datetime
import glob
from pathlib import Path
import os
import matplotlib.pylab as plt


###############################################################################
#################### Parameters that should be changed ########################
###############################################################################
# Type of measurement to load ("calibration" or "measurement")
measurementType = "measurement"

# If measurementType = "measurement", time to keep for the analysis
timeRange = ["00:00", "03:00"]

###############################################################################
#################### Parameters that should not change ########################
###############################################################################
# Date where all sensors were set (if measurementType = "measurement") or 
# where the comparison is possible (if measurementType = "calibration")
datesToKeep = {"measurement": [datetime.datetime(2021, 6, 30), datetime.datetime.now()],
               "calibration": [datetime.datetime(2021,6,15), datetime.datetime(2021,6,16)]}

# Number of times data have been collected
nbColl = 3

# Path for data
dataPath = Path(os.curdir).absolute().parent.joinpath("Data")
relPathCalibBefore = str(dataPath.joinpath(os.path.join("raw", "CalibrationBefore")))
relPathOnsite = str(dataPath.joinpath(os.path.join("raw")))

# Sampling period (min)
dt = 10


###############################################################################
#################### Read the data ############################################
############################################################################### 
# Get the current working directory
currentDir = str(Path(os.path.abspath(os.curdir)))

# Get a list of all data files
listOfFiles = {}
if measurementType == "calibration":
    listOfFiles[1] = glob.glob(os.path.join(relPathCalibBefore+"*.txt"))
elif measurementType == "measurement":
    listOfFiles = {i: glob.glob(os.path.join(relPathOnsite, str(i), "*.txt")) 
                       for i in range(1, nbColl+1)}

df_temp = {}
df_rhum = {}
for k in listOfFiles:
    # Read temperature data
    df_temp[k] = pd.DataFrame(
                {i.split(os.sep)[-1].split("-")[0]:
                     pd.read_csv(i, sep="\t", header=0, skiprows=[1],
                                 index_col=0, parse_dates=True,
                                 decimal=",", encoding="ISO-8859-1")["Temperature"]\
                         .rename(i.split(os.sep)[-1].split("-")[0])
                     for i in listOfFiles[k]})
    
    # Read relative humidity data
    df_rhum[k] = pd.DataFrame(
                {i.split(os.sep)[-1].split("-")[0]:
                     pd.read_csv(i, sep="\t", header=0, skiprows=[1],
                                 index_col=0, parse_dates=True,
                                 decimal=",", encoding="ISO-8859-1")["Humidity"]\
                         .rename(i.split(os.sep)[-1].split("-")[0])
                     for i in listOfFiles[k]})

df_temp = pd.concat(df_temp.values())
df_rhum = pd.concat(df_rhum.values())
# Drop potential duplicated index
df_temp = df_temp.groupby(df_temp.index).first()
df_rhum = df_rhum.groupby(df_rhum.index).first()

# Data were recorded at the same time, thus interpolation is needed and then take every 10 minutes recording
if measurementType == "calibration":
    new_index = pd.date_range(start = df_temp.index[0], end = df_temp.index[-1], freq = pd.offsets.Minute(1))
    df_temp = df_temp.reindex(new_index).interpolate(method = "time", limit = dt).resample(str(dt)+"T").first()
    df_rhum = df_rhum.reindex(new_index).interpolate(method = "time", limit = dt).resample(str(dt)+"T").first()

###############################################################################
#################### Plot the data ############################################
############################################################################### 
# Calculate difference to the mean for each time step
df_diff_temp = df_temp.subtract(df_temp.mean(axis = 1), axis = 0)

# Creates a figure with all sensors temporal variation in the first axis,
# difference to the mean of all sensors on the second axis
fig, ax = plt.subplots(nrows = 2, ncols = 1, sharex = True)
df_temp.plot(ax = ax[0])
df_diff_temp.plot(ax = ax[1])

# Select only data for the date range defined for the given analysis
df_diff_temp = df_diff_temp[(df_diff_temp.index >= datesToKeep[measurementType][0])
                            & (df_diff_temp.index <= datesToKeep[measurementType][1])]
df_temp = df_temp[(df_temp.index >= datesToKeep[measurementType][0]) 
                  & (df_temp.index <= datesToKeep[measurementType][1])]

# Select only certain time of the day ('timeRange') if measurementType = "measurement"
if measurementType == "measurement":
    df_diff_temp = df_diff_temp.between_time(start_time = timeRange[0],
                                             end_time = timeRange[1])

# Plot boxplot
df_diff_temp.boxplot()