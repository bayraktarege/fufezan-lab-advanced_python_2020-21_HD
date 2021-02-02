#!/usr/bin/env python
# coding: utf-8

# # Counting Aminoacid Propensity in Human Genome

# In[6]:


import csv
from collections import Counter
import seaborn as sns


# In[2]:


Human_data = "uniprot-filtered-organism__Homo+sapiens+(Human)+[9606]_+AND+review--.fasta"


# In[3]:


with open(Human_data) as aas:
    whole_seq = "" 
    for line in aas:
        if not line.startswith(">"):
            whole_seq += line.replace("\n", "")
print(Counter(whole_seq))


# In[4]:


processed_data_dict  = {}
cnt = Counter(whole_seq)
for key, value in cnt.items():
    processed_data_dict[key] = value
processed_data_dict


# In[7]:


sns.displot(data=processed_data_dict)


# In[ ]:




