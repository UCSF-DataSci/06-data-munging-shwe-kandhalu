# Data Munging Project

## 1. Initial State Analysis

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: 125718 rows
- **Columns**: income_groups, age, gender, year, population

### Column Details
| Column Name | Data Type | Non-Null Count | Unique Values |  Mean  |
|-------------|-----------|----------------|---------------|--------|
| [income_groups]  | [object]    | [119412]        | [8]      | [Mean] |
| [age]  | [float64]    | [119495]        | [101]      | [Mean] |
| [gender]  | [float64]    | [119811]        | [3]      | [Mean] |
| [year]  | [float64]    | [119516]        | [169]      | [Mean] |
| [population]  | [float64]    | [119378]        | [114925]      | [Mean] |

### Identified Issues

1. **[Issue Name, e.g., Missing Values]**
   - Description: [Detailed description of the issue]
   - Affected Column(s): [List of columns]
   - Example: [Specific example from the dataset]
   - Potential Impact: [How this could affect analysis if left uncleaned]

2. **[Next Issue]**
   - ...

[Add more issues as needed]

## 2. Data Cleaning Process

### Issue 1: [Issue Name]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Explain why you chose this method]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]

### Issue 2: [Next Issue]
- ...


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