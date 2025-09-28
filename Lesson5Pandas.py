import pandas as pd
import numpy as np

# Hierarchical indexing

data = pd.Series(np.random.randn(10),
                 index=[['a','a','a','b','b','b','c','c','d','d'],
                        [1,2,3,1,2,3,1,2,2,3]])
print("Data Is :")
print(data)
print("Data Index is :")
print(data.index)
print("Data Column b is :")
print(data['b'])
print("Data Column b:c is :")
print(data['b':'c'])
print("Data Column b:d is :")
print(data.loc[['b','d']])
print("Data loc[:,2] is")
print(data.loc[:,2])
print("Unstacked Data is :")
print(data.unstack())
print("Restacked Data is :")
data1=(data.unstack().stack())
print(data1)

#column has hierarchical index
frame = pd.DataFrame(np.arange(12).reshape((4,3)),
                     index=[['a','a','b','b'],
                            [1,2,1,2]],
                     columns=[['Ohio','Ohio','Colorado'],
                              ['Green','Red','Green']])
print("Frame is :")
print(frame)
print("Frame Index is :")
print(frame.index)
print("Frame Columns is :")
print(frame.columns)
print("Frame Column Ohio is :")
print(frame['Ohio'])
print("Frame Column Ohio Ohio is :")
print(frame['Ohio']['Green'])
print("Frame Column Colorado is :")
print(frame['Colorado'])
print("Framer Column Colorado Green is :")
print(frame['Colorado']['Green'])
print("Frame Column Ohio Red is :")
print(frame['Ohio']['Red'])
print(frame)
print("Index level 0 is :")
print(frame.index.get_level_values(0))
print(frame)
print("Index level a is :")
frame.index.names=['key1','key2']
print(frame)
print("Index level a is :")
print(frame.index.names)
print("Sum of Frame is :")
print(frame.sum())
print("Sum of Frame axis=1 is :")
print(frame.sum(axis=1))
#reordering and sortking levels
print("Reordered Frame is :")
print(frame.swaplevel('key1','key2'))
print("Sorted Frame is :")
print(frame.sort_index(level=1))
print("Sorted Frame is :")
print(frame.swaplevel(0,1).sort_index(level=0))
#Summary statistics by level
print("Sorted Frame is :")
print(frame)


# Column sum for level 1 (key1)
print("Column sum for level 1 (key1) is :")
print(frame.groupby(level='key1').sum())

# Column sum for level 0 (key2)
print("Column sum for level 0 (key2) is :")
print(frame.groupby(level='key2').sum())

# Row sum for level 0 (key1)
print("Row sum for level 0 (key1) is :")
print(frame.sum(axis=1).groupby(frame.index.get_level_values('key1')).sum())

# Row sum for level 1 (key2)
print("Row sum for level 1 (key2) is :")
print(frame.sum(axis=1).groupby(frame.index.get_level_values('key2')).sum())

#Indexing with a DataFrame column
print("DataFrame is :")
print(frame)
print("DataFrame Column Ohio is :")
print(frame['Ohio'])
print("DataFrame Column Ohio Green is :")
print(frame['Ohio']['Green'])

#set index using columns


# Example: set index using column level name 'key1'
print(frame)
print("Indexed Frame is :")
frame2_indexed = frame.reset_index().set_index('key1')
print(frame2_indexed)


