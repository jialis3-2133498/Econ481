#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercis 0
def github():
    """
    This function will output the link to the problem set 2 solutions in Gitbuh
    """
    return ""
github()


# In[10]:


# Exercis 1 
import numpy as np
import scipy as sp
def simulate_data(seed: int) -> tuple:
    """
    Some docstrings.
    """
    np.random.seed(seed)
    myrange = range(0, 1000)
    X = np.random.normal(0, 2, (1000, 3))
    myErr = np.random.normal(0, 1, (1000, 1))
    y = np.zeros((1000, 1))
    
    for i in myrange:
        myNum = 5 + 3*X[i, 0] + 2*X[i, 1] + 6*X[i, 2] + myErr[i]
        y[i] = myNum
    myAnswer = (y, X)
    
    return myAnswer
#simulate_data(481)





# In[15]:


# Exercis 2
import numpy as np
import scipy as sp
# Generate X1, X2, X3
np.random.seed(481)
X = np.random.normal(0, 2, (1000, 3))

# Generate y
y = np.zeros((1000, 1))
myrange = range(0, 1000)
myErr = np.random.normal(0, 1, (1000, 1))
    
for i in myrange:
    myNum = 5 + 3*X[i, 0] + 2*X[i, 1] + 6*X[i, 2] + myErr[i]
    y[i] = myNum

def neg_log_likelihood(betas:np.array) -> int:
    """
    Some docstrings.
    """
    beta0, beta1, beta2, beta3 = betas
    ranran = range(0, 1000)
    
    residuals = np.zeros((1000, 1))
    yPredicted = np.zeros((1000, 1))
    for i in ranran:
        yPredicted[i] = beta0 + beta1* X[i, 0] + beta2* X[i, 1] + beta3*X[i, 2]
        residuals[i] = y[i] - yPredicted[i]
    likelihood_fun = -np.sum(residuals**2/2) - 500*np.log(2*np.pi*1)
    return -likelihood_fun

result = sp.optimize.minimize(neg_log_likelihood, [1, 1, 1, 1], method = 'Nelder-Mead')
result.x
def estimate_mle(y: np.array, X: np.array) -> np.array:
    """
    Some docstrings.
    """
    eB = np.array(result.x)
    return  eB.reshape(-1, 1)
estimate_mle(y, X)


# In[14]:


# Exercis 3
import numpy as np
import scipy as sp
# Generate X
np.random.seed(481)
X = np.random.normal(0, 2, (1000, 3))
myErr = np.random.normal(0, 1, 1000)


#Generate y
myrange = range(0, 1000)
for i in myrange:
    myNum = 5 + 3*X[i, 0] + 2*X[i, 1] + 6*X[i, 2] + myErr[i]
    y[i] = myNum


def neg_residuals(betas: np.array, X: np.array, y:np.array):
    beta0, beta1, beta2, beta3 = betas
    e = np.zeros((1000, 1))
    py = np.zeros((1000, 1))
    for i in range(1000):
        py[i] = beta0 + beta1 * X[i, 0] + beta2 * X[i, 1] + beta3*X[i, 2]
        e[i] = y[i] - py[i]
    ef = np.sum(e**2)
    return ef
initialGuess = [1, 1, 1, 1]
est_coeff = sp.optimize.minimize(neg_residuals, initialGuess, args = (X, y), method = 'Nelder-Mead')
est_coeff.x

def estimate_ols(y: np.array, X: np.array) -> np.array:
     """
     Some docstrings.
     """
     eOLS = np.array(est_coeff.x)

     return eOLS.reshape(-1, 1)
estimate_ols(y, X)


# In[ ]:




