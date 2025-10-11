import pandas as pd
import matplotlib.pyplot as plt
import os
print("This is Assignment submission for Lesson6 Question 1")

#Please use mtcars dataset Download mtcars dataset to perform the following actions:
#Q1: Plot am-based histogram to compare mpg
#Q2: Use scatterplot to plot mpg VS. hp
#Q3: Create a scatterplot matrix for new data consisting of columns [disp, hp, drat, wt, qsect].
#Q4: Create boxplots for new data consisting of columns [disp, hp, drat, wt, qsect].
#Q5: Use plots to answer which variable has the most impact on mpg.

print("Answers to Question 1 : Import data mtcars.csv into Python")
os.chdir("C:/Users/mohan/Downloads")
print("Current Directory is ",os.getcwd())
if os.path.exists('mtcars.csv'):
    data = pd.read_csv('mtcars.csv')
    print("mtcars.csv file is loaded into dataframe data successfully")
else:
    print("File does not exist in the directory")

print("Data from top 2 rows:")
print(data.head(2))
print("Number of Rows and Columns is: ", data.shape)
print("Column Names are: ", data.columns)
print("Data Types of each column are: ", data.dtypes)
print("Descriptive statistics of the dataframe:")
print(data.describe())
print("\n------------------------------------------------")

print("Question 1.1 : Plot am-based histogram to compare mpg")
# Dynamically create histograms for each unique value in 'am'

for am_value in data['am'].unique():   #for each unique value in 'am' column
    plt.hist(
        data[data.am == am_value].mpg,
        bins=10,
        density=1,
        alpha=0.5,
        label=f'am={am_value}'
    )
#plots histogram for mpg based on am values with 10 bins, density normalized, transparency 0.5, and label indicating am value
plt.ylabel('Density')  #Label y-axis
plt.xlabel('Miles Per Gallon (mpg)') #Label x-axis
plt.title('MPG Histogram by Transmission Type') #Title of the plot
plt.legend() #Show legend
plt.savefig('MPG_Histogram.pdf') #Save the plot as a PDF file
plt.show() #Display the plot
print("\n------------------------------------------------")


print("Question 1.2 : Scatterplot of mpg vs hp")

# Create scatter plot

plt.scatter(data['hp'], data['mpg'], color='blue', edgecolor='black')

# Add labels and title
plt.xlabel('Horsepower (hp)')             # X-axis label
plt.ylabel('Miles per Gallon (mpg)')      # Y-axis label
plt.title('ScatterPlot of MPG vs Horsepower (HP)')  # Title of the plot

# Optional: Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Save the figure before displaying
plt.savefig('MPG_vs_HP_Scatterplot.pdf')

# Display the plot
plt.show()


print("Question 1.3 : Create a scatterplot matrix for new data consisting of columns [disp, hp, drat, wt, qsect].")

from pandas.plotting import scatter_matrix


# Use the classic style for better aesthetics
plt.style.use('classic')

# Fix column name if needed (some files have 'qsec' instead of 'qsect')
if 'qsect' in data.columns and 'qsec' not in data.columns:
    data = data.rename(columns={'qsect': 'qsec'})

# Select relevant columns
cols = ['disp', 'hp', 'drat', 'wt', 'qsec']
subset = data[cols]

# Create scatterplot matrix with KDE on the diagonal
scatter_matrix(
    subset,
    figsize=(10, 10),
    diagonal='kde',     # Kernel Density Estimation for smoother histograms
    color='blue',       # Point color
    alpha=0.6,          # Transparency for overlapping points
    s=60,               # Point size
)

# Add a title
plt.suptitle('Scatterplot Matrix for disp, hp, drat, wt, qsec', fontsize=14)

# Save before showing
plt.savefig('Scatterplot_Matrix_mtcars.pdf')

# Display the plot
plt.show()

print("------------------------------------------------")

print("Question 1.4 : Create boxplots for new data consisting of columns [disp, hp, drat, wt, qsect].")


