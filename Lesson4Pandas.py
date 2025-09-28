from multiprocessing.managers import State

import pandas as pd  # Import pandas library for data manipulation
import numpy as np  # Import numpy library for numerical operations

np.random.seed(123)  # Set random seed for reproducibility
data = np.random.normal(2, 2, 20)  # Generate 20 random numbers from a normal distribution (mean=2, std=2)
print(data)  # Print the generated data array
data[2] = None  # Set the third element of data to None
data[np.random.randint(3, 20, 3)] = np.nan  # Randomly set 3 elements (indices 3 to 19) to NaN
data = data.reshape(4, 5)  # Reshape the data array to a 4x5 matrix
df = pd.DataFrame(data, columns=list('abcde'))  # Create a DataFrame with columns 'a' to 'e'
print(df)  # Print the DataFrame
print(df.dtypes)  # Print the data types of each column in the DataFrame
print(df.size)  # Print the total number of elements in the DataFrame
print(df.shape)  # Print the shape (rows, columns) of the DataFrame
print(df.ndim)  # Print the number of dimensions of the DataFrame
print(df.axes)  # Print the row and column labels of the DataFrame
print(df.values)  # Print the underlying NumPy array of the DataFrame
print(df.head(2))  # Print the first 2 rows of the DataFrame
df.isnull()  # Check for null values in the DataFrame
print(df.isnull())
print(df.isnull().sum())  # Print the count of null values in each column
print(df.isnull().sum(axis=0)) # Print the count of null values in each column (axis=0)
print(df.isnull().sum(axis=1)) #Print the count of null values in each row (axis=1)
print(df.isnull().values.sum()) #Print the total count of null values in the DataFrame
print(df.isnull().sum().sum()) #Print the total count of null values in the DataFrame
print(df.notnull().sum()) #print the count of non-null values in each column
print(df.notnull().sum(axis=0)) #print the count of non-null values in each column (axis=0)
print(df.notnull().sum(axis=1)) #print the count of non-null values in each row (axis=1)
print(df.notnull().values.sum()) #print the total count of non-null values in the DataFrame
print(df.notnull().sum().sum()) #print the total count of non-null values in the DataFrame
df1=df
print(df1.dropna()) #Drop rows with any null values and print the resulting DataFrame
print(df1)

print(df1.fillna(0)) #Fill null values with 0 and print the resulting DataFrame


print(df1.fillna({'b': 0.5, 'c': 1.5, 'd': 2.5, 'e': 3.5})) #Fill null values in specific columns with specified values and print the resulting DataFrame# ull values in specific columns with specified values and print the resulting DataFrame
#print(df1.fillna(method='ffill')) #Fill null values using forward fill method and print the resulting DataFrame
#print(df1.fillna(method='bfill')) #Fill null values using backward fill method and print the resulting DataFrame

print(df.fillna(df.mean())) #Fill null values with the mean of each column and print the resulting DataFrame


# Define column names for the DataFrame
k1 = 'k1'
k2 = 'k2'
# Create a DataFrame with two columns: 'k1' and 'k2'
# 'k1' contains repeated string values, 'k2' contains integer values
data = pd.DataFrame({k1: ['one', 'two'] * 2 + ['two'],
                     k2: [1, 1, 3, 4, 4]})
# Print the created DataFrame
print(data)

print(data.duplicated())  # Check for duplicate rows in the DataFrame and print the boolean result
print(data.duplicated().sum())  # Print the count of duplicate rows in the DataFrame
print(data.duplicated(subset=[k1]))  # Check for duplicate rows based on column 'k1' and print the boolean result
print(data.duplicated(subset=[k1]).sum())  # Print the count of duplicate rows based on column 'k1'

print(data.drop_duplicates())  # Drop duplicate rows and print the resulting DataFrame
print(data.drop_duplicates(subset=[k1]))  # Drop duplicate rows based on column '
print(data.drop_duplicates(subset=[k1], keep='last'))  # Drop duplicate rows based on column 'k1', keeping the last occurrence, and print the resulting DataFrame


