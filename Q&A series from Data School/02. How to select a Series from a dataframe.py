
# coding: utf-8

# ### <font color=blue> Ques 02:</font>   <font color=red> How do I select a `Series / Column` from a `Dataframe`?</font> 

# `DataFrames` and `Series` are the two main `data structures` in pandas for data storage: 
#  > A **DataFrame** is like a table, and each column of the table is called a **Series**. 
# We will often select a Series in order to analyze or manipulate it.

# In[2]:


import pandas as pd


# In[3]:


# UFO dataset
# read_csv( ) is used for 'comma' seperated file

ufo_ds = pd.read_csv('http://bit.ly/uforeports')  # ufo = pd.read_table('http://bit.ly/uforeports', sep = ',')
ufo_ds.head()


# In[4]:


type(ufo_ds)


# In[5]:


# Selecting 'City' column (a series)
# Column name is case-sensitive

ufo_ds['City'].head() 


# In[6]:


type(ufo_ds['City'])


# In[7]:


# Each name becomes an attribute of the dataframe. 
# So, we can use dot notation which is more easy but there is a limitation. 
# The column name must not be a "keyword", and there should be "no space" in column name.

ufo_ds.City.head()


# <font color=red> `Dot notation` does not always work but `Bracket notation` always works. If we want to stick to 'Dot' notation, then we have to rename all the columns so that there is no space in the columns name and no name is a keyword (built-in method or attribute) of python.</font> 

# #### We can add two series (columns) if they are strings. 
# ### Creating a new column by combining two columns.

# In[8]:


# We can create a new series/colum 

ufo_ds['Location'] = ufo_ds.City + ' , ' + ufo_ds.State   # Need Bracket notation for the new column 

ufo_ds.head()

