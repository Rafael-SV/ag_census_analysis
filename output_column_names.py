import pyarrow as pa
import pandas as pd
import numpy as np
import pickle
import re

with open('qs.census2002.txt', 'r') as f:
	tmp = pd.read_csv(f, sep='\t', lineterminator='\n',  header=0, nrows=10000).dtypes
tmp_col = tmp.index
tmp_type = [i.name for i in tmp.values]

col_types = dict(zip(tmp_col, tmp_type))
col_types_copy = col_types.copy()
print(len(col_types))
for key, value in col_types_copy.items():
	if value == 'int64':
		col_types.update({key: 'float64'})
for key, value in col_types.items():
	if value == 'object':
		print('''StructField("{}", StringType(), True),'''.format(key))
	else:
		print('''StructField("{}", IntegerType(), True),'''.format(key))
with open('truncated_ag_census_2002.txt') as f:
	census_02_dataframe = pd.read_csv(f, sep='\t', lineterminator='\n',  header=0, dtype=col_types)

table = pa.Table.from_pandas(census_02_np_dataframe)

