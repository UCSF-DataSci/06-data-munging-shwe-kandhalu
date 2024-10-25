import pandas as pd
import numpy as np

def clean_dataset(filename, output):
    
    # read csv file input
    df = pd.read_csv(filename)

    # issue 1: handling missing values
    df = df.dropna()

    # issue 2: handling duplicated values
    df = df.drop_duplicates()

    # issue 3: outliers
    

    # issue 4: incorrect data type

    # save cleaned dataset as csv file
    df.to_csv(output, index = False)

    print(f"Cleaned Dataset saved as {output}")

clean_dataset('messy_population_data.csv', 'cleaned_population_data.csv')