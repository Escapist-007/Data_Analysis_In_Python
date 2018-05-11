
# coding: utf-8

# ### <font color=blue>Ques 12 :</font>  <font color=red>How do I change the data type of a pandas Series ? </font> 

# #### This is useful when a column's data type is string but actually holds numbers. So, we can change the type from string to number for doing mathematical calculation. 

# In[1]:


import pandas as pd
drinks_ds = pd.read_csv('http://bit.ly/drinksbycountry')
drinks_ds.head(3)


# In[2]:


drinks_ds.dtypes    # 'object' means string


# In[3]:


drinks_ds['beer_servings'] = drinks_ds.beer_servings.astype(float)


# In[4]:


drinks_ds.dtypes 


# In[5]:


drinks = pd.read_csv('http://bit.ly/drinksbycountry',dtype={'beer_servings':float})
drinks.dtypes


# In[12]:


orders_ds = pd.read_table('http://bit.ly/chiporders')  
orders_ds.head(3)


# In[13]:


orders_ds.dtypes


# #### Datatype of the column 'item_price' is 'object'. We will cast it as float and then find mean of the column

# In[14]:


orders_ds.item_price.str.replace('$','').head()


# In[15]:


orders_ds.item_price.str.replace('$','').astype(float).mean()


# In[16]:


# converting True and False to 1 and 0 . This is important in ML
orders_ds.item_name.str.contains('Chicken').astype(int).head()

