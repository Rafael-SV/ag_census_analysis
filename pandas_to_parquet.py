import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import numpy as np
import pickle
import re

with open('truncated_ag_census_2002.txt') as f:
	census_02_dataframe = pd.read_csv(f, sep='\t', lineterminator='\n',  header=0, low_memory=False)

table = pa.Table.from_pandas(census_02_dataframe)
pq.write_table(table, 'census_truncated.parquet')
