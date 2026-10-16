#!usr/bin/python3

"""
a)  scatterplot, x = position_mb, y = log2_ratio
b) save plot to file
c)
"""

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotnine import ggplot, geom_point, ggtitle

# Variables:
input_data = 'CNV_log2_skin_melanoma.csv' 
plot_title = 'CNV skin melanoma'
x_axis = 'cell_count_pmn_ml'
x_label = 'Cell count (PMN/ml)'
y_axis = 'purity_percent'
y_label = 'Purity (%)'

# Load the ‘penguins’ dataset using seaborn. Remove any rows with missing values. Hint: Check out how to use the dropna() function.
dataset = sns.load_dataset(input_data)


# Plot a scatterplot using matplotlib. The plot should show flipper length on the x-axis and body mass on the y-axis. Add an informative title, xlabel and ylabel. Save the plot.
plt.scatter(dataset[x_axis],[y_axis]) 
plt.title(plot_title)
plt.xlabel(x_label)
plt.ylabel(y_label)