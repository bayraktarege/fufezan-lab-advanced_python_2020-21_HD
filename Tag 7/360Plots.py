#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly
import plotly.graph_objs as go
from collections import Counter
import plotly.express as px


# In[2]:


covid_url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import json
import urllib


# In[3]:


covid_json_unformated = urllib.request.urlopen(covid_url).read().decode("utf-8")
covid_json = json.loads(covid_json_unformated)
cdf = pd.DataFrame(covid_json['records'])


# In[4]:


def renamer(rename, newname):
    cdf.rename(columns={rename : newname}, inplace=True)


# In[5]:


renamer("countriesAndTerritories", "country")
renamer("notification_rate_per_100000_population_14-days", "14d-incidence")
renamer("countryterritoryCode", "cntryCode")
renamer("geoId", "GeographicalID")
renamer("continentExp", "Continent")
renamer("dateRep", "ReportedDate")
renamer("cases_weekly", "WeeklyCases")
renamer("deaths_weekly", "WeeklyDeaths")


# In[6]:


def splitter(data, column, mark, newcol1, newcol2):
    split = data[column].str.split(mark, expand=True)
    split.columns = [newcol1, newcol2]
    data = data.join(split)
    data = data.drop(columns=column)
    return data


# In[7]:


newcdf = splitter(cdf, "year_week", "-", "year", "week")


# In[8]:


def sorter(data, column):
    data = data.sort_values([column])
    return data

reporteddate = sorter(newcdf, "ReportedDate")
reporteddate['ReportedDate'] = pd.to_datetime(reporteddate['ReportedDate'])
reporteddate["ReportedDate"].dt.day
reporteddate.insert(0,column="deltaTime_since_start_of_recording", value=reporteddate["ReportedDate"].dt.day)
reporteddate = reporteddate.reset_index(drop=True)


# In[10]:


def extractor(data, column, country):
    i = 0
    for i in range(len(data)):
        count = data.loc[i][column]
        if  count == country:
            continue
        else: data = data.drop(i)
    i += 1
    data = data.sort_values(["deltaTime_since_start_of_recording"])
    data = data.reset_index(drop=True)
    return data

msk_de = extractor(reporteddate, "country", "Germany")
msk_swe = extractor(reporteddate, "country", "Sweden")
msk_gr = extractor(reporteddate, "country", "Greece")


# In[11]:


def diagramme(data, ülke):
    grp_country = data[['WeeklyDeaths', 'popData2019', 'ReportedDate','country', 'year']].groupby(['country', 'year'])
    data_radial_plot = []
    for (country, year), df in grp_country:
        day_in_year = df['ReportedDate'] - pd.to_datetime(year, format='%Y')
    
        data_radial_plot.append(
                go.Scatterpolar(
                    r=(df['WeeklyDeaths']*100000)/df['popData2019'],
                    theta=day_in_year.dt.days * 360/365,
                    hovertext=f'{country} {year}',
                    name=f'{country} {year}',
#                 fill='toself'
        )
        )
    
    layout = {
        'title': {
            'text':'Weekly death rate of Covid-19 for' + ' ' + ülke
        },
        'polar': {
        },
        'radialaxis': {
        }
        }
    fig = go.Figure(data=data_radial_plot, layout=layout)
    fig.show()
    
diagramme(msk_gr, "Greece")
diagramme(msk_de, "Germany")
diagramme(msk_swe, "Sweden")
#diagramme(clean_msk_ita, "Italy")


# In[ ]:




