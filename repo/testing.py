# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:13:08 2023

@author: 19105
"""

import pandas as pd

all_df = []

# creating df
state_df = pd.read_csv('state_parks.csv', usecols=["Park Name", "Region", "County or Counties", "Status", "Remarks"])
all_df.append(state_df)

filtered_df = state_df[state_df['Region'] == 'Piedmont']

state_names = list(filtered_df['Park Name'])


print(f"filtered: {filtered_df}")
print(f"names: {state_names}")

print(type(state_names))