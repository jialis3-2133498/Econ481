#!/usr/bin/env python
# coding: utf-8

# In[10]:
#111111


# Loops
# we can add new elements inside the append function in the for loop
old_list = ['x', 'y', 'z']
k = len(old_list)
for i in range(k):
    old_list.append(old_list[i] + '_is new')
print(old_list)
# isinstance function can be used to check the type of the element

# Pass condition
# Do nothing statement
x = 0
if x <0:
    print('negative')
elif x == 0:
    pass # Tell python to do nothing, just pass to the next command
else:
    print('positive')

# Break
my_sum = 0
n  = 0
for i in range(2024):
    if my_sum > 2024 - i:
        n = n + (i -1)
        break # if the condition met, use break to exit for loops
    my_sum += i
n, my_sum


# In[25]:


# Functions
def square(x: float) -> float: # it said that input should be float, and the output is also should be float
    # Docstrings, tell people what the function is doing
    """
    This function takes as inuput a scalar and outputs the scalar squared.
    """
    return x ** 2
print(square(5))

# Functions can take multiple inputs
def linear_function(x: float, m: float, b:float) -> float:
    return m*x + b
print(linear_function(x=3., m=-1., b = 9.))

#
def linear_function(x: float, m: float=-1, b:float=9) -> float: # it sets the defualt of the m and b, inputs without defult should be in front of defualted inputs
    return m*x + b
print(linear_function(x=3.))




# In[39]:


# datetime import
from datetime import datetime, date, time, timedelta
# pip install datatime, we can download the package if we do not have the access
dt = datetime(2011, 10, 29, 20, 30, 21) # 2011-10-29, 20:30:21
dt.day
dt.minute # tells you the minutes
dt.date()
print(dt.strftime("%Y-%m-%d: %H:%M")) # reshape the date time output
datetime.strptime("20091031", "%Y%m%d") # reshape the date time

# Time differences
dt2 = datetime(2011, 11, 15, 22, 30) # we did not define seconds
delta = dt2 - dt
delta # it tells the time difference
dt + delta # we can go back the the dt2



# In[40]:


# Importing
# some_module.py
PI = 3.14159
def f(x):
    return x + 2
def g(a, b):
    return a + b
import some_module
result = some_module.f(5)
pi = some_module.PI


# In[41]:


import numpy as np


# In[ ]:


https://github.com/jialis3-2133498/Econ481.git 



# In[ ]:




