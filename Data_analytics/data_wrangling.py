#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\91888\Downloads\nba.csv")


# In[2]:


df


# In[3]:


col=['Number','Age']
df.boxplot(col)


# In[25]:


print(np.where(df['Number']>30))


# In[5]:


print(np.where(df['Age']>35))


# In[26]:


print(np.where(df['Number']>15))


# In[27]:


print(np.where(df['Age']>20))


# In[17]:


import matplotlib.pyplot as plt
plt.scatter(df['Number'],df['Age'])
plt.xlabel('Number')
plt.ylabel('Age')
plt.show()


# In[28]:


print(np.where(df['Number']>65))


# In[22]:


Q1= df['Weight'].quantile(0.25)
Q3= df['Weight'].quantile(0.75)
Q1,Q3


# In[23]:


df.boxplot(['Weight'])


# In[29]:


iqr=Q3-Q1
iqr


# In[32]:


upper = Q3+1.5*iqr
lower = Q1-1.5*iqr
lower,upper


# In[36]:


df[(df['Weight']<lower)|(df['Weight']>upper)]


# In[37]:


remove_outliers = df[(df['Weight']>lower)&(df['Weight']<upper)]
remove_outliers


# In[38]:


df['Weight'].plot(kind='hist')


# In[41]:


df['log_math']=np.log10(df['Weight'])
df['log_math'].plot(kind='hist')


# In[42]:


df['Number'].plot(kind='hist')


# In[44]:


df['new_number']=np.log10(df['Number'])
df['new_number'].plot(kind='hist')


# In[ ]:




