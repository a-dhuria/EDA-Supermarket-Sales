#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[49]:


df = pd.read_csv('C:\\Users\\anany\\Downloads\\supermarket_sales - Sheet1.csv')
df.head(10)


# In[11]:


df.info()


# In[47]:


# Check if there is any null value or not
df.isnull().values.any()


# In[20]:


sns.countplot(x=df['Branch'])
df['Branch'].value_counts()


# In[22]:


sns.countplot(x=df['Payment'])


# In[24]:


sns.scatterplot(x=df['Rating'],y=df['gross income'])


# In[25]:


sns.boxplot(x=df['Branch'], y=df['gross income'])


# In[26]:


sns.boxplot(x=df['Gender'], y=df['gross income'])


# In[28]:


cat=df[["Product line", "gross income"]].groupby(['Product line'], as_index=False).sum().sort_values(by='gross income', ascending=False)
plt.figure(figsize=(20,8))
sns.barplot(x='Product line', y='gross income', data=cat)


# In[29]:


sns.heatmap(np.round(df.corr(),2), annot=True)


# In[31]:


plt.figure(figsize=(12, 6))
plt.title('Total Monthly transaction by Gender')
sns.countplot(x=df['Product line'], hue = df.Gender)


# In[35]:


df['Time'] = pd.to_datetime(df['Time'])
df['Hour'] = (df['Time']).dt.hour
df['Hour'].unique()


# In[36]:


sns.lineplot(x="Hour",  y = 'Quantity',data =df).set_title("Product Sales per Hour")


# In[38]:


xdata = [0,1,2,3,4,5,6,7,8,9,10]
plt.figure(figsize = (12,6))
sns.barplot(y = df['Product line'], x = df['Rating'])
plt.show(xdata)


# In[40]:


sns.boxenplot(y = 'Product line', x = 'Quantity', data=df )


# In[43]:


plt.figure(figsize=(20,7))
sns.barplot(x=df['City'],y=df['gross income'],palette='Set1')
plt.xlabel('City name',fontsize='16')
plt.ylabel('Gross income',fontsize='16')


# In[44]:


plt.figure(dpi=125)
sns.countplot(y ='Product line', hue = "City", data = df) 
plt.xlabel('Count')
plt.show()


# In[ ]:




