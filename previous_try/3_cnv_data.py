#!usr/bin/python3

"""
a)  scatterplot, x = position_mb, y = log2_ratio
b) save plot to file
c)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotnine import ggplot, geom_point, ggtitle


# Variables:
dataset = pd.read_csv('cnv_data.csv')
plot_title = 'CNV'
x_axis = 'position_mb'
x_label = 'Position mb'
y_axis = 'log2_ratio'
y_label = 'log2 ratio'
print(dataset)

plotly_fig = px.scatter(dataset, x=x_axis, y=y_axis, title=plot_title)
plotly_fig.write_image(f'{plot_title}.png')  #apparently need kaleido for this but it is what it is. and chrome. Prb should have chosen smth else