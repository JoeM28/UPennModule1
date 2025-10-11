import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

from fontTools.misc.bezierTools import epsilonDigits

iris1= pd.read_csv('iris.csv')

print(iris1.head(2))
print(iris1.columns)
print(iris1.describe())


# Plot sepal length with green dashed line, line width 3
plt.plot(iris1.sepal_length, ls='--', color='g', lw=3)
plt.show()

# Plot sepal width with red solid line, line width 3
plt.plot(iris1.sepal_width, ls='-', color='r', lw=3)
plt.show()

# Plot petal length with blue dash-dot line, line width 2
plt.plot(iris1.petal_length, ls='-.', color='b', lw=2)
plt.show()

# Plot petal width with magenta dotted line, line width 2
plt.plot(iris1.petal_width, ls=':', color='m', lw=2)
plt.show()
# Multiple plots in one chart
plt.plot(iris1.sepal_length, ls='--', color='g', lw=1, label='Sepal Length')
plt.plot(iris1.sepal_width, ls='-', color='r', lw=1, label='Sepal Width')
plt.plot(iris1.petal_length, ls='-.', color='b', lw=1, label='Petal Length')
plt.plot(iris1.petal_width, ls=':', color='m', lw=1, label='Petal Width')
plt.legend()# Adds a legend to identify each line in the plot by its label
plt.ylabel('Sepal Length')
plt.title('IRIS GRAPH')
plt.ylim([0,10])  # Set y-axis limits from 0 to 9 to ensure all data points are visible within this range
plt.xticks([0,50,100,150]) # Set x-axis ticks at specified positions to improve readability
plt.show()

# Scatter plot of sepal length vs sepal width
plt.scatter(iris1.sepal_width, iris1.sepal_length, s=5, c='r')
# scatter creates a scatter plot with sepal width on the x-axis and sepal length on the y-axis and sets the size and color of the points
plt.ylabel('Sepal Length')  # Label y-axis
plt.xlabel('Sepal Width')   # Label x-axis
plt.title('Sepal Length vs Sepal Width') # Title of the plot
plt.savefig('Scatterplot.pdf')  # Save the current figure as a PDF file named 'Scatterplot.pdf'
plt.show() # Display the plot

#Assin the species to colors
plt.figure() # Create a new figure for the next plot
colors = {'setosa':'r', 'versicolor':'g', 'virginica':'b'} # Define a dictionary mapping species names to colors
# Create a scatter plot with colors based on species
plt.scatter(iris1.sepal_width, iris1.sepal_length, s=5, c=iris1.species.map(colors))
# scatter creates a scatter plot with sepal width on the x-axis and sepal length on the y-axis and sets the size and color of the points based on species
plt.ylabel('Sepal Length')  # Label y-axis
plt.xlabel('Sepal Width')   # Label x-axis
plt.title('Sepal Length vs Sepal Width by Species') # Title of the plot
import matplotlib.patches as mpatches # Import the patches module from matplotlib for creating legend handles
legend_handles = [mpatches.Patch(color=color, label=species) for species, color in colors.items()]
# Create legend handles for each species with corresponding colors
plt.legend(handles=legend_handles, title='Species') # Add a legend to the plot using the created handles
plt.show() # Display the plot

#Historgram
plt.figure()
plt.hist(iris1.sepal_length, bins=10, density =1, color='b', edgecolor='y')
plt.ylabel('Density')  # Label y-axis
plt.xlabel('Sepal Length')   # Label x-axis
plt.title('Sepal Length Histogram') # Title of the plot
plt.show()
plt.savefig('Histogram.pdf')

#multiple subplots
plt.figure()
plt.subplot(2,1,1) # Create a subplot grid with 2 rows and 1 column, and activate the first subplot
plt.plot(iris1.sepal_length, ls='--', color='g', lw=1, label='Sepal Length')


plt.subplot(2,1,2) # Activate the second subplot in the 2x1 grid
plt.plot(iris1.sepal_width, ls='-', color='r', lw=1, label='Sepal Width')
plt.show()

