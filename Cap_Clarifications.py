# -*- coding: utf-8 -*-
"""
Created on Tue May 26 10:17:12 2020

@author: us0nya
"""

# Capstone Step 3: Exploring Costs - Office Hours JK 05/07/2020
# import required modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load AAA Data 
# Load the data into a `pandas` DataFrame object
tr_path = r'C:\Users\us0nya\Documents\PGDMLAI\Data Sets\member_sample.csv'
AAA_df = pd.read_csv(tr_path, index_col =0)

#  Data Set View
pd.set_option('display.max_columns', None)  
#pd.set_option('display.expand_frame_repr', True)
pd.set_option('max_colwidth', 80)
pd.set_option('column_space',120)
pd.set_option('display.width', 120)
pd.set_option('float_format', '{:f}'.format)

# Examine head of df
print(AAA_df.head(10))