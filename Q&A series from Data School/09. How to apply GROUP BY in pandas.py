
# coding: utf-8

# ### <font color=blue>Ques 09 :</font>  <font color=red>When should I use a "GROUP BY" pandas?</font> 

# In[10]:


import pandas as pd
drinks_ds = pd.read_csv('http://bit.ly/drinksbycountry')
drinks_ds.head(4)


# In[12]:


# What is the average beer_servings across all continents? 
drinks_ds.beer_servings.mean()


# In[13]:


# What is the average beer_servings by continents? How beer_servings varied from continent to continent ?
drinks_ds.groupby('continent').beer_servings.mean()


# In[5]:


# Max beer_servings by continents
drinks_ds.groupby('continent').beer_servings.max()


# ## Specifying multiple aggregation functions at once

# In[6]:


drinks_ds.groupby('continent').beer_servings.agg(['count','max','min','mean'])


# ## Calculating mean/max/min for all numeric columns

# In[7]:


drinks_ds.groupby('continent').mean()


# In[8]:


drinks_ds.groupby('continent').agg(['count','mean','max','min'])


# # Visually showing the result

# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')

drinks_ds.groupby('continent').mean().plot(kind='bar')

