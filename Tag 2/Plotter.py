#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import plotly
import plotly.graph_objs as go


# In[ ]:


human = pd.read_csv('output1.csv', header=None)
octopus = pd.read_csv('output2.csv', header=None)


# In[ ]:


def plotter(col1, col2, organism, a):
    plot = [
        go.Bar(
            x=organism[col1],
            y=organism[col2]
        )
    ]

    fig = go.Figure(data=plot)
    fig.update_xaxes(title_text="Amino acid")
    fig.update_yaxes(title_text="Quantity")
    fig.update_layout(template="plotly_dark", title=a)
    fig.show()


# In[ ]:


plotter(0, 1, human, 'Human proteome')
plotter(0, 1, octopus, 'Octopus proteome')


# In[ ]:




