import pandas as pd
import numpy as np

df = pd.read_csv('messy_population_data.csv')

# issue 1: handling missing values
df_clean = df.dropna()

# issue 2: handling duplicated values
df_clean = df.drop_duplicates()

# issue 3: outliers
numeric_df = df.select_dtypes(include='number')
    
for col in numeric_df.columns:
    Q1 = numeric_df[col].quantile(0.25)
    Q3 = numeric_df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df_clean = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

# save cleaned dataset as csv file
output = 'cleaned_population_data.csv'
df_clean.to_csv(output, index = False)
print(f"Cleaned Dataset saved as {output}")