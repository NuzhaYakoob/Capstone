# -*- coding: utf-8 -*-
"""
Created on Tue May 26 10:17:12 2020

@author: Nuzha
"""

#### Capstone Coding Clarifications
# member_sample_dirty.csv is the file provided. Once tidied, it will be save to member_sample_tidy.csv
# (nn) where n is an alphabet --> represent the column in the dirty .csv file

# import required modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load AAA Data 
# Load the data into a `pandas` DataFrame object
tr_path = r'C:\Users\us0nya\Documents\PGDMLAI\Data Sets\member_sample_dirty.csv'
AAA_df = pd.read_csv(tr_path, index_col =0)

#  Data Set View
pd.set_option('display.max_columns', None)  
#pd.set_option('display.expand_frame_repr', True)
pd.set_option('max_colwidth', 80)
pd.set_option('column_space',150)
pd.set_option('display.width', 120)
pd.set_option('float_format', '{:f}'.format)

# Examine head of df
print(AAA_df.head(10))
print(AAA_df.shape)

#############*** Percentage of missing data ***################################
AAA_df.isna().mean().round(4) * 100

### Percentage of non missing data ###
AAA_df.count() / len(AAA_df)*100

### Percentages of missing data  -> sorted ###
percent_missing = AAA_df.isnull().sum() * 100 / len(AAA_df)

print(percent_missing.head(50))
print(percent_missing.tail(50))

print(missing_value_df.head(50)) # -> Breakdown into smaller groups based on % data missing and determine how to impute (or delete if not a relevant feature)
print(missing_value_df.tail(50)) # ->

percent_missing = AAA_df.isnull().sum() * 100 / len(AAA_df)
percent_missing.sort_values()
percent_missing.sort_values().tail(50) # 50 features with most missing values



##############*** Dispatch and Problem Code Description #######################
###  Check whether content of columns DTL Prob1 Code Description (CJ) are identical to Dispatch Code1 Description (CH) 
###  Tested the getDuplicateColumns function on a small simple dataset where Column names are different but column content was identical => Worked as expected

AAA_df['DTL Prob1 Code Description'].value_counts(dropna=False)
AAA_df['Dispatch Code1 Description'].value_counts(dropna=False)


def getDuplicateColumns(df):
    '''
    '''
    duplicateColumnNames = set()
    # Iterate over all the columns in dataframe
    for x in range(df.shape[1]):
        # Select column at xth index.
        col = df.iloc[:, x]
        # Iterate over all the columns in DataFrame from (x+1)th index till end
        for y in range(x + 1, df.shape[1]):
            # Select column at yth index.
            otherCol = df.iloc[:, y]
            # Check if two columns at x 7 y index are equal
            if col.equals(otherCol):
                duplicateColumnNames.add(df.columns.values[y])
    return list(duplicateColumnNames)


# Get list of duplicate columns
duplicateColumnNames = getDuplicateColumns(AAA_df)
print('Duplicate Columns are as follows')
for col in duplicateColumnNames:
    print('Column name : ', col)

# Trying to verify columns CH and CJ from .csv where the content seems identical
getDuplicateColumns(AAA_df) # Empty []

# Drop duplicate columns in a DataFrame and generate a new DataFrame
AAA_new_df = AAA_df.drop(columns=getDuplicateColumns(AAA_df))
print("Modified Dataframe", AAA_new_df, sep='\n')


Cols_concat =[AAA_df['DTL Prob1 Code Description'], AAA_df['Dispatch Code1 Description'] ]
CHCJ_df=pd.concat(Cols_concat, axis=1)
print(CHCJ_df)



######### Occupation Code -> Broader Grouping ? ##############################
# 58% missing values. 
AAA_df['Occupation Code'].value_counts(dropna=False)
# Occupation Group  (BT) -> Redundant -> Drop
del AAA_df['Occupation Group']
AAA_df.shape



######### Gender Info ######################################################## 
AAA_df['Gender'].value_counts(dropna=False)
AAA_df['Right_Gender'].value_counts(dropna=False)
AAA_df['Right_Gender'].replace({"F": "Female","M":"Male","U":"Unknown"}, inplace=True)

is_missing = AAA_df['Gender'].isnull()
print(is_missing)

# Method 1: index of missing data in 'Gender' column
gender_missing_index = AAA_df[AAA_df['Gender'].isnull()].index.tolist()
print(gender_missing_index)
type(AAA_df['Gender']) # pandas.core.series.Series
type(gender_missing_index) # list

# Method 2: index of missing data in 'Gender' column
rows_with_nan = []
for index, row in AAA_df[['Gender']].iterrows():
    is_nan_series = row.isnull()
    if is_nan_series.any():
        rows_with_nan.append(index)

print(rows_with_nan)
type(rows_with_nan) # list

## HELP!: Need some input on how to code the following
# step 1: Iterate through 'Gender' column using the list 'gender_missing_index' and fill missing values with data available in 'Right_Gender' column.
# step 2: Determine how to fill remainder of missing values in the 'Gender' column.
# step 3: Delete Right_Gender column 

# Test
g = 124
print(AAA_df['Gender'].iloc[124])
AAA_df['Gender'].iloc[g] = AAA_df['Right_Gender'].iloc[g]
print(AAA_df['Gender'].iloc[124])

index = [rows_with_nan]
for index, row in AAA_df[['Gender']].iterrows():
   AAA_df['Gender'].iloc[x] = AAA_df['Right_Gender'].iloc[x]

print(AAA_df['Gender'].head(30)) # No changes reflected
print(index)



######### Dwelling Info ######################################################
# 96% of values are missing in 'Right_Dwelling Type' (BU) -> delete
del AAA_df['Right_Dwelling Type']
AAA_df.shape
# Dwelling Type (AA) 
AAA_df['Dwelling Type'].value_counts(dropna=False)



######### Normal Service / Other Info #########################################
# Clearing Code Last Description has 2 additional values - insignificant (count =1)
# Minor discrepancies in count for common values
print(AAA_df['Clearing Code Last Description'].sample(30))       # normal service CG
print(AAA_df['SC STS RSN Code Description'].sample(30))          # normal service CY
AAA_df['Clearing Code Last Description'].value_counts(dropna=False)
AAA_df['SC STS RSN Code Description'].value_counts(dropna=False)



############### Is Duplicate & Was Duplicated  ################################

AAA_df['Was Duplicated'].value_counts(dropna=False)         # DH
AAA_df['Is Duplicate'].value_counts(dropna=False)           # CL







######### Exporting DataFrame to CSV File (member_sample_tidy.csv) ###########

AAA_df.to_csv(r'C:\Users\us0nya\Documents\PGDMLAI\Data Sets\member_sample_tidy.csv', sep =',', index = False)

# the deletion of Occupation Group (column BT in .csv) and Right_Dwelling Type (Column BU) is not reflected. 