plt.subplot(2,2,1) # Create a subplot grid with 2 rows and 2 columns, and activate the first subplot
plt.plot(iris1.sepal_length, ls='--', color='g', lw=1, label='Sepal Length')
plt.subplot(2,2,2)
plt.plot(iris1.sepal_width, ls='-', color='r', lw=1, label='Sepal Width')
plt.subplot(2,2,3)
plt.plot(iris1.petal_length, ls='-.', color='b', lw=1, label='Petal Length')
plt.subplot(2,2,4)
plt.plot(iris1.petal_width, ls=':', color='m', lw=1, label='Petal Width')
plt.tight_layout() # Adjust subplots to fit into the figure area.

plt.subplots_adjust(top=0.9, bottom=0.1, hspace=0.4, wspace=0.4) # Manually adjust subplot parameters for better spacing
plt.show()

# fig axs method
fig, axs = plt.subplots(2, 2) # Create a figure and a 2x2 grid of subplots
axs[0, 0].plot(iris1.sepal_length, ls='--', color='g', lw=1, label='Sepal Length') # Plot on the first subplot
axs[0, 0].set_title('Sepal Length') # Set title for the first subplot
axs[0, 1].plot(iris1.sepal_width, ls='-', color='r', lw=1, label='Sepal Width') # Plot on the second subplot
axs[0, 1].set_title('Sepal Width') # Set title for the
axs[1, 0].plot(iris1.petal_length, ls='-.', color='b', lw=1, label='Petal Length') # Plot on the third subplot
axs[1, 0].set_title('Petal Length') # Set title for the third subplot
axs[1, 1].plot(iris1.petal_width, ls=':', color='m', lw=1, label='Petal Width') # Plot on the fourth subplot
axs[1, 1].set_title('Petal Width') # Set title for the fourth subplot
plt.tight_layout() # Adjust subplots to fit into the figure area.
plt.subplots_adjust(top=0.9, bottom=0.1, hspace=0.4, wspace=0.4) # Manually adjust subplot parameters for better spacing
plt.show()
# Save the figure as a PDF file
fig.savefig('Subplots.pdf')

