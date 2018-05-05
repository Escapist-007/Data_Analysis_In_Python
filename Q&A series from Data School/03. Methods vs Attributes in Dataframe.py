
# coding: utf-8

# ### <font color=blue> Ques 03: </font>  <font color=red>  Why do some pandas commands end with parentheses, and other commands not? </font> 

# >**Method** ends with **parenthesis** but **attribute** doesn't.

# In[2]:


import pandas as pd

# IMDB - Internet Movie Database (Dataset)
movie_ratings_ds = pd.read_csv('http://bit.ly/imdbratings')
movie_ratings_ds.head(4)


# In[3]:


# Give some descriptive statistical info about the numerical columns (default) of the dataframe
movie_ratings_ds.describe()  


# In[4]:


movie_ratings_ds.shape       # Returns no. of rows, no. of columns in the Dataframe


# In[5]:


movie_ratings_ds.dtypes     # Show the datatype of all columns


# In[6]:


movie_ratings_ds.describe(include=['object']) 
# top --> Record having highest frequency , freq --> No. of frequecny of the top record

