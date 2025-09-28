import pandas as pd
import os

print("This is Assignment submission for Lesson4 Question 1")

#Question 1: Import data Assignment4_data.csv into Python from my PC Downloads folder
#Detailed explanation are provided as print statements to explain solution steps

os.chdir("C:/Users/mohan/Downloads")
print("Current Directory is ",os.getcwd())
if os.path.exists('Assignment4_data.csv'):
    data = pd.read_csv('Assignment4_data.csv')
    print("Assignment4_data.csv file is loaded into dataframe data successfully")
else:
    print("File does not exist in the directory")


#Question 1.1: Explore the data and perform a statistical analysis of the data
#Detailed explanation are provided as print statements to explain solution step
print("Answers to Question 1.1 : Explore the datasets")
print("Exploring the data :")
print("Data from top 3 rows:")
print(data.head(3))
print("Data from bottom 3 rows:")
print(data.tail(3))
print("Number of Rows and Columns is: ", data.shape)
print("Column Names are: ", data.columns)
print("Data Types of each column are: ", data.dtypes)
print("Index of the dataframe is: ", data.index)
print("Unique values in the 'variable' column are: ", data['variable'].unique())
print("Values in the dataframe first two rows are: ")
print(data.values[0:2])
print("\n------------------------------------------------")

#Question 1.2: Find and handle missing values in the data. (It is your choice how you handle the missing data.)
#Detailed explanation are provided as print statements to explain solution step
print("\nAnswers to Question 1.2 : Find and handle missing values in the data")
print("Checking for missing values in each column:")
print(data.isnull().sum())
print("Percentage of missing values in each column:")
print(data.isnull().mean() * 100)
print("Number of Rows and Columns after before missing values: ", data.shape)
print("\nHandling missing values by removing rows with any missing values")
data_cleaned = data.dropna()
#print("Data after removing rows with missing values:")
#print(data_cleaned)
print("Number of Rows and Columns after removing missing values: ", data_cleaned.shape)
print("Verifying no missing values remain:")
print(data_cleaned.isnull().sum())

print("\nAlternate way to handle missing values by filling them with column means for numeric columns and mode for categorical columns")
data_filled = data.copy()
for col in data.columns:
    if data[col].dtype in ['int64', 'float64']:  # numeric columns
        data_filled[col] = data[col].fillna(data[col].mean())
    else:  # categorical/object columns
        data_filled[col] = data[col].fillna(data[col].mode()[0])

print("Verifying no missing values remain:")
print(data_filled.isnull().sum())
print("Number of Rows and Columns after filling missing values: ", data_filled.shape)
print("\n------------------------------------------------")

#Question 1.3: Explore the variable column and convert the "variable” column to dummy variables and join the dummies to the data.
#Detailed explanation are provided as print statements to explain solution step
print("\nAnswers to Question 1.3 : Convert the 'variable' column to dummy variables and join the dummies to the data")

#Explore unique values
print("Unique values in the 'variable' column are:", data['variable'].unique())
print(sorted(data['variable'].unique()))

#Create dummy variables (force 0/1 with astype(int))
dummies = pd.get_dummies(data['variable'], prefix='var').astype(int)
print("\nDummy variables created from 'variable' column (first 3 rows):")
print(dummies.head(3))

#Join dummy variables to original dataframe
data_with_dummies = pd.concat([data, dummies], axis=1)
print("\nData after joining dummy variables (first 3 rows):")
print(data_with_dummies.head(3))

#Show shape change
print("\nNumber of Rows and Columns after adding dummy variables:", data_with_dummies.shape)

#join Dummy variables against numeric columns only
data_with_dummies_numeric = pd.concat([data.select_dtypes(include=['number']), dummies], axis=1)
print("\nData with only numeric columns and dummy variables (first 3 rows):")
print(data_with_dummies_numeric.head(3))
print("\nNumber of Rows and Columns in numeric data with dummy variables:", data_with_dummies_numeric.shape)
print("\n------------------------------------------------")

#Question 1.4: Convert the "one” column into 3 bins.
#Detailed explanation are provided as print statements to explain solution step
print("\n--- Question 1.4: Handle NaN, then quantile-based binning (qcut) on 'one' ---")

#Inspect NaNs in 'one'
nan_before = data['one'].isna().sum()
print(f"\nNaN count in 'one' BEFORE fill: {nan_before}")

#Replace NaNs in 'one' with the column mean
one_mean = data['one'].mean(skipna=True)
data['one_filled'] = data['one'].fillna(one_mean)
nan_after = data['one_filled'].isna().sum()
print(f"Mean of 'one' (used for fill): {one_mean:.2f}")
print(f"NaN count in 'one_filled' AFTER fill: {nan_after}")

#Convert the filled 'one' column into 3 quantile-based bins using qcut
data['one_qbins'] = pd.qcut(data['one_filled'], q=3, precision=2)

#Show first few rows to verify
print("\nFirst 5 rows with 'one', 'one_filled', and 'one_qbins':")
print(data[['one', 'one_filled', 'one_qbins']].head(5))

#Display bin ranges (interval categories)
print("\nBin ranges (intervals) created by qcut:")
print(data['one_qbins'].cat.categories)

#Frequency count per bin (now includes all rows since NaNs were filled)
print("\nFrequency count of values in each bin:")
print(data['one_qbins'].value_counts().sort_index())

#Summary counts
total_rows = len(data)
binned_rows = data['one_qbins'].notna().sum()
print("\nSummary:")
print(f"Total rows in dataset: {total_rows}")
print(f"Rows binned (non-NaN after fill): {binned_rows}")
print(f"Rows not binned (should be 0 after fill): {total_rows - binned_rows}")
print("\n------------------------------------------------")