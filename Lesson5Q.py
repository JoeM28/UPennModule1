import pandas as pd
import os
import numpy as np
from pandas import Series, DataFrame
print("This is Assignment submission for Lesson5")
#Q1:Upload Registration.csv Download Registration.csvand Course_info.xlsx Download Course_info.xlsxinto Pandas.
#Q2:Explore and clean Registration data.
#Q3:Explore and clean Course info data.
#Q4:Which course has the highest registration
#Q5:Inner join two datasets.
#Q6:Create a data frame with student names as the index, course numbers as columns, and if the student registered a course as values (0, 1).
print("Answers to Question 1 : Import data Registration.csv and Course_info.xlsx into Python")
os.chdir("C:/Users/mohan/Downloads")
print("Current Directory is ",os.getcwd())

print("Loading Registration.csv into dataframes")
if os.path.exists('Registration.csv'):
    reg_data = pd.read_csv('Registration.csv')
    print("Registration.csv file is loaded into dataframe reg_data successfully")
else:
    print("File Registration.csv does not exist in the directory")

print("Registration Dataframe Top 3 Rows: \n", reg_data.head(3))


print("Loading Course_info.xlsx into dataframes")
if os.path.exists('Course_info.xlsx'):
    course_data = pd.read_excel('Course_info.xlsx')
    print("Course_info.xlsx file is loaded into dataframe course_data successfully")
else:
    print("File Course_info.xlsx does not exist in the directory")

print("Course       Dataframe Top 3 Rows: \n", course_data.head(3))

print("\n------------------------------------------------")


#Q2:Explore and clean Registration data.
#Detailed explanation are provided as print statements to explain solution step

print("Answers to Question 2 : Explore and clean Registration data")

print("Number of Rows and Columns is: ", reg_data.shape)
print("Column Names are: ", reg_data.columns)
print("Data Types of each column are: ", reg_data.dtypes)
print("Index of the dataframe is: ", reg_data.index)
print("Distribution of records in each column of Registration data:")
print(reg_data.describe(include='all'))

# Find records with nulls in Registration data
null_reg_data = reg_data[reg_data.isnull().any(axis=1)]
print("Records with null values in Registration data:")
print(null_reg_data)

print("\nHandling missing values by removing rows with any missing values")
reg_data_cleaned = reg_data.dropna()
print("Number of Rows and Columns after removing missing values: ", reg_data_cleaned.shape)
print("Verifying no missing values remain:")
print(reg_data_cleaned.isnull().sum())

print("\nRemoving duplicate rows if any")
reg_data_cleaned = reg_data_cleaned.drop_duplicates()
print("Number of Rows and Columns before removing duplicate rows: ", reg_data.shape)
print("Number of Rows and Columns after removing duplicate rows: ", reg_data_cleaned.shape)
print("Verifying no duplicate rows remain:")
print(reg_data_cleaned.duplicated().sum())
print("\n------------------------------------------------")

#Q3:Explore and clean Course info data.
#Detailed explanation are provided as print statements to explain solution step
print("Answers to Question 3 : Explore and clean Course info data")
print("Number of Rows and Columns is: ", course_data.shape)
print("Column Names are: ", course_data.columns)
print("Data Types of each column are: ", course_data.dtypes)
print("Index of the dataframe is: ", course_data.index)
print("Distribution of records in each column of Course info data:")
print(course_data.describe(include='all'))

# Find records with nulls in Course info data
null_course_data = course_data[course_data.isnull().any(axis=1)]
print("Records with null values in Course info data:")
print(null_course_data)
print("\nHandling missing values by removing rows with any missing values")
course_data_cleaned = course_data.dropna()
print("Number of Rows and Columns after removing missing values: ", course_data_cleaned.shape)
print("Verifying no missing values remain:")
print(course_data_cleaned.isnull().sum())
print("\nRemoving duplicate rows if any")
course_data_cleaned = course_data_cleaned.drop_duplicates()
print("Number of Rows and Columns before removing duplicate rows: ", course_data.shape)
print("Number of Rows and Columns after removing duplicate rows: ", course_data_cleaned.shape)
print("Verifying no duplicate rows remain:")
print(course_data_cleaned.duplicated().sum())
print("\n------------------------------------------------")


#Q4:Which course has the highest registration

