import pandas as pd

df = pd.read_csv('vgsales.csv')

# Data Visualization
# Gives the max numbers of rows and column
print(df.shape)
# Gives the desciption of data with count, min, std, min , max , 25, 50 , 75%
print(df.describe())
print(df.values)

