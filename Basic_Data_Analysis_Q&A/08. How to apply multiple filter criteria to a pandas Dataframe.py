
import pandas as pd
movie_ratings_ds = pd.read_csv('http://bit.ly/imdbratings')
movie_ratings_ds.head(4)

movie_ratings_ds[(movie_ratings_ds.duration >= 200) & (movie_ratings_ds.genre == 'Drama')]

movie_ratings_ds[(movie_ratings_ds.duration >= 200) | (movie_ratings_ds.genre == 'Drama')].head()


movie_ratings_ds[ movie_ratings_ds.genre.isin(['Drama', 'Crime', 'Adventure'])].head(10)


# How to read only some specific columns & rows from a CSV file?


ufo_ds = pd.read_csv('http://bit.ly/uforeports', usecols = [0,3], nrows = 5) 
# Picking 1st and 4th column [ City and State ]
# picking first 5 rows

ufo_ds


# How to iterate a Series and Dataframe ?

for c in ufo_ds.State:
    print(c)


for index, row in ufo_ds.iterrows():
    print(index, row.City, row.State)

