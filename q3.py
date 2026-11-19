#!usr/bin/python3
import matplotlib.pyplot as plt
import pandas as pd
import sys

# Q3 a) scatterplot of cnv_data, x = log2_ratio, y = copy_number

# Import data
dataset = pd.read_csv('cnv_data.csv')

# Variables:
plot_title = 'CNV data'
x_axis = 'log2_ratio'
x_label = 'log2 ratio'
y_axis = 'copy_number'
y_label = 'Copy number'

# Scatterplot w matplotlib
# user input
# not the best solution, it worked before
csv_in = sys.argv[1]
fig_out = sys.argv[2]


# Scatterplot w matplotlib
def plot_csv(csv_in, fig_out):
    dataset = pd.read_csv(csv_in) 
    plt.scatter(dataset[x_axis],dataset[y_axis]) 
    plt.title(plot_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
    graphic = plt.savefig(fig_out, dpi='figure')
    return graphic  # Q3 b) save plot to file 




 

