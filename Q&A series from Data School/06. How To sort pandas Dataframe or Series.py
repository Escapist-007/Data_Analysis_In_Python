
# coding: utf-8

# ### <font color=blue>Ques 06 :</font>  <font color=red>How do I `sort` pandas Dataframe or Series?</font> 

# > pandas allows us to sort a Dataframe by one of its columns (known as a "Series"), and also allows us to sort a **Series** alone. 

# In[2]:


# IMDB - Internet Movie Database (Dataset)
import pandas as pd
movie_ratings_ds = pd.read_csv('http://bit.ly/imdbratings')
movie_ratings_ds.head(4)


# In[3]:


# We can sort the dataframe by any column
# This don't sort the actual data. It just shows us in sorted order
# Ascending Order

movie_ratings_ds.sort_values('duration').head()


# In[4]:


# Changing the actual order of the rows in dataframe we need to use "inplace=True"
# Descending order

# sort_values ( by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
movie_ratings_ds.sort_values('duration', ascending=False).head()


# In[5]:


# See the sorted value of a column
# Sort the series

movie_ratings_ds.title.sort_values().head()


# In[6]:


# Sort by multiple columns

movie_ratings_ds.sort_values(['star_rating', 'duration'], ascending=False).head(10)


# In[7]:


movie_ratings_ds.head()

