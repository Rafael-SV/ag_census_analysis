import pandas as pd
import numpy as np
import pickle
import re

with open('qs.census2002.txt', 'r') as f:
	tmp = pd.read_csv(f, sep='\t', lineterminator='\n',  header=0, nrows=10000).dtypes
tmp_col = tmp.index
tmp_type = [i.name for i in tmp.values]

col_types = dict(zip(tmp_col, tmp_type))
print(col_types)

with open('qs.census2002.txt', 'r') as f:
	census_02_dataframe = pd.read_csv(f, sep='\t', lineterminator='\n',  header=0, dtype=col_types)

print(census_02_dataframe.head())
