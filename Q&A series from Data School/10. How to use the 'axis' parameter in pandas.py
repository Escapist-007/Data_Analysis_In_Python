
# coding: utf-8

# ### <font color=blue>Ques 10 :</font>  <font color=red>How to use the "axis" parameter in pandas? </font> 

# In[4]:


import pandas as pd
drinks_ds = pd.read_csv('http://bit.ly/drinksbycountry')
drinks_ds.head(4)


# In[5]:


# Dropping the 'continent' column
drinks_ds.drop('continent', axis=1, inplace=True)
drinks_ds.head(2)


# In[6]:


drinks_ds.drop(1, axis=0,inplace=True)  # Dropping 2nd row
drinks_ds.head(3)


# In[7]:


# We can use aggregation along row-wise (default) or column-wise.
# axis = 0 / axis = 'index' means row-wise
# axis = 1 / axis = 'columns' means column-wise
drinks_ds.mean(axis=0)


# In[8]:


drinks_ds.mean(axis='index')


# In[9]:


drinks_ds.shape


# In[10]:


print(drinks_ds.mean(axis=0).shape)
print(drinks_ds.mean(axis=1).shape)


# In[12]:


drinks_ds.head()


# In[11]:


drinks_ds.mean(axis=1).head()

