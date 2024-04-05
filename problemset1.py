#!/usr/bin/env python
# coding: utf-8

# In[1]:
# 
#
#
#
#
##

# Exercise 0
def github() -> str:
    """
    The following code is the URL to my github file for the problem set 1
    """
    return "https://github.com/jialis3-2133498/Econ481/blob/main/problemset1.py"
print(github())


# In[38]:


import numpy as np




# In[39]:


import pandas as pd


# In[40]:


import scipy as sp


# In[41]:


import matplotlib as mp


# In[42]:


import seaborn as sb


# In[28]:


# Exercis 2 Even-Odds
def evens_and_odds(n : int) -> dict:
    """
    This function is to add up all evens in the range of n, and all odds in the range of n
    """
    myran = range(1, n) 
    even = 0
    odd = 1
    evens = []
    odds = []
    for n in myran:
        if n % 2 == 0:
            evens.append(n) # append all even numbers into the even list
        else:
            odds.append(n) # append all odd numbers into the odd list
        even_sum = sum(evens)
        odd_sum = sum(odds)
    return {'evens': even_sum, 'odds': odd_sum}
print(evens_and_odds(4))


# In[17]:


# Exercis 3 
from typing import Union
import datetime
from datetime import datetime, date, time, timedelta 
def time_diff(date_1: str, date_2: str, k: str) -> Union[str,float]:
    """
    This function is to tell the time difference between two input dates according to 
    their types. If the third input is a float, the output will be a float. Otherwise, it will
    output a string.
    """
    date2 = datetime.strptime(date_2, "%Y-%m-%d") # This code converts a string into a date object
    dateTwo = datetime.date(date2)
    date1 = datetime.strptime(date_1, "%Y-%m-%d")
    dateOne = datetime.date(date1)
    timediff = abs(dateTwo - dateOne).days
    if k == 'string':
        
        return f"There are {timediff} days between two days"
    else:
        return float(timediff)  
   

print(time_diff('2020-01-03', '2020-01-01', 'string'))


# In[8]:


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
print(reverse(['a', 'b', 'c']))


# In[14]:


# Exercis 5
def prob_k_heads(n: int, k: int) -> float:
    """
    This function will output the probability of k successes from n trials by using Binomial 
    Distribution Equation.
    """
    ram_n = range(1, n+1)
    mynum_n = 1
    for i in ram_n:
        mynum_n = mynum_n * i # This is the factorial of N
        
    ram_k = range(1, k+1)
    mynum_k = 1
    for i in ram_k:
        mynum_k = mynum_k * i # This is the factorial of K
        
    ram_nk = range(1, n-k+1)
    mynum_nk = 1
    for i in ram_nk:
        mynum_nk = mynum_nk * i # This is the factorial of N-K



    p = 0.5
    q = (1-p)
    answer1 = mynum_n / (mynum_k * mynum_nk)
    answer2 = answer1 * (p**k) * (q**(n-k)) # This is the Binomial Distribution Equation
        

    return answer2
print(prob_k_heads(1, 1))


# In[ ]:




