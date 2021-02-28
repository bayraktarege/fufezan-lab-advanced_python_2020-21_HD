#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import plotly
import plotly.graph_objs as go


# In[2]:


gpcr183 = "GPCR183.fasta"
aac = pd.read_csv("amino_acid_properties.csv")
hydrophobicity = aac.pop("hydropathy index (Kyte-Doolittle method)")
onelcode = aac.pop("1-letter code")


# In[3]:


with open(gpcr183) as gpcr:
    whole_seq = "" 
    for line in gpcr:
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


# In[7]:


def slidingwindow(beginning, end):
    sliding_window = hyd_seq_list[beginning : end]
    add = 0
    for element in sliding_window:
        add += element
    data = [go.Bar(y=hyd_seq_list[beginning : end])]
    fig = go.Figure(data=data)
    fig.update_layout(template="plotly_dark", title="Sliding window:" + 
                      str(beginning) + "-" + 
                      str(end) + " " +
                     "average hydropathy" + 
                      "=" + 
                      str(add / len(sliding_window)))
    fig.update_xaxes(title_text="Amino acid position")
    fig.update_yaxes(title_text="Hydrophaty")
    fig.show()
    
slidingwindow(10, 20)
slidingwindow(30, 300)
slidingwindow(0, 360)


# In[8]:


# pip install pytest-cov


# In[9]:


import pytest as pt


# In[10]:


import sys, os


# In[11]:


os.chdir(r"C:\Users\bayra\desktop\data science\exercises\tag 5")


# In[12]:


cwd = os.getcwd()
cwd


# In[13]:


get_ipython().run_cell_magic('writefile', 'coffeepy/__init__.py ', 'from . import core')


# In[14]:


get_ipython().run_cell_magic('writefile', 'tests/test_core.py', 'import pytest\nimport sys, os\nimport csv\nimport pandas as pd\nimport plotly\nimport plotly.graph_objs as go\n\ngpcr183 = "GPCR183.fasta"\naac = pd.read_csv("amino_acid_properties.csv")\nhydrophobicity = aac.pop("hydropathy index (Kyte-Doolittle method)")\nonelcode = aac.pop("1-letter code")\n\nwith open(gpcr183) as gpcr:\n    whole_seq = "" \n    for line in gpcr:\n        if not line.startswith(">"):\n            whole_seq += line.replace("\\n", "")\n\ndef listcreator(data):\n    lis = list()\n    for i in range(0, len(data)):\n        lis.append(data[i])\n        i += 1\n    return lis\n\nlist_hyd = listcreator(hydrophobicity)\none_letterc = listcreator(onelcode)\n\ndef convert(lis1, lis2):\n    dict = {}\n    for i in range(0, len(lis1)):\n        dict.update({lis1[i]: lis2[i]})\n        i += 1\n    return dict\n\nmapping_dict = convert(one_letterc, list_hyd)\n\ndef matcher(seq, hyd):\n    matches = list()\n    for item in seq:\n        matches.append(hyd.get(item))\n    return matches\n\nhyd_seq_list = matcher(whole_seq, mapping_dict)\n\ndef slidingwindow(beginning, end):\n    sliding_window = hyd_seq_list[beginning : end]\n    add = 0\n    for element in sliding_window:\n        add += element\n    data = [go.Bar(y=hyd_seq_list[beginning : end])]\n    fig = go.Figure(data=data)\n    fig.update_layout(template="plotly_dark", title="Sliding window:" + \n                      str(beginning) + "-" + \n                      str(end) + " " +\n                     "average hydropathy" + \n                      "=" + \n                      str(add / len(sliding_window)))\n    fig.update_xaxes(title_text="Amino acid position")\n    fig.update_yaxes(title_text="Hydrophaty")\n    fig.show()\n    \nslidingwindow(10, 20)\nslidingwindow(30, 300)\nslidingwindow(0, 360)\n\n# -------- START of inconvenient addon block --------\n# This block is not neccessary if you instaled your package\n# using e.g. pip install -e\n# or have a symbolic link in your sitepackages (my preferend way)\nsys.path.append(\n    os.path.abspath(\n        os.path.join(\n            os.path.dirname("C:\\\\Users\\\\bayra\\\\desktop\\\\data science\\\\exercises\\\\tag 5"), # location of this file\n            os.pardir, # and one level up, in linux ../\n        )\n    )\n)\n# --------  END of inconvenient addon block  --------\n\nimport coffeepy\n\n\ndef test_find_peaks():\n    peaks = coffeepy.core.find_peaks([0, 2, 1])\n    assert peaks == [2] \n    \ndef test_find_peaks_2():\n    peaks = coffeepy.core.find_peaks([0, 2, 1, 0, 2, 1])\n    assert peaks == [2, 2] \n    \ndef test_find_peaks_3():\n    peaks = coffeepy.core.find_peaks([])\n    assert peaks == [] \n    \n    \ndef test_find_peaks_5():\n    peaks = coffeepy.core.find_peaks([(0,0,0), (10,0,0), (0,0,6)])\n    assert peaks == [(10,0,0)] ')


# In[15]:


get_ipython().run_cell_magic('writefile', 'coffeepy/core.py', '\ngpcr183 = "GPCR183.fasta"\naac = pd.read_csv("amino_acid_properties.csv")\nhydrophobicity = aac.pop("hydropathy index (Kyte-Doolittle method)")\nonelcode = aac.pop("1-letter code")\n\nwith open(gpcr183) as gpcr:\n    whole_seq = "" \n    for line in gpcr:\n        if not line.startswith(">"):\n            whole_seq += line.replace("\\n", "")\n\ndef listcreator(data):\n    lis = list()\n    for i in range(0, len(data)):\n        lis.append(data[i])\n        i += 1\n    return lis\n\nlist_hyd = listcreator(hydrophobicity)\none_letterc = listcreator(onelcode)\n\ndef convert(lis1, lis2):\n    dict = {}\n    for i in range(0, len(lis1)):\n        dict.update({lis1[i]: lis2[i]})\n        i += 1\n    return dict\n\nmapping_dict = convert(one_letterc, list_hyd)\n\ndef matcher(seq, hyd):\n    matches = list()\n    for item in seq:\n        matches.append(hyd.get(item))\n    return matches\n\nhyd_seq_list = matcher(whole_seq, mapping_dict)\n\ndef slidingwindow(beginning, end):\n    sliding_window = hyd_seq_list[beginning : end]\n    add = 0\n    for element in sliding_window:\n        add += element\n    data = [go.Bar(y=hyd_seq_list[beginning : end])]\n    fig = go.Figure(data=data)\n    fig.update_layout(template="plotly_dark", title="Sliding window:" + \n                      str(beginning) + "-" + \n                      str(end) + " " +\n                     "average hydropathy" + \n                      "=" + \n                      str(add / len(sliding_window)))\n    fig.update_xaxes(title_text="Amino acid position")\n    fig.update_yaxes(title_text="Hydrophaty")\n    fig.show()\n    \nslidingwindow(10, 20)\nslidingwindow(30, 300)\nslidingwindow(0, 360)\n\ndef find_peaks(list_of_intensities):\n    peaks = []\n    for pos, current_peak in enumerate(list_of_intensities[:-1]):\n        if pos == 0:\n            continue\n        if list_of_intensities[pos - 1] < current_peak > list_of_intensities[pos + 1]:\n            peaks.append(current_peak)\n    return peaks')


# In[16]:


get_ipython().system('pytest tests')


# In[17]:


get_ipython().system('pytest --cov-report html --cov=coffeepy tests/')


# In[18]:


get_ipython().system('pytest --cov-report html --cov=tests tests/')


# In[ ]:




