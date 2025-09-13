import pandas as pd
from pandas import Series, DataFrame

import numpy as np

s1=Series([1,2,3,4,5])
s2=Series([1,2,3,4,5])
print(s1)
print(s2)
print(type(s1))
print(type(s2))
s3=Series(range(10),index=["a","b","c","d","e","f","g","h","i","j"])
print(s3)
print(s3["a"])
s3["k"]=25
print(s3)
print(s3["k"])
print(s3[['a','b']])
print(s3[s3>5])
print(s3*2)
sum1= np.sum(s3)
print(sum1)
print(s3.T)
print(s3.axes)
print(s3.dtype)
print(s3.values)
print(s3.ndim)
print(s3.size)
print(s3.shape)
print("Whatsss")
# Access value at position 0 (index 'a')
print(s3.iat[0])

# Access values at positions 0 and 1 (indices 'a' and 'b')
print(s3.iloc[[0, 1]])

# Check if all values in s3 are unique
print(s3.is_unique)

print("Starting DataFrame")

# T: Transpose (same as original for Series)
print(s3.T)

# at: Access value by label
print(s3.at["a"])

# axes: List of row axis labels
print(s3.axes)

# dtype: Data type of values
print(s3.dtype)

# empty: Check if Series is empty
print(s3.empty)

# hasnans: Check if Series contains NaNs
print(s3.hasnans)

# iat: Access value by integer position
print(s3.iat[0])

# iloc: Access values by integer positions
print(s3.iloc[[0, 1]])

# is_unique: Check if all values are unique
print(s3.is_unique)

# loc: Access value by label
print(s3.loc["a"])

# ndim: Number of dimensions
print(s3.ndim)

# shape: Shape of Series
print(s3.shape)

# size: Number of elements
print(s3.size)

# values: Series as ndarray
print(s3.values)


#dataframes

print("START New DatFrames")
import numpy as np
from pandas import DataFrame

d={'Name':["Anil","Sunil","Kumar","Ravi","Ajay"],
   'Age':[23,34,25,45,22],
   'Rating':[4.5,3.4,2.5,4.0,3.8]}

df1=DataFrame(d)

print("Full DataFrame:")
print(df1)

print("Type of df1:")
print(type(df1))

print("First 2 rows:")
print(df1.head(2))

print("Last 2 rows:")
print(df1.tail(2))

print("Column labels:")
print(df1.columns)

print("Row index:")
print(df1.index)

print("Axes (row and column labels):")
print(df1.axes)

print("Data types of each column:")
print(df1.dtypes)

print("Underlying NumPy array values:")
print(df1.values)

print("Shape (rows, columns):")
print(df1.shape)

print("Total number of elements:")
print(df1.size)

print("Number of dimensions:")
print(df1.ndim)

print("Transposed DataFrame:")
print(df1.T)

print("First 5 rows (default head):")
print(df1.head())

print("Last 5 rows (default tail):")
print(df1.tail())

print("Column labels again:")
print(df1.columns)

index=['a','b','c','d','e']
print("DataFrame with custom index labels:")
df2=DataFrame(d,index=index)
print(df2)

print("Random DataFrame with 5 rows and 3 columns:")
df3=DataFrame(np.random.rand(5,3),index=index)
print(df3)

print("Transposed random DataFrame:")
print(df3.T)
print("Data types of random DataFrame columns:")
print(df3.dtypes)