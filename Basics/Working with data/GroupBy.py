import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename="/home/thorne/Desktop/new.csv"
df = pd.read_csv(filename)
print(df)

# GroupBy- Groups data into subsets according to diff categories
# Can bedone by grouping a single or multiple var

df_test= df[["drive-wheels", "body-style", "price"]]
df_grp= df_test.groupby(["drive-wheels", "body-style"], as_index=False).mean()