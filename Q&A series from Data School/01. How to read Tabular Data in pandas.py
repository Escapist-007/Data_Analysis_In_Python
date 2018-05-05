
# coding: utf-8

# ### <font color=blue>Ques 01 :</font>  <font color=red>How do I read `Tabular Data` file into pandas?</font> 
# #### Tabular Data means data that looks like a table (rows & columns)

# In[1]:


import pandas as pd


# In[2]:


orders_ds = pd.read_table('http://bit.ly/chiporders')  # URL of the dataset
orders_ds.head()


#  > By default, `read_table( )` assumes that the data is `tab` seperated, and first column is 'header'. 
#  These are some default parameters of read_table( ) function.
#  Here, the Dataset is in default format of read_Table( ) function, so it is loaded perfectly.
#  
#  #### We can put the cursor in the bracket of read_table( ) function, and press <font color=red>`shift + tab` </font>to see all the parameters of this function.

# In[3]:


movie_users_ds = pd.read_table('http://bit.ly/movieusers') 
movie_users_ds.head()


# The movie dataset is not in default format. Here, seperator is ` | ` (pipe) and 1st column is not header.

# In[4]:


column_list = ['User_id', 'Age', 'Gender', 'Occupation', 'Zip-code']    # For column header
movie_users_ds = pd.read_table('http://bit.ly/movieusers', sep='|', header = None, names = column_list )

# Here, header = None, as there is no header in the dataset.
# If a header exists and we want to replace that, then header = 0 

movie_users_ds.head()

