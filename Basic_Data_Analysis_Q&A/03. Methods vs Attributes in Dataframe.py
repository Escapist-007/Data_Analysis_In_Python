import pandas as pd

# IMDB - Internet Movie Database (Dataset)
movie_ratings_ds = pd.read_csv('http://bit.ly/imdbratings')
movie_ratings_ds.head(4)


movie_ratings_ds.describe()  # Give some descriptive statistical info about the numerical columns (default) of the dataframe
movie_ratings_ds.shape       # Returns no. of rows, no. of columns in the Dataframe
movie_ratings_ds.dtypes      # Show the datatype of all columns

movie_ratings_ds.describe(include=['object']) 
# top --> Record having highest frequency , freq --> No. of frequecny of the top record