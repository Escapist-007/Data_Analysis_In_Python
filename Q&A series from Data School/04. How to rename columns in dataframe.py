
# coding: utf-8

# ### <font color=blue> Ques 04: </font>  <font color=red> How do I `rename` columns in pandas dataframe? </font>

# In[2]:


import pandas as pd

# See the column names
ufo_ds = pd.read_csv('http://bit.ly/uforeports')
ufo_ds.columns


# In[3]:


ufo_ds.head(3)


# In[4]:


ufo_ds.rename(columns = {'Colors Reported':'Color_Reported', 'Shape Reported':'Shape_Reported'})
ufo_ds.columns


# In[5]:


# The column name is not changed permanently. We have to put one more argument : inplace = True.

ufo_ds.rename(columns = {'Colors Reported':'Color_Reported', 'Shape Reported':'Shape_Reported'}, inplace=True)
ufo_ds.columns


# In[6]:


ufo_ds.head(2)


# In[8]:


# Another way of renaming  [ If we want to change all the column name ]

ufo_col = ['city', 'color', 'shape', 'state', 'time']
ufo_ds.columns = ufo_col
ufo_ds.columns


# In[9]:


# Or we can rename the columns name when we load the dataset
# 0th row will be header

ufo_col = ['city', 'color', 'shape', 'state', 'time']
ufo_ds = pd.read_csv('http://bit.ly/uforeports', header=0, names = ufo_col)  # Replace 0th row (Given Header row)
ufo_ds.head(3)


# > ### If we have 100 columns having `space in their names`, and we want to replace these spaces. How we can do that ? 

# We can do that using **string methods**. Each column name is a string

# In[10]:


ufo_ds = pd.read_csv('http://bit.ly/uforeports')
ufo_ds.head(2)


# In[11]:


ufo_ds.columns = ufo_ds.columns.str.replace(' ','_')  # "ufo_ds.columns" is reassigned


# In[12]:


ufo_ds.head(3)

