#!/usr/bin/env python
# coding: utf-8

# # Counting Amino acid Propensity in Octopus Genome

# In[ ]:


import csv
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


Octopus_data = "uniprot-reviewed_yes+AND+organism_+Octopus.fasta"


# In[ ]:


with open(Octopus_data) as aas:
    whole_seq = "" 
    for line in aas:
        if not line.startswith(">"):
            whole_seq += line.replace("\n", "")


# In[ ]:


processed_data_dict  = {}
cnt = Counter(whole_seq)
for key, value in cnt.items():
    processed_data_dict[key] = value


# In[ ]:


output_file = open("output2.csv", "w")
writer = csv.writer(output_file)
for key, value in processed_data_dict.items():
    writer.writerow([key, value])

output_file.close()


# In[ ]:




