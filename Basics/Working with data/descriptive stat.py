import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(filename, names =headers)
#print(df)

# Helps describe basic features of data
# df.describe() -Clear idea of distributions
# value_counts() -Summarize categorical data.

drive_wheel_counts=df["drive-wheels"].value_counts()
print(drive_wheel_counts)

# Box plot- Shows median, upper and lower quartile and the inter-quartile range
