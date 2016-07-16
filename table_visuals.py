"""
Useful snippets to enhance visuals in Pandas
"""
import pandas as pd 

# Sort by column
df.sort_values('column_name', ascending=False)

# Explicitly style a column
df.style.format({'column_name': "{:.2f}"})

# Using a lambda expression to be smarter
df.style.format(lambda x: int(x) if isinstance(x, float) else x)

# Using a dict
data_table = {
    'pct_col_1': '{:.1%}',
    'pct_col_2': '{:.1%}',
    'pct_col_3': '{:.1%}',
    'float_col_a': '{:.2f}',
    'float_col_c': '{:.2f}',
    'float_col_c': '{:.2f}'
}

df.style.format(data_table)


# Create your own heatmap
def heat_map(val):
    """
    Colors for HeatMap
    """
    if not isinstance(val, float):
        color = 'white'
    elif val < 50:
        color = 'red'
    elif val < 70:
        color = 'orange'
    elif val < 90:
        color = 'yellow'
    else:
        color = 'green'
    #return 'color: %s' % color
    return 'background-color: %s' % color

df.style.applymap(heat_map)