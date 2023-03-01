import pandas as pd
import numpy as np
df = pd.read_csv('iris_dataset.csv')
# Add null values to the file 
# df.loc[5, 'species'] = ''
# df.to_csv("iris_dataset.csv", index=False)
# Check for null values
bool_series = pd.isnull(df["species","sepal_lenght"])
df[bool_series]
print(df.to_string())
