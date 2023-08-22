#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to view some basic statistical details like percentile, mean, std etc. of
# the species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris-virginica’.

# In[14]:


import pandas as pd
df=pd.read_csv(r'C:\Users\91888\Downloads\iris.csv')


# In[8]:


setosa=df['Species']=='Iris-setosa'
df[setosa].describe()


# In[10]:


iris_versicolor=df['Species']=='Iris-versicolor'
df[iris_versicolor].describe()


# In[13]:


iris_virginica=df['Species']=='Iris-virginica'
df[iris_virginica].describe()


# Descriptive Statistics - Measures of Central Tendency and variability
# Perform the following operations on any open source dataset (e.g., data.csv)

# In[15]:


import numpy as np
import statistics as st
df1=pd.read_csv(r'C:\Users\91888\Downloads\loan.csv')
print(df1.mean())


# In[26]:


print(df.mean(axis=1))


# In[ ]:




