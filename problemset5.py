#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Exercise 0
def github() -> str:
    """
    This function will return a link to Github where this 
    python file is stored and updated.
    """

    return "https://github.com/jialis3-2133498/Econ481/blob/main/problemset5.py"
print(github())


# In[6]:


import requests
from bs4 import BeautifulSoup

def scrape_code(url: str) -> str:
    """
    This function will take an ECON481 course website URL and
    scrape all python codes appeared inside the HTML. Lastly, it
    will return a string that full of python codes.
    Python codes scraped from the URL should run without any syntax errors. 
    """
    r1 = requests.get(url)
    # This code is getting the access from the url passed in
    
    if not r1.ok:
        return "Sorry, unable to request access this website"
    # If we failed to get the access, it will return a note
        
    r1_bs = BeautifulSoup(r1.text, "html.parser")
    # We use BeautifulSoup library to retreat the raw HTML commands using html.parser.
    
    codes = r1_bs.find_all('code', attrs={'class': 'sourceCode python'})
    # This code extract all the raw HTML commands under the code class named "sourceCode python".
    # Now, codes is full of <code> tag chuncks
    
    pythoncodes = '' 
    # We create an empty string that later will be used to store python codes. 
    
    for code in codes:
        # Thie for-loop examine each <code> tag found in the raw HTML commands
        
        mycode = code.get_text()
        # This code gets rid of all the tags and attributes from the <code> chunk, and only leave the text we want
        
        lines = mycode.split('\n')
        # This code split the HTML texts we got from the above into lines (by using '\n')
        
        cleaned_code = '\n'.join([line for line in lines if not line.startswith('%')])
        # First, this code will inspect all the texts and use if-not statement to exclude lines start with '%'
        # Second, new lines without '%' is stored as a list
        # Third, join each element from that list by using '\n'
        
        pythoncodes += cleaned_code + '\n'
        # Update each chunks into pythoncodes and join them by using '\n'
    
    return '"' + pythoncodes.strip() + '"'
    # Return the pythoncodes with " ". 

print(scrape_code('https://lukashager.netlify.app/econ-481/01_intro_to_python#/strings'))


# In[ ]:




