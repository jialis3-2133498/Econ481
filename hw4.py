#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercise 0
def github() -> str:
    """
    This function will return a link to Github where this homework answer is stored
    """

    return "https://github.com/<user>/<repo>/blob/main/<filename.py>"
print(github())



# In[2]:


# Exercise 1 
import pandas as pd

def load_data() -> pd.DataFrame:
    """
    This function is to scrape a dataset from the course website 
    and load it as a dataframe in python.
    """
    tesla = pd.read_csv('https://lukashager.netlify.app/econ-481/data/TSLA.csv',index_col = 0, parse_dates = True)
    # Index_col = 0 means we directly use first column in the dataset as our index
    # parse_dates = True means we want dates aranged like YY-MM-DD
    return tesla
print(load_data())
df = pd.DataFrame(load_data())


# In[3]:


# Exercise 2
import matplotlib.pyplot as plt
def plot_close(df: pd.DataFrame, start: str, end: str) -> None:
    """
    This function will take the dataframe from Exercise 1 and also the optional 
    start and end datetime, and then plot the Tesla's closing stock price 
    withing the datetime. 
    """
    df.loc[start:end]
    # set up the range of dataframe being selected from the start to end datetime

    plt.figure()
    # set up the plot
    
    plt.plot(df.index, df['Close'], color='red', linestyle = '-', ms = 0.5,
                    linewidth = 1.5)
    # the range of X-axis will be the index of the dataframe that we selected according to the start and end date
    # the y-axis will be the closing price from the dataframe.
    # The line will be red, with linewidth 1.5.
    
    plt.title(f"Closing Price of Tesla Stock ({start} to {end})")
    # Set up the plot's title
    plt.xlabel('Date')
    # Set up the plot's X-axis lable
    plt.ylabel('Tesla Stock Closing Price')
    # Set up the plot's Y-axis lable
    plt.show()

print(plot_close(df, '2010-06-29', '2024-04-15')) 
    
    


# In[4]:


# Exercise 3
import pandas as pd
import statsmodels.api as sm
import numpy as np

df['lag_close'] = df['Close'].shift(1, freq = 'D')
# This code will generate a lag closing price so that we can subtract with the closing price
# freq = 'D' means we only consider about the stock price difference within consecutive Days.
# For non consecutive days, we will just put a NA and we will drop those NA when we do regression

df['delta'] = df['Close'] - df['lag_close']
# We can get the stock price difference by subtracting the Close price with Lagged Close price

df['lagged_delta'] = df['delta'].shift(1)
# In order to do the Autoregression Model 1, we also need lagged delta

def autoregress(df: pd.DataFrame) -> float:
    """
    This function will take the dataframe from Exercise 1 
    and compute the t-statistics of the lagged-delta from the 
    Autoregression Model 1.
    """
    X = df['lagged_delta'].dropna()
    # Independent variable will be lagged_delta
    
    y = df['delta']
    # Dependent variable will be delta
  
    y = y.loc[X.index]
    # We want our variable y and variable X have same length index after we drop NA
    

    est = sm.OLS(y, X, missing = 'drop')
    # We will use the sm.OLS to run the Autoregression Model
    model = est.fit(cov_type = 'HC1', use_t = True)
    
    #model = sm.OLS(y, X).fit(cov_type='HC1')
    return model.tvalues['lagged_delta']
print(autoregress(df))





# In[11]:


# Exercise 4
import statsmodels.formula.api as smf
def autoregress_logit(df: pd.DataFrame) -> float:
    """
    Some docstrings.
    """
    df.dropna(inplace=True)
    X = df['lagged_delta']
    #y = df['delta']
    #X = X.replace([np.inf, -np.inf], np.nan).dropna()
    #y = y.loc[X.index]
    y = (df['delta'] > 0).astype(int)
    
    model = smf.logit('y~ 0+ X', data = df).fit()
    model.tvalues['X']

    return model.tvalues
print(autoregress_logit(df))


# In[7]:


# Exercise 5
def plot_delta(df: pd.DataFrame) -> None:
    """
    Some docstrings.
    """
    #plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['delta'],  linestyle='-')
    plt.title('Tesla Stock Price Differences')
    plt.xlabel('Date')
    plt.ylabel('Price Difference')
    #plt.grid(True)
    plt.show()
print(plot_delta(df))


# In[ ]:




