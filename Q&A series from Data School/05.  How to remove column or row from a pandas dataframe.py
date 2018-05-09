
# coding: utf-8

# ### <font color=blue> Ques 05: </font>  <font color=red>  How do I `remove columns / rows` from a pandas dataframe? </font>

# In[1]:


import pandas as pd
ufo_ds = pd.read_csv('http://bit.ly/uforeports')
ufo_ds.head()


# In[2]:


ufo_ds.shape


# In[3]:


ufo_ds.columns


# In[4]:


# We will drop the column : "Colors Reported"
# axis = 0 means row 
# axis = 1 means column

ufo_ds.drop('Colors Reported', axis=1, inplace=True)


# In[5]:


ufo_ds.columns


# In[6]:


ufo_ds.head(3)


# In[7]:


# Drop multiple columns
ufo_ds.drop(['City','Time'], axis=1, inplace=True)


# In[8]:


ufo_ds.head(3)


# > #### Removing rows :

# In[9]:



ufo_ds.drop([0, 1] , axis = 0, inplace = True)   # Index no of the rows

ufo_ds.head()

