"""
Useful snippets for plots in Jupyter (IPython)
"""

### Histograms 

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

%matplotlib inline

df['desired_column'].hist()
plt.title("Your chart title")
plt.ylabel("Y Axis Name")
plt.xlabel("X Axis Name")


# Using plotly

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Bar, Scatter, Figure, Layout
import plotly.plotly as py
import plotly.graph_objs as go

init_notebook_mode(connected=True) # See https://plot.ly/python/offline/

chart_title = 'Title (could be dyanmic string)'
y_value names = ['Name 1', 'Name 2']  # Can use df.columns.values.tolist()[1:]
# Can use iterator to dynamically build traces
trace1 = go.Bar(
    x=df['x_axis_col'],
    y=df['y1_col'],
    name=y_value names[0] 
)
trace2 = go.Bar(
    x=df['x_axis_col'], # Same as trace1
    y=df['y1_col'],
    name=y_value names[1] 
)
data = [trace1, trace2]
layout = go.Layout(
    title=chart_title,
    barmode='group',
    yaxis=dict(title='Static Y Category Title'),
    xaxis=dict(title='Static X Title', dtick=1.0),
)
fig = go.Figure(data=data, layout=layout)
iplot(fig, filename='grouped-bar')