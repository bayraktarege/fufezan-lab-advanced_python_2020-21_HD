import pytest
import sys, os
import csv
import pandas as pd
import plotly
import plotly.graph_objs as go

gpcr183 = "GPCR183.fasta"
aac = pd.read_csv("amino_acid_properties.csv")
hydrophobicity = aac.pop("hydropathy index (Kyte-Doolittle method)")
onelcode = aac.pop("1-letter code")

with open(gpcr183) as gpcr:
    whole_seq = "" 
    for line in gpcr:
        if not line.startswith(">"):
            whole_seq += line.replace("\n", "")

def listcreator(data):
    lis = list()
    for i in range(0, len(data)):
        lis.append(data[i])
        i += 1
    return lis

list_hyd = listcreator(hydrophobicity)
one_letterc = listcreator(onelcode)

def convert(lis1, lis2):
    dict = {}
    for i in range(0, len(lis1)):
        dict.update({lis1[i]: lis2[i]})
        i += 1
    return dict

mapping_dict = convert(one_letterc, list_hyd)

def matcher(seq, hyd):
    matches = list()
    for item in seq:
        matches.append(hyd.get(item))
    return matches

hyd_seq_list = matcher(whole_seq, mapping_dict)

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

# -------- START of inconvenient addon block --------
# This block is not neccessary if you instaled your package
# using e.g. pip install -e
# or have a symbolic link in your sitepackages (my preferend way)
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname("C:\\Users\\bayra\\desktop\\data science\\exercises\\tag 5"), # location of this file
            os.pardir, # and one level up, in linux ../
        )
    )
)
# --------  END of inconvenient addon block  --------

import coffeepy


def test_find_peaks():
    peaks = coffeepy.core.find_peaks([0, 2, 1])
    assert peaks == [2] 
    
def test_find_peaks_2():
    peaks = coffeepy.core.find_peaks([0, 2, 1, 0, 2, 1])
    assert peaks == [2, 2] 
    
def test_find_peaks_3():
    peaks = coffeepy.core.find_peaks([])
    assert peaks == [] 
    
    
def test_find_peaks_5():
    peaks = coffeepy.core.find_peaks([(0,0,0), (10,0,0), (0,0,6)])
    assert peaks == [(10,0,0)] 
