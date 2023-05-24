import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(filename, names =headers)

df.replace("?", np.NaN, inplace=True)

print(df.head(5))
#missing data
missing_data = df.isnull()
missing_data.head(5)

#for loop to figure out the numbe rof missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print(column, missing_data[column].value_counts())
    print("")