#fig axs method to draw scatter plots , histogram and box plot
fig, axs = plt.subplots(2, 2) # Create a figure and a 2x2 grid of subplots
axs[0, 0].scatter(iris1.sepal_width, iris1.sepal_length, s=5, c='r') # Scatter plot on the first subplot
axs[0, 0].set_title('Sepal Length vs Sepal Width') # Set title for the first subplot
axs[0, 0].set_ylabel('Sepal Length')  # Label y-axis for the first subplot
axs[0, 0].set_xlabel('Sepal Width')   # Label x-axis for the first subplot
axs[0, 1].hist(iris1.sepal_length, bins=10, density =1, color='b', edgecolor='y') # Histogram on the second subplot
axs[0, 1].set_title('Sepal Length Histogram') # Set title for the second subplot
axs[0, 1].set_ylabel('Density')  # Label y
axs[0, 1].set_xlabel('Sepal Length')   # Label x-axis for the second subplot
axs[1, 0].boxplot([iris1.sepal_length, iris1.sepal_width, iris1.petal_length, iris1.petal_width],
                   labels=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']) # Box plot on the third subplot
axs[1, 0].set_title('Box Plot of Iris Features') # Set title
axs[1, 0].set_ylabel('Value')  # Label y-axis for the third subplot
axs[1, 1].axis('off') # Turn off the fourth subplot (no
axs[1, 1].set_title('Empty Plot') # Set title for the fourth subplot
plt.tight_layout() # Adjust subplots to fit into the figure area.
plt.subplots_adjust(top=0.9, bottom=0.1, hspace=0, wspace=0.4) # Manually adjust subplot parameters for better spacing
plt.show()
# Save the figure as a PDF file
fig.savefig('MultiplePlots.pdf')

#Pandas plot method
iris1.plot(y='sepal_length', use_index=True, ls='--', color='g', lw=3, title='Sepal Length') # Plot sepal length using pandas plot method
plt.ylabel('Sepal Length')  # Label y-axis
plt.xlabel('Index')   # Label x-axis
plt.ylim([0,10])  # Set y-axis limits from 0 to
plt.show()

#Line Plots
iris1.sepal_length.plot(ls='--', color='g', lw=1, title='Sepal Length') # Plot sepal length using pandas plot method
iris1.sepal_width.plot(ls='-', color='r', lw=1, title='Sepal Width') # Plot sepal width using pandas plot method
plt.legend() # Adds a legend to identify each line in the plot by its label
plt.show() # Display the plot

#Scatter plot
plt.style.use('ggplot') # Use ggplot style for the plot
colormap=iris1.species.factorize()[0] # Convert species names to numerical codes for coloring
iris1.plot.scatter(x='sepal_width', y='sepal_length', c=colormap, s=5, cmap='viridis', title='Sepal Length vs Sepal Width by Species')
# Create a scatter plot of sepal width vs sepal length with colors based on species
# x and y specify the axes, c specifies the color mapping, s sets the size of points, and cmap sets the colormap
plt.ylabel('Sepal Length')  # Label y-axis
plt.xlabel('Sepal Width')   # Label x-axis
plt.show() # Display the plot

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.style.use('ggplot')

# Factorize species → gives codes and species names
colormap, species_names = iris1.species.factorize()

# Use plt.scatter (returns a PathCollection object)
scatter = plt.scatter(
    iris1['sepal_width'],
    iris1['sepal_length'],
    c=colormap,
    s=30,
    cmap='viridis'
)

plt.xlabel('Sepal Width')
plt.ylabel('Sepal Length')
plt.title('Sepal Length vs Sepal Width by Species')

# Create legend
colors = [scatter.cmap(scatter.norm(i)) for i in range(len(species_names))]
handles = [mpatches.Patch(color=colors[i], label=species_names[i]) for i in range(len(species_names))]
plt.legend(handles=handles, title='Species', loc='upper left')

plt.show()

#Scatter matrix
plt.style.use('classic')
pd.plotting.scatter_matrix(iris1, c= colormap, s=60, diagonal='kde')
plt.show()

#Historgam against different species
fig,axs = plt.subplots(ncols=2) # Create a figure and a grid of 1 row and 2 columns of subplots
plt.tight_layout() # Adjust subplots to fit into the figure area.
iris1.groupby('species').sepal_length.plot(kind='kde' , ax=axs[1])
# Plot kernel density estimate of sepal length for each species on the first subplot
axs[1].set_title('Sepal Length Distribution by Species') # Set title for the first subplot
axs[1].set_xlabel('Sepal Length') # Label x-axis for the first subplot
axs[1].set_ylabel('Density') # Label y-axis for the first subplot
iris1.groupby("species").sepal_length.hist( ax=axs[0], alpha=0.5)
# Plot histogram of sepal length for each species on the second subplot with transparency
axs[0].set_title('Sepal Length Histogram by Species') # Set title for the second subplot
axs[0].set_xlabel('Sepal Length') # Label x-axis for the second subplot
axs[0].set_ylabel('Count') # Label y-axis for the second subplot
plt.subplots_adjust(top=0.9, bottom=0.1, hspace=0.4, wspace=0.4) # Manually adjust subplot parameters for better spacing
plt.show()
fig.savefig('HistKDE.pdf')

#box plots
color= dict(boxes='DarkGreen', whiskers='DarkOrange', medians='DarkBlue', caps='Gray')
iris1_sub = iris1.iloc[:, 0:4] # Select the first four columns of the iris1 DataFrame
iris1_sub.plot.box(color=color, sym='r+', vert=True, positions=[1, 2, 3, 4], patch_artist=True)
# Create a box plot for the selected columns with specified colors and styles
plt.title('Box Plot of Iris Features') # Set title for the plot
plt.ylabel('Value')  # Label y-axis
plt.xlabel('Features')   # Label x-axis
plt.show()
fig.savefig('Boxplot.pdf')




