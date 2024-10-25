# Data Munging Project

## 1. Initial State Analysis

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: 125718 rows
- **Columns**: income_groups, age, gender, year, population

### Column Details
| Column Name | Data Type | Non-Null Count | Unique Values |  Mean  |
|-------------|-----------|----------------|---------------|--------|
| income_groups  | object    | 119412        | 8      | N/A |
| age  | float64    | 119495        | 101      | 50.00 |
| gender  | float64    | 119811        | 3      | 1.578 |
| year  | float64    | 119516        | 169      | 2025 |
| population  | float64    | 119378        | 114925      | 11129830 |

### Identified Issues

1. **Missing Values**
   - Description: Checked for missing values across each column and added them up.
   - Affected Column(s): income_groups, age, geneder, year, population
   - Example: gender is missing 5907 values after running df.isnull().sum()
   - Potential Impact: Certain functions will not work if missing values are there. For example, mean() or median() of dataset will come back with errors since there are missing values present. They need to be taken out

2. **Duplicated Values**
   - Description: Checked for duplicated values across each column and added them up.
   - Affected Column(s): There are no duplicated columns in this dataset. However, there are 2950 duplicated rows.
   - Potential Impact: Duplicate rows will lead to overfitting of data which will lead to inaccurate analysis.

3. **Outliers**
   - Description: Some columns have outlying values.
   - Affected Column(s): population
   - Example: Population column has values that are outliers according to the IQR.
   - Potential Impact: Outliers can skew data analysis and cause over/underfitting.

## 2. Data Cleaning Process

### Issue 1: Missing values
- **Cleaning Method**: Find missing values and drop rows that have missing values.
- **Implementation**:
  ```
  df = df.dropna()
  ```
- **Justification**: This method finds where the missing values are and simply gets rid of them. We cannot easily replace this data since we do not have a good measure of replacement, so removing the value is better.
- **Impact**: 
  - Rows affected: [NUMBER]
  - Data distribution change: The summary stats remained the same after dropping missing values.

### Issue 2: Duplicated values
- **Cleaning Method**: I used df.drop_duplicates() to drop any duplicated values.
- **Implementation**:
  ```
  df = df.drop_duplicates()
  ```
- **Justification**: This function does exactly what I need it to do - removing duplicated values.
- **Impact**: 
  - Rows affected: [NUMBER]
  - Data distribution change: The summary stats remained the same after dropping duplicated values.

  ### Issue 3: Outliers
- **Cleaning Method**: Used the IQR method to check if values are outliers. Made sure to only look at dataset with numbers, as an IQR cannot be taken otherwise. I looked if the value was below or above the IQR, adn removed them.
- **Implementation**:
  ```
    numeric_df = df.select_dtypes(include='number')
    
    for col in numeric_df.columns:
        Q1 = numeric_df[col].quantile(0.25)
        Q3 = numeric_df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
  ```
- **Justification**: I needed to make sure that it only loops through the columns that were numeric, as other columns will not have an IQR. 
- **Impact**: 
  - Rows affected: population column
  - Data distribution change: The population data became more reliable after outliers were removed.

## 3. Final State Analysis

### Dataset Overview
- **Name**: cleaned_population_data.csv
- **Rows**: 95425 rows
- **Columns**: income_groups, age, gender, year, population

### Column Details
| Column Name | Data Type | Non-Null Count | #Unique Values |  Mean  |
|-------------|-----------|----------------|----------------|--------|
| income_groups  | object    | 93611        | 8      | N/A |
|  age  | float64    | 93611        | 101      | 50.12 |
|  gender  | float64    | 93611        | 3      | 1.5812 |
|  year  | float64    | 93611        | 169      | 2025 |
|  population  | float64    | 93611        | 92342      | 9234575 |

### Summary of Changes
- Missing values and duplicate values were all dropped. Outliers for the population column were also removed. Some challenges were how to approach cleaning the data. For example, for the removal of outliers, I got an error that did not let me calculate the IQR properly, as not all values are numerical. Since income_group category is not numerical, I had to find a way to create a new dataset that only included the numeric columns, so I can calculate the IQR of just those, and remove those outliers.
-  The mean, standard deviation, min, max, and IQR all changed. 