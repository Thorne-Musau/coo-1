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

#DEaling with missing data
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)

df["bore"].replace(np.nan, avg_bore, inplace=True)
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

# Data Standardization
# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]

# check your transformed data 
df.head()

#Data Normalization
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()


#Binning
# Binning is a process of transforming continuous numerical variables into discrete categorical 'bins' for grouped analysis.
# df["horsepower"]=df["horsepower"].astype(int, copy=True)
plt.plot.hist (df['horsepower'])

#set x/y labels and plot
plt.plot.xlabel("horsepower")
plt.plot.ylabel("count")
plt.plot.title("horsepower bins")

bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
bins