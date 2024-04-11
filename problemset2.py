#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercis 0
def github():
    """
    This function will output the link to the problem set 2 solutions in Gitbuh
    """
    return "https://github.com/jialis3-2133498/Econ481/blob/main/problemset2.py"
print(github())


# In[8]:


# Exercis 1 
import numpy as np
import scipy as sp
def simulate_data(seed: int) -> tuple:
    """
    This function will take an integer in and compute random x1, x2, x3, and error terms. For the independent variables, 
    they follow 0 mean and sqrt(2) standard deviation. For the error term, it follows 0 mean and 1 standard deviation. 
    This function will use the given regression model to compute all y according to different x and error terms.
    """
    np.random.seed(seed)
    x1 = np.random.normal(0, np.sqrt(2), (1000, 1))
    x2 = np.random.normal(0, np.sqrt(2), (1000, 1))
    x3 = np.random.normal(0, np.sqrt(2), (1000, 1)) # Those three codes will generate x1, x2, x3 with 0 mean and sqrt(2) std. 
    X = np.column_stack((x1, x2, x3)) # Combine x1, x2, and x3 into an array horizontally. 
    myErr = np.random.standard_normal((1000, 1))
    y = np.zeros((1000, 1)) # create an array for y
    y = 5 + 3*x1 + 2*x2 + 6*x3 + myErr # update y values 

    myAnswer = (y, X)
    
    return myAnswer


print(simulate_data(481))
y = simulate_data(481)[0] # We call y out so that we can use it in the Exercise 2 and 3
X = simulate_data(481)[1] # we call X out so that we can use it in Exercise 2 and 3






# In[9]:


# Exercis 2
import numpy as np
import scipy as sp

def negative_log_likelihood(startingGuess1:np.array, X: np.array, y:np.array) -> int:
    """
    This function will take the starting guess of betas, X, and y in. And compute the negative likelihood 
    function so that we can later use scipy.optimize.minimize function to do the MLE operation. 
    """
    beta0, beta1, beta2, beta3 = startingGuess1 # In the scipy.min(), it will take my initial guess of betas and X, y together
                                                # and pass them into my neg_log_likelihood() to iterate untill it finds 
                                                # the best betas that maximize the likelihood. 
    ranran = range(0, 1000)
    
    residuals = np.zeros((1000, 1))
    yPredicted = np.zeros((1000, 1))
    n = 1000 # sample size
    for i in ranran:
        yPredicted[i] = beta0 + beta1* X[i, 0] + beta2* X[i, 1] + beta3*X[i, 2] # compuete the predicted y
        residuals[i] = y[i] - yPredicted[i] # Compute the residual
    likelihood_function = -np.sum(residuals**2/2) - (n/2)*np.log(2*np.pi*1) # Likelihood formula for x
    return -likelihood_function # becasue we are using scipy.minimize function, we can minimize a negative number, which is equivalant
                            # to maximize a number. 
startingGuess1 = [100, 99, 17, 10] # It is the inital guess of betas 

result = sp.optimize.minimize(negative_log_likelihood, startingGuess1, args = (X, y), method = 'Nelder-Mead') # We will use this function
                                                                                                        # to maximize the likelihood
result.x # extract the best coefficients from the result

def estimate_mle(y: np.array, X: np.array) -> np.array:
    """
    This function will return the best estimaes of betas after using the MLE method.
    """
    eB = np.array(result.x)
    return  eB.reshape(-1, 1)
print(estimate_mle(y, X))


# In[4]:


# Exercis 3
import numpy as np
import scipy as sp

def residuals(originalGuess: np.array, X: np.array, y:np.array):
    """
    This function will take the initialGuess of betas, X, and y in. And then compute the residual sum of squares. 
    """
    beta0, beta1, beta2, beta3 = originalGuess
    e = np.zeros((1000, 1))
    py = np.zeros((1000, 1))
    for i in range(1000):
        py[i] = beta0 + beta1 * X[i, 0] + beta2 * X[i, 1] + beta3*X[i, 2] # Compute the predicted y
        e[i] = y[i] - py[i]
    errf = np.sum(e**2)
    return errf
originalGuess = [1, 1, 1, 1]
est_coeff = sp.optimize.minimize(residuals, originalGuess, args = (X, y), method = 'Nelder-Mead') # The command will minimize
                                                                                                    # the Residual Sum of Squares 
                                                                                                    # so that it can get the best betas
est_coeff.x

def estimate_ols(y: np.array, X: np.array) -> np.array:
     """
     This function will return best estimates of betas after using OLS method.
     """
     eOLS = np.array(est_coeff.x)

     return eOLS.reshape(-1, 1)
print(estimate_ols(y, X))


# In[ ]:




