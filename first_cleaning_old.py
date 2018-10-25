import pandas as pd
import numpy as np
import pickle
import re

with open('trunc_02_census.txt', 'r') as f:
	census_02_ls = f.readlines()

#with open('census_02_full_ls.pkl', 'rb') as f:
	#census_02_ls = pickle.load(f)

#with open('census_02_full_ls.pkl', 'rb') as f:
#        census_02_full_ls = pickle.load(f)

state_ls = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
upper_case_states = [ i.upper() for i in state_ls]

def check_for_state(inp_str, list_of_want_to_contain):
        if any(s in inp_str for s in upper_case_states):
                return True
        else:
                return False

only_with_state_ls = []
only_no_state_ls = []

for index, item in enumerate(census_02_ls):
	if check_for_state(item, state_ls) == True or index == 0 :
		only_with_state_ls.append(item)
	else:
		only_no_state_ls.append(item)
print(only_with
census_data_frame_states = pd.read_csv('./only_with_state_ls.txt', sep='\t',   header=only_with_state_ls[0])
print(census_data_frame_states.head())

