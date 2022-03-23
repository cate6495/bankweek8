#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("bank-additional-full.csv")
df.head()


# In[3]:


print("Dataset shape:", df.shape)


# In[4]:


missing_values = df.isnull().sum()
missing_values


# In[5]:


df.describe()


# In[6]:


df.select_dtypes("number")


# In[7]:


# checking for skewness
df.hist(bins= 10, figsize=(14, 10))
plt.show()


# In[ ]:


# to check for outliers in the numerical columns
def outlier_vars(df, show_plot=True):
    
    outliers = []
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    num_df = df.select_dtypes(include='number')
    result = dict ((((num_df < (Q1 - 1.5 * IQR)) | (num_df > (Q3 + 1.5 * IQR)))==True).any())
    for k,v in result.items():
        if v == True:
            outliers.append(k)
    if show_plot:
        pair_plot = sns.pairplot(df[outliers]);
        print(f'{result},\n\n Visualization of outlier columns')
        return pair_plot
    else:
        return df[outliers]
    
    
outlier_vars(df)


# In[ ]:




