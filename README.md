# Data Munging Project

## 1. Initial State Analysis

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: 125718 rows
- **Columns**: income_groups, age, gender, year, population

### Column Details
| Column Name | Data Type | Non-Null Count | Unique Values |  Mean  |
|-------------|-----------|----------------|---------------|--------|
| [income_groups]  | [object]    | [119412]        | [8]      | [N/A] |
| [age]  | [float64]    | [119495]        | [101]      | [50.00] |
| [gender]  | [float64]    | [119811]        | [3]      | [1.578] |
| [year]  | [float64]    | [119516]        | [169]      | [2025] |
| [population]  | [float64]    | [119378]        | [114925]      | [11129830] |

### Identified Issues

1. **[Missing Values]**
   - Description: [Checked for missing values across each column and added them up.]
   - Affected Column(s): [income_groups, age, geneder, year, population]
   - Example: [gender is missing 5907 values after running df.isnull().sum()]
   - Potential Impact: [Certain functions will not work if missing values are there. For example, mean() or median() of dataset will come back with errors since there are missing values present. They need to be taken out]

2. **[Duplicated Values]**
   - Description: [Checked for duplicated values across each column and added them up.]
   - Affected Column(s): [There are no duplicated columns in this dataset. However, there are 2950 duplicated rows.]
   - Potential Impact: [Duplicate rows will lead to overfitting of data which will lead to inaccurate analysis.]

3. **[Outliers]**
   - Description: [Some columns have outlying values.]
   - Affected Column(s): [population]
   - Example: [Population column has values that are outliers according to the IQR.]
   - Potential Impact: [Outliers can skew data analysis and cause over/underfitting.]

4. **[Incorrect Data Types]**
   - Description: [Some columns have incorrect data types which means the data stored in the columns do not match the expected format.]
   - Affected Column(s): [income_groups, age, gender, year, population]
   - Example: [income_groups are stores as object but should be category type.]
   - Potential Impact: [Incorrect data types can lead to errors, which produces unreliable analysis.]

## 2. Data Cleaning Process

### Issue 1: [Missing values]
- **Cleaning Method**: [Find missing values and drop rows that have missing values.]
- **Implementation**:
  ```python
df.isna().sum()
df_clean = df.dropna()
  ```
- **Justification**: [This method finds where the missing values are and simply gets rid of them. We cannot easily replace this data since we do not have a good measure of replacement, so removing the value is better.]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]

### Issue 2: [Duplicated values]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Explain why you chose this method]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]

  ### Issue 3: [Outliers]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Explain why you chose this method]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]

### Issue 4: [Incorrect Data Types]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Explain why you chose this method]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]

## 3. Final State Analysis

### Dataset Overview
- **Name**: cleaned_population_data.csv (or whatever you named it)
- **Rows**: [Your answer]
- **Columns**: [Your answer]

### Column Details
| Column Name | Data Type | Non-Null Count | #Unique Values |  Mean  |
|-------------|-----------|----------------|----------------|--------|
| [Column 1]  | [Type]    | [Count]        | [#Unique]      | [Mean] |
| ...         | ...       | ...            | ...            | ...    |

### Summary of Changes
- [List major changes made to the dataset]
- [Discuss any significant changes in data distribution]