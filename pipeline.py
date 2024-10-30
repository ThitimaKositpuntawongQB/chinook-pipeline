# Databricks notebook source
import pandas as pd
import math
import os
import configparser

# Get the parent path of the notebook
notebook_path = dbutils.entry_point.getDbutils().notebook().getContext().notebookPath().get()
parent_path = os.path.dirname('/Workspace' + notebook_path)
os.chdir(parent_path)

# read config file
config = configparser.ConfigParser()
config.read('./pipeline.conf')
inputPath = config.get('DEFAULT', 'INPUT_PATH')
outputPath = config.get('DEFAULT', 'OUTPUT_PATH')

## File path
inputpath = "/Workspace/Users/thitimak@ais.co.th/track_small.csv"
outputpath = "/Workspace/Users/thitimak@ais.co.th/output_small.csv"

## Extract
tracks = pd.read_csv(inputpath)

## Transfer
tracks['UnitPrice'] = tracks['UnitPrice'].apply(lambda x: math.ceil(x))
tracks

# Load
tracks.to_csv(outputpath, index=False)