# Fix column name if needed (some files use 'qsec' instead of 'qsect')
if 'qsect' in data.columns and 'qsec' not in data.columns:
    data = data.rename(columns={'qsect': 'qsec'})

# Select relevant columns
cols = ['disp', 'hp', 'drat', 'wt', 'qsec']
subset = data[cols]

# Define custom color scheme (same as example)
color = dict(
    boxes='DarkGreen',     # Box border color
    whiskers='DarkOrange', # Whisker color
    medians='DarkBlue',    # Median line color
    caps='Gray'            # Cap color
)

# Plot with style similar to your reference
plt.style.use('classic')
#plt.figure(figsize=(8, 6))

# Create boxplot using Pandas (internally calls Matplotlib)
subset.plot.box(
    color=color,    # Custom colors for boxplot elements
    sym='r+',       # Red '+' marker for outliers
    grid=True       # Adds background grid
)

# Add title and labels
plt.title('Boxplots for disp, hp, drat, wt, and qsec')
plt.ylabel('Value Range')

# Save before displaying
plt.savefig('Boxplots_mtcars_Styled.pdf')

# Show the plot
plt.show()

print("------------------------------------------------")

print("Question 1.5 : Use plots to answer which variable has the most impact on mpg.")

# If your file uses qsect, normalize the name:
if 'qsect' in data.columns and 'qsec' not in data.columns:
    data = data.rename(columns={'qsect': 'qsec'})

# -----------------------------
# Column partitioning
# -----------------------------
# Numeric columns (excluding the target)
num_cols_all = data.select_dtypes(include='number').columns.drop('mpg')

# Consider columns with <= 6 unique values as categorical/discrete
# This is  good for cyl, gear, carb, am.
categorical_numeric = [c for c in num_cols_all if data[c].nunique() <= 6]
continuous_numeric  = [c for c in num_cols_all if data[c].nunique() > 6]

# Text columns (object dtype) – in mtcars this is typically just 'model'
text_cols = data.select_dtypes(include='object').columns.tolist()

print("Columns Continous , Categorical and Text")
print("Use scatter plot for Continuous numeric:", continuous_numeric)
print("Use Box plot for Categorical/discrete numeric:", categorical_numeric)
print("Use Bar chart for Text columns:", text_cols)

# =========================================================
# 1) SCATTER PLOTS (continuous numeric vs mpg)
# =========================================================
if continuous_numeric:
    cols_per_row = 3
    n = len(continuous_numeric)
    rows = (n + cols_per_row - 1) // cols_per_row

    plt.figure(figsize=(5 * cols_per_row, 4 * rows))
    plt.suptitle('MPG vs Continuous Variables', fontsize=14)

    for i, var in enumerate(continuous_numeric, 1):
        plt.subplot(rows, cols_per_row, i)
        plt.scatter(data[var], data['mpg'], color='blue', edgecolor='black', alpha=0.7)
        plt.xlabel(var)
        plt.ylabel('Miles per Gallon (mpg)')
        plt.title(f'mpg vs {var}')
        plt.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('mpg_vs_continuous_scatter.pdf')
    plt.show()

print("Using the scatter plot Check if mpg increases or decreases consistently as another variable changes")
print("From the scatter plots, we can observe the following relationships between mpg and the continuous variables:")
print("- disp (Displacement): As displacement increases, mpg tends to decrease, indicating that larger engines are less fuel-efficient.")
print("- hp (Horsepower): There is a negative correlation where higher horsepower generally corresponds to lower mpg.")
print("- drat (Rear Axle Ratio): The relationship is less clear, but there seems to be a slight positive trend where higher drat values may lead to slightly better mpg.")
print("- wt (Weight): A strong negative correlation is evident; as the weight of the car increases, mpg decreases significantly.")
print("- qsec (1/4 mile time): There is a weak positive correlation, suggesting that cars with better acceleration (lower qsec) may have slightly lower mpg.")
print("Overall, weight (wt) appears to have the most pronounced negative impact on mpg among the continuous variables.")