data = pd.DataFrame({
    'City':['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
    'Population':[15,12,11,10,9,8,17,4,15,14]
})
print(data)

city_state = {
    'New York': 'NY',
    'Los Angeles': 'CA',
    'Chicago': 'IL',
    'Houston': 'TX',
    'Phoenix': 'AZ',
    'Philadelphia': 'PA',
    'San Antonio': 'TX',
    'San Diego': 'CA',
    'Dallas': 'TX',
    'San Jose': 'CA'
}

print(city_state)

#data['State'] = data.City.map(city_state) # Map city names to state abbreviations and create a new 'State' column
#print(data) # Print the updated DataFrame with the new 'State' column

#data['State'] = data['City'].map(city_state)  # Map city names to state abbreviations and create a new 'State' column
#print(data)  # Print the updated DataFrame with the new 'State' column


# Fixed unresolved reference 'city' in lambda function
data['State']=data['City'].map(lambda x: city_state[x]) # Map city names to state abbreviations using a lambda function
print(data) # Print the updated DataFrame with the new 'State' column

data['State1']=data['City'].map(lambda x: city_state.get(x)) # Map city names to state abbreviations using a lambda function with get method
print(data) # Print the updated DataFrame with the new 'State1' column

#replace values
np.random.seed(189) # Set random seedfor reproducibility
data=np.random.randint(-20, 20, 12) # Generate 12 random integers between -20 and 20
print(data) # Print the generated data array
data[np.random.randint(0, 11, 3)] = -100 # Randomly set 3 elements (indices 0 to 11) to -100
print(data) # Print the modifieddata array
data = data.reshape(4,3) # Reshape the data array to a 4x3 matrix
print(data)  # Print the reshaped data array
df=pd.DataFrame(data, columns=list('abc'))  # Create a DataFrame with columns 'a' to 'c'
print(df)  # Print the DataFrame

print(df.replace(-100, np.nan))  # Replace -100 with NaN and print the resulting DataFrame
print(df.replace([-100, -20, 5], np.nan)) # Replace -100, -10, and 0 with NaN and print the resulting DataFrame

np.random.seed(123)
data=pd.DataFrame(np.random.randn(1000,4), columns=list('ABCD')) # Create a DataFrame with 1000 rows and 4 columns of random numbers
print(data) # Print the DataFrame
print(data.describe()) # Print summary statistics of the DataFrame

#col2=data[2]
#print(col2[np.abs(col2) > 3]) # Print values in column 'B' where the absolute value is greater than 3

col2 = data['B'] # Access column 'B' of the DataFrame
print(col2)
print(col2[np.abs(col2) > 1]) # Print values in colum   n 'B' where the absolute value is greater than 3
print(np.abs(data) > 3) # Print a boolean DataFrame indicating where absolute values are greater than 3


print(data.describe())
print(data[(np.abs(data) > 3).any(axis=1)]) # Print rows where any column has an absolute value greater than 3
data[(np.abs(data) > 3)] = np.sign(data)*3
print(data.describe()) # Print summary statistics of the modified DataFrame

#Discretiziation and Binning
values =     np.random.randint(18,54,10) # Generate 10 random integers between 18 and 54
print(values)
bins = np.array([0] + list(range(1,5)) + [np.inf] ) * 10 # Define bin edges for categorization
print(bins)


import numpy as np

values = np.random.randint(18,50,10)
bins = [0, 10, 20, 30, 40, np.inf]

bin_index = np.digitize(values, bins)
print("Values:", values)
print("Bins:", bins)
print("Bin indices:", bin_index)
categories = ['0-10', '10-20', '20-30', '30-40', '40+']
categorized_values = [categories[i-1] for i in bin_index]
print(categorized_values)
cats = pd.cut(values, bins)
print(cats)
print(cats.codes)
print("Categories")
print(cats.categories)
print("value counts")
#print(pd.value_counts(cats))
#print(pd.cut(values,5,precision=2))

values2 = np.random.randn(100)
print(values2)
cats2 = pd.qcut(values2, 4)
print(cats2)
print(pd.value_counts(cats2))
print(pd.value_counts(pd.qcut(values2, [0,0.1,0.5,0.9,1.0])))

df = pd.DataFrame({
    'Key' : ['b','c','a','e','b','b'] ,
    'data1' : range(6) })
print(df)
print(pd.get_dummies(df['Key']))
dummies = pd.get_dummies(df['Key'], prefix='Key')
print(dummies)

df_with_dummy = df[['data1']].join(dummies)
print(df_with_dummy)

#String operation
s = "Python is a great tool for data anlaysis"

words = s.split()
print(words)

y = [w.upper() for w in words]
print(y)

s1= ' '.join(words)
print(s1)

print('data' in s)
print(s.index('for'))
print(s.find('new'))
print(s.count('for'))
print(s.replace('for','FOR'))
#pandas

mtcars = pd.read_csv('mtcars.csv')
print(mtcars)
sub_mtcars=mtcars.iloc[0:5,0:4]



sub_mtcars['company'] = sub_mtcars['model'].str.split().str[0]
print(sub_mtcars)

print(sub_mtcars.model.str.contains('Mazda'))
print(sub_mtcars.model.str.startswith('M'))

print(sub_mtcars.model.str[:4])

