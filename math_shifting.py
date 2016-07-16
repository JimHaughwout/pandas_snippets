"""
Useful snippets to create mapped columns and plot
"""
import pandas as pd  


# Basic filter
df[df.col_x == 1]
df[df.col_x == 1].mean()


# Basic histogram of col_x
df['df.col_x'].hist()

# Shifted
(df['raw'] - x).hist()

# Shift datetime to unix time so we can do interesting stuff
from calendar import timegm
def ts_to_unix(ts):
	"""
	Converts pandas timestamp to unix time. Useful for doing stats on time.
	"""
	try: # As Pandas
		return timegm(ts.to_datetime().utctimetuple())
	except: # As Python DateTime
		return timegm(ts.utctimetuple())

df['unix_ts'] = df['date_time'].apply(ts_to_unix)
df['unix_ts'].median()  # Or .mean() or .min() or .max()