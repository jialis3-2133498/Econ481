#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Exercise 0
def github() -> str:
    """
    The following code is the URL to my github file for the problem set 1
    """
    return "https://github.com/jialis3-2133498/Econ481_ProblemSet1.git"


# In[3]:


import numpy as np


# In[4]:


import pandas as pd


# In[5]:


import scipy as sp


# In[6]:


import matplotlib as mp


# In[7]:


import seaborn as sb


# In[50]:


# Exercis 1 Even-Odds
def evens_and_odds(n : int) -> dict:
    """
    This function is to add up all evens in the range of n, and all odds in the range of n
    """
    myran = range(n)
    even = 0
    odd = 1
    evens = []
    odds = []
    for n in myran:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)
        even_sum = sum(evens)
        odd_sum = sum(odds)
    return {'evens': even_sum, 'odds': odd_sum}
#answer = {'evens:' + even, 'odds:' + odd}
evens_and_odds(8)


# In[31]:


# Exercis 3 
from typing import Union
import datetime
from datetime import datetime, date, time, timedelta 
def time_diff(date_1: str, date_2: str, k: str) -> Union[str,float]:
    """
    This function is to tell the time difference between two input dates according to 
    their types. If the third input is a float, the output will be an integer. Otherwise, it will
    output a string.
    """
    date2 = datetime.strptime(date_2, "%Y-%m-%d")
    dateTwo = datetime.date(date2)
    date1 = datetime.strptime(date_1, "%Y-%m-%d")
    dateOne = datetime.date(date1)
    timediff = abs(dateTwo - dateOne).days
    if k == 'string':
        
        return f"There are {timediff} days between two days"
    else:
        return timediff
   
time_diff('2022-09-01', '2022-09-08', 'float')
time_diff('2022-09-01', '2022-09-08', 'string')


# In[50]:


# Exercis 4 
def reverse(in_list: list) -> list:
    """
    This function will reverse the order of elements and output a new list with reversed order.
    """
    n = len(in_list)
    i = range(n-1, -1, -1) # if n is 3, then i will be 2, 1, 0, -1 will be excluded automatically. 
    re_list = []
    for k in i:
            re_list.append(in_list[k])
        

    return re_list
reverse(['a', 'b', 'c'])


# In[26]:


# Exercis 5
def prob_k_heads(n: int, k: int) -> float:
    """
    This function will output the probability of k from n
    """
    ram_n = range(1, n+1)
    mynum_n = 1
    for i in ram_n:
        mynum_n = mynum_n * i
        
    ram_k = range(1, k+1)
    mynum_k = 1
    for i in ram_k:
        mynum_k = mynum_k * i
        
    ram_nk = range(1, n-k+1)
    mynum_nk = 1
    for i in ram_nk:
        mynum_nk = mynum_nk * i



    p = 0.5
    q = 0.5
    answer1 = mynum_n / (mynum_k * mynum_nk)
    answer2 = answer1 * (p**k) * (q**(n-k))
        

    return answer2
prob_k_heads(1, 1)

#Q2, when I use i for all loops, I will get the right answer, but if I use I, j, k in the loop, I will get the wrong answer. 







