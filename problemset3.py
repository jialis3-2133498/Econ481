#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercise 0 
def github() -> str:
    """
    Store the Assignment into the github.
    """

    return "https://github.com/<user>/<repo>/blob/main/<filename.py>"

# Exercise 1
import pandas as pd
y2022 = pd.read_excel('https://lukashager.netlify.app/econ-481/data/ghgp_data_2022.xlsx')
def import_yearly_data(years : list) -> pd.DataFrame:
    """
    import the year list and output the desired data. 
    """
    n = range(len(years))
    myAnswer = pd.DataFrame()
    for i in n:
        if years[i] == 2022:
            data = pd.read_excel('https://lukashager.netlify.app/econ-481/data/ghgp_data_2022.xlsx', sheet_name='Direct Emitters', skiprows = 3)
        elif years[i] == 2021:
            data = pd.read_excel('https://lukashager.netlify.app/econ-481/data/ghgp_data_2021.xlsx', sheet_name='Direct Emitters', skiprows = 3)
        elif years[i] == 2020:
            data = pd.read_excel('https://lukashager.netlify.app/econ-481/data/ghgp_data_2020.xlsx', sheet_name='Direct Emitters', skiprows = 3)
        else:
            data = pd.read_excel('https://lukashager.netlify.app/econ-481/data/ghgp_data_2019.xlsx', sheet_name='Direct Emitters', skiprows = 3)
        data['year'] = years[i]
        myAnswer = pd.concat([myAnswer, data], ignore_index=True)
    return myAnswer
emissions_data = import_yearly_data([2019, 2020, 2021, 2022])
print(emissions_data)


# In[2]:


#!pip install pyxlsb
# Exercise 2
import pandas as pd
from pyxlsb import open_workbook as open_xlsb

def import_parent_companies(years: list) -> pd.DataFrame:
   """
   take the list of years and output the data being called
   """
   
   sheet_names = {
       2022: '2022',
       2021: '2021',
       2020: '2020',
       2019: '2019',
       2018: '2018',
       2017: '2017',
       2016: '2016',
       2015: '2015',
       2014: '2014',
       2013: '2013',
       2012: '2012',
       2011: '2011',
       2010: '2010'
   }
   ppcc = pd.DataFrame()  # Initialize an empty DataFrame
   
   for year in years: 
      if year in sheet_names:
          sheet_name = sheet_names[year]
          ddtt = pd.read_excel('https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb', 
                               sheet_name = sheet_name , engine='pyxlsb').dropna(how = 'all')
          ppcc = pd.concat([ppcc, ddtt], ignore_index=True)
          ppcc['year'] = year
   
   return ppcc
parent_data = import_parent_companies([2019, 2020, 2021, 2022])
print(parent_data)



# In[6]:


# Exercis 3
def n_null(df: pd.DataFrame, col = str) -> int:
    """
    calculate the null in different columns
    """

    value1 = df[col].isna().sum()
    return value1
print(n_null(emissions_data, 'Facility Id'))
print(n_null(emissions_data, 'FRS Id'))

print(n_null(parent_data, 'FRS ID (FACILITY)'))
print(n_null(parent_data, 'GHGRP FACILITY ID'))
# It is better to use Facility Id because it has 0 Null or Na. For FRS Id, it has 518 Nulls or Nas


# In[7]:


# Exercise 4
import pandas as pd

def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    clean the data and concate the new dataframe
    """
    parent_data.rename(columns = {'GHGRP FACILITY ID': 'Facility Id'})
    ljd = pd.merge(emissions_data, parent_data, on=['year', 'Facility Id'], how = 'left')
    
    cleaned_data = ljd[['Facility Id', 'year', 'State', 'Industry Type (sectors)',
                                 'Total reported direct emissions', 'PARENT CO. STATE', 
                                 'PARENT CO. PERCENT OWNERSHIP']]
    cleaned_data.columns = cleaned_data.columns.str.lower()
    return cleaned_data

# Test
df4 = clean_data(emissions_data, parent_data)
print(df4)

#print(clean_data(import_yearly_data([2019]), import_parent_companies([2019])))


# In[72]:


# Excercise
def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    Take the two dataframes and output the statistics
    """
    vAgg = ['total reported direct emissions', 'parent co. percent ownership']
    myRes = df4.groupby(group_vars, as_index=True)[vAgg].agg(['min', 'median', 'mean', 'max'])
    myRes = myRes.sort_values(by=('total reported direct emissions', 'mean'),
                                ascending=False)
    

    return  myRes

print(aggregate_emissions(df4, ['state']))


# In[ ]:


# Exercise 4
import pandas as pd

def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    This function is to clean the concatenated emissions and parent companies data.

    Parameters:
    emissions_data: Concatenated DataFrame of emissions data.
    parent_data: Concatenated DataFrame of parent companies data.

    Returns:
    pd.DataFrame: Cleaned Left Joined DataFrame.
    """
    parent_data.rename(columns = {'GHGRP FACILITY ID': 'Facility Id'}, inplace = True)
    left_joined_data = pd.merge(emissions_data, parent_data, on=['year', 'Facility Id'], how = 'left')
    
    cleaned_data = left_joined_data[['Facility Id', 'year', 'State', 'Industry Type (sectors)',
                                 'Total reported direct emissions', 'PARENT CO. STATE', 
                                 'PARENT CO. PERCENT OWNERSHIP']]
    cleaned_data.columns = cleaned_data.columns.str.lower()
    return cleaned_data

# Test
df4 = clean_data(df1, df2)
print(df4)

#print(clean_data(import_yearly_data([2019]), import_parent_companies([2019])))

