#!/usr/bin/env python
# coding: utf-8

# # Counting Aminoacid Propensity in Human Genome

# In[ ]:


import csv
from collections import Counter


# In[ ]:


Human_data = "uniprot-filtered-organism__Homo+sapiens+(Human)+[9606]_+AND+review--.fasta"


# In[ ]:


with open(Human_data) as aas:
    whole_seq = "" 
    for line in aas:
        if not line.startswith(">"):
            whole_seq += line.replace("\n", "")
print(Counter(whole_seq))


# In[ ]:


processed_data_dict  = {}
cnt = Counter(whole_seq)
for key, value in cnt.items():
    processed_data_dict[key] = value
processed_data_dict


# In[ ]:


output_file = open("output1.csv", "w")
writer = csv.writer(output_file)
for key, value in processed_data_dict.items():
    writer.writerow([key, value])

output_file.close()


# In[ ]:




