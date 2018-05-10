
# coding: utf-8

# ### <font color=blue>Ques 07:</font>  <font color=red>How do I `filter` rows of a pandas dataframe by column value ?</font>  

# In[1]:


# IMDB - Internet Movie Database (Dataset)
import pandas as pd
movie_ratings_ds = pd.read_csv('http://bit.ly/imdbratings')
movie_ratings_ds.head(4)


# In[2]:


movie_ratings_ds.shape


# In[3]:


movie_ratings_ds.head()


# ### We want to find the records having duration >= 200.

# ### <font color=red> Long Process </font>

# In[4]:


# Creating a python list containing boolean value for each row
booleans = []
for length in movie_ratings_ds.duration:
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)
        
booleans[0:6]   # check first 5 values


# In[5]:


len(booleans)


# In[6]:


# convert the boolean list into pandas series

is_long = pd.Series(booleans)
is_long.head()


# In[7]:


# Pass the Series to dataframe. It will show only the rows having True value in the Series
movie_ratings_ds[is_long]  


# ### <font color=red > Short Process </font>

# In[8]:


is_long = movie_ratings_ds.duration >= 200
movie_ratings_ds[is_long].head()


# In[9]:


# We can wrap it one line
movie_ratings_ds[ movie_ratings_ds.duration >= 200 ].head()


# In[10]:


# Showing only one column based on filter

movie_ratings_ds[ movie_ratings_ds.duration >= 200 ].title.head()

# It has some limitation. So, there is a better approach for this same task


# In[11]:


# use of "loc" method
movie_ratings_ds.loc[ movie_ratings_ds.duration >= 200, 'genre']

