# clean_data.py

import pandas as pd
import numpy as np

df = pd.read_csv('messy_population_data.csv')

df.info()

df.describe(include='all')

df.isnull().sum()

df.duplicated().sum()

print(df.dtypes)

unique_counts = df.nunique()
print(unique_counts)

for col in df.columns:
    print(f"Value counts for {col}:")
    print(df[col].value_counts())