print("Correlation of mpg with all numeric variables:")
print(data.corr(numeric_only=True)['mpg'].sort_values(ascending=False))
print("Highest Correlation with mpg is wt (Weight) with Correlation of -0.87")
print("Graph analysis and correlation analysis both indicate that weight (wt) has the most significant impact on miles per gallon (mpg).")
print("\n------------------------------------------------")


# =========================================================
# 2) BOX PLOTS (mpg by categorical/discrete numeric columns)
#    One subplot per categorical/discrete variable
# =========================================================
if categorical_numeric:
    cols_per_row = 3
    n = len(categorical_numeric)
    rows = (n + cols_per_row - 1) // cols_per_row

    plt.figure(figsize=(5 * cols_per_row, 4 * rows))
    plt.suptitle('MPG by Categorical/Discrete Variables', fontsize=14)

    for i, var in enumerate(categorical_numeric, 1):
        ax = plt.subplot(rows, cols_per_row, i)
        # Build groups of mpg by each category level (sorted for stable order)
        levels = sorted(data[var].unique())
        groups = [data.loc[data[var] == lvl, 'mpg'] for lvl in levels]
        ax.boxplot(groups, tick_labels=[str(l) for l in levels], patch_artist=True)
        ax.set_xlabel(var)
        ax.set_ylabel('Miles per Gallon (mpg)')
        ax.set_title(f'mpg by {var}')
        ax.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('mpg_by_categorical_boxplots.pdf')
    plt.show()


print("Using Box plots Check if mpg varies significantly across different categories of a variable")
print("From the box plots, we can observe the following relationships between mpg and the categorical/discrete variables:")
print("- cyl (Number of Cylinders): Cars with fewer cylinders (4) tend to have higher mpg, while those with more cylinders (8) have lower mpg.")
print("- gear (Number of Gears): Cars with more gears (5) generally show higher mpg compared to those with fewer gears (3).")
print("- carb (Number of Carburetors): There is a trend where cars with fewer carburetors (1 or 2) tend to have higher mpg, while those with more carburetors (4 or 8) have lower mpg.")
print("- am (Transmission Type): Cars with automatic transmission (am=1) tend to have higher mpg compared to manual transmission (am=0).")
print("Overall, the number of cylinders (cyl) appears to have the most pronounced impact on mpg among the categorical/discrete variables.")
print("\n------------------------------------------------")

# =========================================================
# 3) BAR CHART for TEXT columns (e.g., model)
#    Here we plot MPG by model (sorted), horizontal for readability.
# =========================================================
for txt in text_cols:
    # If many models, a horizontal bar sorted by mpg works best
    ordered = data[[txt, 'mpg']].sort_values('mpg', ascending=False)

    plt.figure(figsize=(10, max(6, 0.35 * len(ordered))))
    plt.barh(ordered[txt], ordered['mpg'])
    plt.gca().invert_yaxis()  # highest mpg at top
    plt.xlabel('Miles per Gallon (mpg)')
    plt.ylabel(txt.capitalize())
    plt.title(f'MPG by {txt}')
    plt.grid(axis='x', linestyle='--', alpha=0.6)

    # Save one figure per text column
    safe_name = txt.replace(' ', '_')
    plt.savefig(f'mpg_by_{safe_name}_bar.pdf')
    plt.show()

print("If we consider text variable model, we see a wide range of mpg values across different car models.")
print("Toyota Corolla has the highest mpg ")


print("Overall Conclusion :")
print("From the analyses using scatter plots, box plots, and bar charts, we can conclude that several variables impact miles per gallon (mpg) in the mtcars dataset.")
print("Among continuous variables, weight (wt) has the most significant negative impact on mpg, with heavier cars generally being less fuel-efficient.")
print("Among categorical/discrete variables, the number of cylinders (cyl) shows a strong influence, where cars with fewer cylinders tend to have higher mpg.")
print("Additionally, transmission type (am) also affects mpg, with automatic transmissions generally providing better fuel efficiency.")
print("These insights can help in understanding the factors that influence fuel economy in vehicles.")


print("End of Assignment submission for Lesson6")
print("------------------------------------------------")