# If you only have reg_data (not yet cleaned), do minimal cleaning:
reg_only = reg_data.copy()
reg_only['coursename'] = reg_only['coursename'].astype(str).str.strip()
print("Sample 5 records with course names : ")
print(reg_only['coursename'].head(5))
# Drop rows with missing or empty course names
reg_only = reg_only[
    reg_only['coursename'].notna() &            # drop NA/None/pd.NA
    (reg_only['coursename'].str.strip() != '')  # drop '' and whitespace-only
    ]

# Count registrations by course name
counts = (reg_only['coursename']
          .value_counts()
          .rename_axis('course_name')
          .reset_index(name='registrations'))
print("Top 5 Registration counts by course name:")
print(counts.head(5))
# Show all courses tied for the maximum
max_reg = counts['registrations'].max()
top_courses = counts[counts['registrations'] == max_reg]
print("\nTop course(s) by Course Name from Registration.csv only:")
print(top_courses.to_string(index=False))

print("\n------------------------------------------------")


#Q5 :Inner join two datasets.
print("\nAnswers to Question 5 : Inner join two datasets")

# Make sure key columns exist and are clean ---
# Strip header whitespace in the Excel table (handles 'Course Name ' → 'Course Name')
course_data_cleaned.columns = course_data_cleaned.columns.str.strip()

# Normalize join keys (strip spaces in values)
reg_data_cleaned['coursename'] = reg_data_cleaned['coursename'].astype(str).str.strip()
course_data_cleaned['Course Name'] = course_data_cleaned['Course Name'].astype(str).str.strip()

#Ensure right table has unique keys on Course Name for a clean many→one merge ---
course_keyed = (course_data_cleaned
                .sort_values(['Course Name','Course number'])   # deterministic
                .drop_duplicates(subset=['Course Name'], keep='first'))

#Inner join: keep only registrations with a matching course in course info ---
merged_data = pd.merge(
    reg_data_cleaned,
    course_keyed[['Course Name','Course number','Course Type']],
    left_on='coursename',
    right_on='Course Name',
    how='inner'      # inner join as required
)

print("Inner Joined Dataframe Top 3 Rows:\n", merged_data.head(3))
print("Inner Joined Dataframe Bottom 3 Rows:\n", merged_data.tail(3))
print("Inner Joined Dataframe Column Names:\n", merged_data.columns)

print("Rows x Cols in merged dataframe:", merged_data.shape)

# How many registration rows were kept vs. dropped by the inner join?
kept = len(merged_data)
total = len(reg_data_cleaned)
print(f"Kept {kept} of {total} registration rows ({kept/total:.1%}) after inner join.")

# List a few registration course names that did NOT match anything in course info
unmatched_names = (
    reg_data_cleaned
    .loc[~reg_data_cleaned['coursename'].isin(course_keyed['Course Name'])]
    ['coursename'].drop_duplicates().head(3)
)
if not unmatched_names.empty:
    print("Sample of non-matching course names (first 3):")
    print(unmatched_names.to_string(index=False))

print("\n------------------------------------------------")

#Q6:Create a data frame with student names as the index, course numbers as columns, and if the student registered a course as values (0, 1).
print("\nAnswers to Question 6: Create a 0/1 (registered) matrix")

#Add a registration flag
merged_data['registered'] = 1

#Build the wide matrix:
#    rows   = Student name
#    cols   = Course number
#    values = registered (1 if any registration exists, else 0)
pivot_table = (
    merged_data
    .pivot_table(index='Student name',           # <-- column name in your merged table
                 columns='Course number',        # <-- column name in your merged table
                 values='registered',
                 aggfunc='max',                  # collapse duplicates to 1
                 fill_value=0)                   # missing -> 0
    .astype(int)
)


print("Pivot Table shape (rows x cols):", pivot_table.shape)
print("Pivot Table column names (course numbers):")
print(pivot_table.columns.tolist())

print("\nPivot Table with student names as index and course numbers as columns (first 5 rows):")
print(pivot_table.head(5))

print("\nPivot Table with student names as index and course numbers as columns (last 5 rows):")
print(pivot_table.tail(5))

print("\n------------------------------------------------")



print("End of Assignment submission for Lesson5")

print("------------------------------------------------")













