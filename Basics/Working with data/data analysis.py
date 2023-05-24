#importing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path,header=None)
df.head(5) #prints first 5 rows of the dataframe
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


#replacing dataframe headers
df.columns =headers
df.head(10)

df1=df.replace('?',np.NaN)# replacing ? NaN so the drop comma can remove the missing values

#dropping missing values
df=df1.dropna(subset=["price"], axis=0)
df.head=20

#Data types in df
print(df.dtypes)



#saving Datasets
#df.to_csv("automobile.csv", index= False)

#pd.set_option("display.max_colwidth", None)
#print(df)