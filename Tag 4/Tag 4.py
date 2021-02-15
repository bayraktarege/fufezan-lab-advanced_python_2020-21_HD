#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import plotly
import plotly.graph_objs as go


# In[2]:


mrp1 = "MRP1_HS.fasta"
aac = pd.read_csv("amino_acid_properties.csv")
hydrophobicity = aac.pop("hydropathy index (Kyte-Doolittle method)")
onelcode = aac.pop("1-letter code")


# In[3]:


with open(mrp1) as mrp:
    whole_seq = "" 
    for line in mrp:
        if not line.startswith(">"):
            whole_seq += line.replace("\n", "")


# In[4]:


def listcreator(data):
    lis = list()
    for i in range(0, len(data)):
        lis.append(data[i])
        i += 1
    return lis

list_hyd = listcreator(hydrophobicity)
one_letterc = listcreator(onelcode)


# In[5]:


def convert(lis1, lis2):
    dict = {}
    for i in range(0, len(lis1)):
        dict.update({lis1[i]: lis2[i]})
        i += 1
    return dict

mapping_dict = convert(one_letterc, list_hyd)


# In[6]:


def matcher(seq, hyd):
    matches = list()
    for item in seq:
        matches.append(hyd.get(item))
    return matches

hyd_seq_list = matcher(whole_seq, mapping_dict)


# In[10]:


def slidingwindow(beginning, end):
    sliding_window = hyd_seq_list[beginning : end]
    add = 0
    for element in sliding_window:
        add += element
    data = [go.Bar(y=hyd_seq_list[beginning : end])]
    fig = go.Figure(data=data)
    fig.update_layout(template="plotly_dark", title="MRP1:" + 
                      str(beginning) + "-" + 
                      str(end) + " " +
                     "average hydropathy" + 
                      "=" + 
                      str(add / len(sliding_window)))
    fig.update_xaxes(title_text="Amino acid position")
    fig.update_yaxes(title_text="Hydrophaty")
    fig.show()
    
slidingwindow(10, 40)
slidingwindow(100, 700)
slidingwindow(0, 360)


# In[ ]:




