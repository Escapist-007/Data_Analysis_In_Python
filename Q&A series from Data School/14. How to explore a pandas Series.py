import pandas as pd
movie_ratings_ds = pd.read_csv('http://bit.ly/imdbratings')
movie_ratings_ds.head(4)

movie_ratings_ds.genre.describe()


# showing the count for every distinct value of the 'genre' column
movie_ratings_ds.genre.value_counts()


# showing percentage
movie_ratings_ds.genre.value_counts(normalize=True)


movie_ratings_ds.genre.unique()  # Show all unique values

movie_ratings_ds.genre.nunique()  # Show the count of unique value


# Show the the details content_rating for each genre type
pd.crosstab(movie_ratings_ds.genre, movie_ratings_ds.content_rating)

movie_ratings_ds.duration.describe()

movie_ratings_ds.duration.plot(kind='hist')  # A histogram shows the distribution of a numerical variable

# Not feasibale if there is so many distinct value for a column
movie_ratings_ds.duration.value_counts().plot(kind='bar')  
movie_ratings_ds.genre.value_counts().plot(kind='bar')