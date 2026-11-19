#!usr/bin/python3
import matplotlib.pyplot as plt
import pandas as pd

# Import data
dataset = pd.read_csv('neutrophil_isolation.csv')


# Variables:
plot_title = 'Neutrophil Isolation'
x_axis = 'cell_count_pmn_ml'
x_label = 'Cell count (PMN/ml)'
y_axis = 'purity_percent'
y_label = 'Purity (%)'

plt.scatter(dataset[x_axis],dataset[y_axis]) 
plt.title(plot_title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()

# Plot a scatterplot using matplotlib. The plot should show flipper length on the x-axis and body mass on the y-axis. Add an informative title, xlabel and ylabel. Save the plot.
plt.scatter(dataset[x_axis],[y_axis]) 
plt.title(plot_title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()

#Mess about w matplotlib
