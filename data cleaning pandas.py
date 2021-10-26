#!/usr/bin/env python
# coding: utf-8

# 1.Introduction
# This assignment will help you to consolidate the concepts learnt in the session.
# 2.Problem Statement
# It happens all the time: someone gives you data containing malformed strings, 
# Python, lists and missing data. How do you tidy it up so you can get on with the 
# analysis?
# Take this monstrosity as the DataFrame to use in the following puzzles:
# df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 
# 'londON_StockhOlm',
# 'Budapest_PaRis', 'Brussels_londOn'],
# 'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
# 'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
# 'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
# '12. Air France', '"Swiss Air"']})
# 1. Some values in the the FlightNumber column are missing. These numbers are 
# meant to increase by 10 with each row so 10055 and 10075 need to be put in 
# place. Fill in these missing numbers and make the column an integer column 
# (instead of a float column).
# 2. The From_To column would be better as two separate columns! Split each 
# string on the underscore delimiter _ to give a new temporary DataFrame with 
# the correct values. Assign the correct column names to this temporary 
# DataFrame.
# 3. Notice how the capitalisation of the city names is all mixed up in this 
# temporary DataFrame. Standardise the strings so that only the first letter is 
# uppercase (e.g. "londON" should become "London".)
# 4. Delete the From_To column from df and attach the temporary DataFrame 
# from the previous questions.
# 5. In the RecentDelays column, the values have been entered into the 
# DataFrame as a list. We would like each first value in its own column, each 
# second value in its own column, and so on. If there isn't an Nth value, the value 
# should be NaN.
# Expand the Series of lists into a DataFrame named delays, rename the columns 
# delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df 
# with delays.

# In[193]:


import pandas as pd
import numpy as np


# In[194]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 
                                'londON_StockhOlm',
                                'Budapest_PaRis', 'Brussels_londOn'],
                    'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                    'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                    'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                        '12. Air France', '"Swiss Air"']})


# In[195]:


df


# In[196]:


"""Some values in the the FlightNumber column are missing. 
These numbers are meant to increase by 10 with each row so 10055 and 10075 
need to be put in place. Fill in these missing numbers and make the column 
an integer column (instead of a float column)."""

df.dtypes
        
#df = df.astype({'FlightNumber': int})


# In[197]:


df['FlightNumber'][1]  = 10055


# In[198]:


df['FlightNumber'][3] = 10075


# In[199]:


df = df.astype({'FlightNumber': int})
df1 = df


# In[200]:


"""The From_To column would be better as two separate columns! Split each 
string on the underscore delimiter _ to give a new temporary DataFrame with 
the correct values. Assign the correct column names to this temporary 
DataFrame."""
from_to = df1['From_To'].str.split("_", n=1, expand =True)
df1['From'] = from_to[0]
df1['To'] = from_to[1]
df1


# In[201]:


df1.drop(columns = ['From_To'], inplace = True)


# In[202]:


df1 = df1[['From','To','FlightNumber','RecentDelays','Airline']]


# In[203]:


df1


# In[204]:


"""Notice how the capitalisation of the city names is all mixed up in this 
temporary DataFrame. Standardise the strings so that only the first letter 
is uppercase (e.g. "londON" should become "London".)"""

df1


# In[205]:


df1_from = df1['From'].str.capitalize()
df1_to = df1['To'].str.capitalize()


# In[206]:


df1['From'] = df1_from
df1['To'] = df1_to


# In[207]:


df1


# In[208]:


"""Delete the From_To column from df and attach the temporary DataFrame 
from the previous questions."""

df


# In[209]:


df.drop('From_To', axis = 1, inplace=True)
df


# In[213]:


df['From'] = df1['From']
df['To'] = df1['To']
df= df[['From','To','FlightNumber','RecentDelays','Airline']]
df


# In[ ]:


"""In the RecentDelays column, the values have been entered into the 
DataFrame as a list. We would like each first value in its own column, 
each second value in its own column, and so on. If there isn't an Nth 
value, the value should be NaN. Expand the Series of lists into a 
DataFrame named delays, rename the columns delay_1, delay_2, etc. 
and replace the unwanted RecentDelays column in df with delays."""


# In[216]:


df


# In[229]:


df['RecentDelays'][2][0]


# In[257]:


delay1 = [23,'NaN',24,13,67]
delay2 = [47,'NaN',43,'NaN',32]
delay3 = ['NaN','NaN',87,'NaN','NaN']


# In[258]:


pd.Series(delay1,dtype=object)


# In[259]:


df['Delay1'] = pd.Series(delay1,dtype=object)
df['Delay2'] = pd.Series(delay2,dtype=object)
df['Delay3'] = pd.Series(delay3,dtype= object)
       


# In[260]:


df


# In[261]:


df.drop('RecentDelays', axis = 1)


# In[ ]:




