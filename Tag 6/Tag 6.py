#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly
import plotly.graph_objs as go
from collections import Counter


# In[2]:


cdata = pd.read_csv("arabica_data_cleaned.csv")
cdata = cdata.drop(columns="Unnamed: 0")


# In[3]:


cdata = cdata[["Country.of.Origin", "Producer", "Processing.Method"]]
cdata.rename(columns={'Country.of.Origin':'Country of Origin',
                          "Processing.Method" : "Processing Method"}, inplace=True)


# In[4]:


def cleaner(data, col1, col2):
    i = 0
    for i in range(0, len(data)):
        if str(data[col1][i]) == 'nan':
            data = data.drop(i)
        elif str(data[col2][i]) == 'nan':
            data = data.drop(i)
        i += 1
    return data


# In[5]:


clean_data = cleaner(cdata, "Producer", "Processing Method")
clean_data = clean_data.reset_index()
clean_data = clean_data.drop(columns="index")


# In[6]:


clean_data


# In[7]:


clean_data.describe()


# In[8]:


def plotter(data, x, y):
    data = [go.Bar(
        x=data[x],
        y=data[y])]
    
    fig = go.Figure(data=data)
    fig.update_xaxes(title_text=x)
    fig.update_yaxes(title_text=y)
    fig.show()


# In[13]:


plotter(clean_data, "Processing Method", "Producer")
plotter(clean_data, "Country of Origin", "Processing Method")
plotter(clean_data, "Processing Method", "Country of Origin")


# In[10]:


def counter(data, choice, col, col2):
    mask = data[col] == choice
    data = data[mask]
    counts = Counter(data[col2])
    return counts


# In[11]:


counter(clean_data, "Mexico", "Country of Origin", "Producer")


# In[ ]:




