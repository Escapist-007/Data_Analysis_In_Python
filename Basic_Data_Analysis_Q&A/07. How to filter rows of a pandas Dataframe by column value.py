
# IMDB - Internet Movie Database (Dataset)

import pandas as pd
movie_ratings_ds = pd.read_csv('http://bit.ly/imdbratings')
movie_ratings_ds.head(4)


movie_ratings_ds.shape

movie_ratings_ds.head()


# We want to find the records having duration >= 200.

#  --  Long Process --

# Creating a python list containing boolean value for each row
booleans = []
for length in movie_ratings_ds.duration:
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)
        
booleans[0:6]   # check first 5 values

len(booleans)


# convert the boolean list into pandas series

is_long = pd.Series(booleans)
is_long.head()

# Pass the Series to dataframe. It will show only the rows having True value in the Series
movie_ratings_ds[is_long]  


# --  Short Process --


is_long = movie_ratings_ds.duration >= 200
movie_ratings_ds[is_long].head()


# We can wrap it one line
movie_ratings_ds[ movie_ratings_ds.duration >= 200 ].head()


# Showing only one column based on filter

movie_ratings_ds[ movie_ratings_ds.duration >= 200 ].title.head()

# It has some limitation. So, there is a better approach for this same task -- using "loc" method
movie_ratings_ds.loc[ movie_ratings_ds.duration >= 200, 'genre']

