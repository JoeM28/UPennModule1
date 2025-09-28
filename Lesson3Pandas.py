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
df3=DataFrame(np.random.rand(5,3),index=index,columns=['X','Y','Z'])
print(df3)

#print("Transposed random DataFrame:")
#print(df3.T)
print("Data types of random DataFrame columns:")
print(df3.dtypes)

df4=df3.reindex(index=['a','bb','c','dd','ee','f'])
print("Reindexed DataFrame with some new labels:")
print(df4)


df4=df4.reset_index(drop=True)
print("DataFrame after resetting index:")
print(df4)

df5=df4
print("Copy of DataFrame df4 into df5:")
print(df5)
#df5.loc[0]['X']=25
#print("Modified DataFrame df5:")
#print(df5)
#print("Original DataFrame df4 remains unchanged:")
#print(df4)
print(" df5.drop('2') does not work")
#df6=df5.drop(2)
df6=df5.drop(2).drop('Y',axis=1)
print("DataFrame df6 after dropping row with index '2':")
print(df6)
print("Original DataFrame df5 remains unchanged:")
print(df5)
print("Selecting column 'X' from df5:")
print(df5['X'])
print("Selecting column 'X' and 'Y' from df5:")
print(df5[['X','Y']])
print("Selecting rows with index labels X")
print("Selecting all rows and column 'X' from df5 using .loc:")
print(df5.loc[:,'X'])
print("Selecting all rows and the second column from df5 using .iloc:")
print(df5.iloc[:,1])
print("Selecting df4 now")
print(df4)
print("Reindexing df4 with new index labels:")
df4=df4.reindex(index=['a','bb','c','dd','ee','f',0,2])
print(df4)
print("Printing df3 (random DataFrame):")
print(df3)
print("Printing data types of df3 columns:")
print(df3.dtypes)
print("Selecting column 'X' from df3:")
print(df3['X'])
print("Selecting columns 'Y' and 'Z' from df3 using .loc:")
print(df3.loc[:,['Y','Z']])
print("Selecting columns 'Y' and 'Z' from df3 using double brackets:")
print(df3[['Y','Z']])
print("Selecting row with index 'c' from df3 using .loc:")
print(df3.loc['c'])
print("Selecting row at position 2 from df3 using .iloc:")
print(df3.iloc[2])
print("Selecting rows at positions 1 and 2 from df3 using .iloc:")
print(df3.iloc[1:3])

print("Access value at row 'c' and column 'Y'")
print(df3.at['c','Y'])
print("Access value at row index 2 and column index 1")
print(df3.loc['c','Y'])
print("Access value at row index 2 and column index 1 using iat")
print(df3.iat[2,1])
print("Access value at row index 2 and column index 1 using iloc")
print(df3.iloc[2,1])
print(df3)
print("Boolean indexing - rows where column 'X' > 0.5")
print(df3[df3['X'] > 0.5])
print(df3['X'] > 0.5)
print("Boolean indexing - rows where column 'X' > 0.5")
print(df3[df3.X > 0.5])
print("Boolean indexing - rows where column 'Y' < 0.5")
print(df3[df3['Y'] < 0.5])
print("Boolean indexing - rows where rows are > 0.2 and < 0.5")
print(df3[(df3 > 0.2) & (df3 < 0.5)])
print(df3.loc['d'] > 0.4)
print(df3.loc[:,df3.loc['d'] > 0.4])

import os
path = os.getcwd()
print("Current working directory:", path)
os.chdir("C:/Users/mohan/Documents/PythonCode/UPennModule1/UPennModule1")
print("Current working directory:", path)
filedata1=pd.read_csv('random_words.csv')
print(filedata1)
print(filedata1[:3])
filedata2=pd.read_table('random_words.csv', sep=',')
print(filedata2[:2])
filedata3=pd.read_table('random_noheader.csv', sep=',',header=None)
print(filedata3)
filedata4=pd.read_csv('random_noheader.csv', names=['a','b','c','d','e','f']  )
print(filedata4)
filedata5=pd.read_csv('random_words.csv', nrows=3)
print(filedata5)
filedata4.to_excel('random_words.xlsx')
filedata6 = pd.read_excel('random_words.xlsx')
print(filedata6)
filedata7 = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(filedata7)
filedata6.to_csv("random_words_out.csv")
filedata8 = pd.read_csv('random_words_out.csv')
print(filedata8)
filedata7.to_csv("irissamplenet.csv", index=False)
print(pd.read_csv("irissamplenet.csv", nrows=5))
irisdata=pd.read_csv("irissamplenet.csv")
print(irisdata)
irissub=irisdata.loc[:,irisdata.columns[:4]]
print(irissub)
irissub1 = irisdata.select_dtypes(include=[np.number])
print(irissub1 )
print(irissub.head())
print(irissub.sum())
print(irissub.mean())
print(irissub.describe())
print(irissub.head())
print(irissub.sum(axis=1,skipna=True).head())

print(irissub.count())
iris_dif=irissub.diff()
print(iris_dif[:5])
print((irisdata))
print(irisdata.species.unique())
#print(irisdata.species.count())
print(irisdata.species.value_counts())

print(irisdata.species.isin(["setosa"]))

print(irisdata.species.isin(["setosa"]).sum())
print(irisdata.sepal_length)
print(irisdata.sepal_length.corr(irisdata.petal_length))
print(irisdata.sepal_length.cov(irisdata.petal_length))
print(irisdata.sepal_length.std())
print(irisdata.corrwith(irisdata[["petal_length"]]))