# Create sample data
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'city': ['NYC', 'LA', 'Chicago', 'Boston'],
    'salary': [50000, 60000, 70000, 55000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\nDefault index:", df.index.tolist())
print("-" * 50)

# Setting 'name' as index
df_indexed = df.set_index('name')
print("\nAfter setting 'name' as index:")
print(df_indexed)
print("New index:", df_indexed.index.tolist())
print("-" * 50)

# BENEFITS OF SETTING INDEX:

# 1. Fast lookups by index
print("\n1. FAST LOOKUPS:")
print("Getting Alice's data: \n", df_indexed.loc['Alice'])
print("Getting Alice's salary: \n", df_indexed.loc['Alice', 'salary'])
print("-" * 30)

# 2. Better sorting
print("\n2. SORTING BY INDEX:")
df_sorted = df_indexed.sort_index()
print("Sorted by name (index):")
print(df_sorted)
print("-" * 30)

# 3. Easy filtering
print("\n3. FILTERING:")
print("People with names starting A-C:")
print(df_indexed.loc['Alice':'Charlie'])
print("-" * 30)

# 4. Grouping operations
sales_data = {
    'date': ['2024-01-01', '2024-01-02', '2024-01-01', '2024-01-02'],
    'product': ['A', 'A', 'B', 'B'],
    'sales': [100, 150, 200, 120]
}
sales_df = pd.DataFrame(sales_data)
print("\n4. GROUPING WITH INDEX:")
print("Sales data:")
print(sales_df)

# Set multi-index
sales_indexed = sales_df.set_index(['date', 'product'])
print("\nWith multi-index (date, product):")
print(sales_indexed)
print("\nTotal sales for 2024-01-01:")
print(sales_indexed.loc['2024-01-01'])
print("-" * 50)

# RESET_INDEX EXPLANATION:
print("\n5. RESET_INDEX:")
print("Converting index back to column:")
df_reset = df_indexed.reset_index()
print(df_reset)
print("\nWith index=False (removes old index):")
df_reset_clean = df_indexed.reset_index(drop=True)
print(df_reset_clean)
print("-" * 50)

# PRACTICAL EXAMPLE - Time Series:
dates = pd.date_range('2024-01-01', periods=4, freq='D')
prices = [100, 102, 98, 105]
stock_data = pd.DataFrame({'price': prices}, index=dates)

print("\n6. TIME SERIES EXAMPLE:")
print("Stock prices with date index:")
print(stock_data)
print("\nPrice on 2024-01-02:", stock_data.loc['2024-01-02', 'price'])
print("Prices from Jan 1-3:")
print(stock_data.loc['2024-01-01':'2024-01-03'])

# When to use set_index():
print("\n" + "="*50)
print("WHEN TO USE SET_INDEX():")
print("✓ When you frequently lookup by a specific column")
print("✓ For time series data (dates as index)")
print("✓ When you need hierarchical indexing")
print("✓ For better performance on large datasets")
print("✓ When working with groupby operations")
print("\nWhen NOT to use:")
print("✗ If you rarely access data by that column")
print("✗ If the column has duplicate values (unless intentional)")
print("✗ For simple, small datasets where performance doesn't matter")

#Merge Two Datasets

df1 = pd.DataFrame({'Key': list('aabccde'),
                    'value1': range(7)})
print(df1)

df2= pd.DataFrame({'Key': list('ace'),
                   'value2': range(4,7)})
print(df2)

print("merge df1 and df2:")
merged1=pd.merge(df1, df2)
print(merged1)
print("Merge df1 and df2 on 'Key' with  inner join:")
merged_inner = pd.merge(df1, df2, on='Key', how='inner')
print(merged_inner)
print("Merge df1 and df2 on 'Key' with  outer join:")
merged_outer = pd.merge(df1, df2, on='Key', how='outer')
print(merged_outer)
print("Merge df1 and df2 on 'Key' with  left join:")
merged_left = pd.merge(df1, df2, on='Key', how='left')
print(merged_left)
print("Merge df1 and df2 on 'Key' with  right join:")
merged_right = pd.merge(df1, df2, on='Key', how='right')
print(merged_right)

#Keys have different names in each DataFrame
df1.columns = ['key1','value1']
df2.columns = ['key2','value2']
print(df1)
print(df2)
print("Merge df1 and df2 with different key names using outer join: \n")
merged2 = pd.merge(df1, df2, left_on='key1', right_on = 'key2', how='outer')
print(merged2)
print("Merge df1 and df2 using INNER join: \n")
merged3 = pd.merge(df1, df2, left_on='key1', right_on = 'key2', how='inner')
print(merged3)
print("Merge df1 and df2 using LEFT join: \n")
merged4 = pd.merge(df1, df2, left_on='key1', right_on= 'key2', how='left')
print(merged4)
print("Merge df1 and df2 using RIGHT join: \n")
merged5 = pd.merge(df1, df2, left_on='key1', right_on= 'key2', how='right')
print(merged5)

#Concat Series

s1 = pd.Series([1,2], index=['A', 'B'])
s2=  pd.Series([2,3], index=['B', 'C'])

pd1=pd.concat([s1, s2], axis=1)
pd2=pd.concat([s1, s2])
print(s1)
print(s2)
print(pd1)
print(pd2)

#ReShape
data=pd.DataFrame(np.arange(6).reshape((2,3)),
                  index=pd.Index(['Ohio','Colorado'], name='state'),
                  columns=pd.Index(['one','two','three'], name='number'))
print(data)
result=data.stack()
print(result)
print(result.unstack())
print(result.unstack(0))
print(result.unstack('state'))
print(result.unstack('number'))
print(data)

# ---------------------------------------------
# Pandas reshape cheat sheet: melt, pivot, stack, unstack
# Using the "sales by state and product" example
# ---------------------------------------------

 

# -------------------------
# 0) Original wide DataFrame
# -------------------------
# Rows = State, Columns = Product, Values = Sales
data = pd.DataFrame(
    [[100, 200, 300],   # Ohio sales
     [400, 500, 600]],  # Colorado sales
    index=pd.Index(['Ohio', 'Colorado'], name='State'),
    columns=pd.Index(['Apples', 'Bananas', 'Cherries'], name='Product')
)

print("=== 0) Original (wide) ===")
print(data)
print("shape:", data.shape, "\n")  # (2 rows x 3 cols)

# ------------------------------------------------------
# 1) melt: wide -> long (flat tidy table for analysis)
# ------------------------------------------------------
# melt needs regular columns, so we reset_index() to bring 'State' out of the index
# id_vars: columns to keep as identifiers (stay as-is)
# var_name: name of the column that will store former column headers (Product names)
# value_name: name of the column that will store the cell values (Sales)
melted = data.reset_index().melt(
    id_vars=['State'],
    var_name='Product',
    value_name='Sales'
)

print("=== 1) Melt (wide -> long) ===")
print(melted)
print("shape:", melted.shape, "\n")  # (2*3 rows x 3 cols)

# ------------------------------------------------------
# 2) pivot: long -> wide (inverse of melt for unique combos)
# ------------------------------------------------------
# index: becomes the new row index
# columns: becomes the new set of columns
# values: what fills the cells
pivoted = melted.pivot(
    index='State',
    columns='Product',
    values='Sales'
)

print("=== 2) Pivot (long -> wide) ===")
print(pivoted)
print("shape:", pivoted.shape, "\n")  # back to (2 x 3)

# ------------------------------------------------------
# 3) stack: columns -> rows (works with indexes/levels)
# ------------------------------------------------------
# stack pushes the column level (here 'Product') into the row index,
# producing a Series with a MultiIndex (State, Product).
stacked = data.stack()          # returns a Series
stacked = stacked.rename('Sales')  # give the values a nice name

print("=== 3) Stack (columns -> rows) ===")
print(stacked)                  # MultiIndex Series: (State, Product) -> Sales
print("type:", type(stacked), "\n")

# ------------------------------------------------------
# 4) unstack: rows -> columns (inverse of stack)
# ------------------------------------------------------
# unstack pulls one index level back out into columns.
# By default, it un-stacks the last index level (here 'Product').
unstacked = stacked.unstack()   # returns a DataFrame

print("=== 4) Unstack (rows -> columns) ===")
print(unstacked)
print("shape:", unstacked.shape, "\n")

# ------------------------------------------------------
# Bonus: controlling levels (optional)
# ------------------------------------------------------
# If you had multiple index levels, you could specify which to move:
# stacked_again = data.stack(level='Product')   # same as default here
# unstacked_again = stacked.unstack(level='Product')
# print(unstacked_again)

