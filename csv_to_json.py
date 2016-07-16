#! /usr/bin/env python
"""
Coverts CSV file to json_serde file
Use of pandas allows simpler detection and processing data types
TODO: Add true getops
"""
from sys import argv, exit
import pandas as pd
import json

if len(argv) != 3:
	print "Usage: python %s infile outfile" % argv[0]
	exit(1)

CSV_FILE = argv[1]
JSON_FILE = argv[2]

df = pd.read_csv(CSV_FILE)
df.to_json(orient='records', path_or_buf=JSON_FILE,
	date_format='iso', double_precision=4)

print "Wrote %d records to %s" % (len(df.index), JSON_FILE)