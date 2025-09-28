import pandas as pd
import os

print("This is Assignment submission for Lesson3 Question 1 to 5")

#Question 1: Import data mtcars.csv into Python downloaded to my PC Downloads folder
#Detailed explanation are provided as print statements to explain solution steps
print("Answers to Question 1 : Import data mtcars.csv into Python")
os.chdir("C:/Users/mohan/Downloads")
print("Current Directory is ",os.getcwd())
if os.path.exists('mtcars.csv'):
    data = pd.read_csv('mtcars.csv')
    print("mtcars.csv file is loaded into dataframe data successfully")
else:
    print("File does not exist in the directory")


#Question 2: Explore the data and perform a statistical analysis of the data
#Detailed explanation are provided as print statements to explain solution step
print("Answers to Question 2 : Explore the data and perform a statistical analysis of the data")
print("Exploring the data :")
print("Data from top 2 rows:")
print(data.head(2))
print("Data from bottom 2 rows:")
print(data.tail(2))
print("Number of Rows and Columns is: ", data.shape)
print("Column Names are: ", data.columns)
print("Data Types of each column are: ", data.dtypes)
print("Index of the dataframe is: ", data.index)
print("Values in the dataframe first two rows are: ")
print(data.values[0:2])
print("Statistical Analysis of the data :")
print("Count of unique models:")
print(data.model.value_counts())
print("Descriptive statistics of the dataframe:")
print(data.describe())
print("Cars with mpg > 30")
print(data[data.mpg > 30])
print("Cars with hp > 250 listing model and hp only")
print(data.loc[data.hp > 250, ['model', 'hp']])
print("Correlation between mpg and hp across models")
print(data.mpg.corr(data.hp))
print("Covariance between mpg and hp across models")
print(data.mpg.cov(data.hp))
print(data[['mpg', 'hp']].corr())


#Question 3: Analyze mpg for cars with different gear, and show your findings.
#Detailed explanation are provided as print statements to explain solution steps
print("Answers to Question 3 : Analyze mpg for cars with different gear")
print("Unique values of gear : ", data.gear.unique())
print("Number of cars with different gear values are: ")
print(data.gear.value_counts())
print("Correlation between mpg and gear across models")
print(data.mpg.corr(data.gear))
#Moderate Positive Correlation of 0.48 indicates Cars with 4 or 5 gears are usually more fuel-efficient than those with 3 gears
print("Covariance between mpg and gear across models")
#Positive covariance indicates that as the number of gears increases, the miles per gallon (mpg) also tends to increase better fuel economy.
print(data.mpg.cov(data.gear))
print("Mean mpg for cars with different gear values:")
print(data.groupby('gear').mpg.mean())
print("Standard Deviation of mpg for cars with different gear values:")
print(data.groupby('gear').mpg.std())
print("Variance of mpg for cars with different gear values:")
print(data.groupby('gear').mpg.var())
print("Summarizing findings:")
mpg_gear_details = data.groupby('gear').mpg.agg(['mean', 'median', 'max', 'min', 'std', 'var', 'count'])
print(mpg_gear_details)

#Question 4 : Analyze mpg for cars with different carb, and show your findings.
#Detailed explanation are provided as print statements to explain solution steps
print("Answers to Question 4 : Analyze mpg for cars with different carbs")
print("Unique values of carb : ", data.carb.unique())
print("Number of cars with different carb values are: ")
print(data.carb.value_counts())
print("Correlation between mpg and carb across models")
#Negative Correlation of -0.55 indicates Cars with more carburetor the fuel economy mpg tends to be lower
print(data.mpg.corr(data.carb))
print("Covariance between mpg and carb across models")
#Negative covariance indicates that as the number of carburetors increases, the miles per gallon decreases
print(data.mpg.cov(data.carb))
print("Mean mpg for cars with different carb values:")
print(data.groupby('carb').mpg.mean())
print("Summarizing findings:")
mpg_carb_details = data.groupby('carb').mpg.agg(['mean', 'median', 'max', 'min', 'std', 'var', 'count'])
print(mpg_carb_details)


#Question 5 : Find out which attribute has the most impact on mpg.
#Detailed explanation are provided as print statements to explain solution steps
print("Answers to Question 5 : Find out which attribute has the most impact on mpg")

# --- Correlation of mpg with all other numeric columns ---
corr_with_mpg = data.corr(numeric_only=True)["mpg"].sort_values(ascending=False)

print("\nCorrelation of each attribute with mpg:\n")
print(corr_with_mpg)

# --- Find the attribute with the maximum impact (highest |correlation|, excluding mpg itself) ---
abs_corr = corr_with_mpg.drop("mpg").abs()
most_impactful = abs_corr.idxmax()
impact_val = abs_corr.max()
print(impact_val)

print(f"\nMost impactful attribute on mpg is '{most_impactful}' "
      f"with correlation = {corr_with_mpg[most_impactful]:.3f}")

#Most impactful attribute on mpg is 'wt' with correlation = -0.868


