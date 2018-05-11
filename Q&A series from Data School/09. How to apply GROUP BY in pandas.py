
import pandas as pd
drinks_ds = pd.read_csv('http://bit.ly/drinksbycountry')
drinks_ds.head(4)

# What is the average beer_servings across all continents? 
drinks_ds.beer_servings.mean()

# What is the average beer_servings by continents? How beer_servings varied from continent to continent ?
drinks_ds.groupby('continent').beer_servings.mean()


# Max beer_servings by continents
drinks_ds.groupby('continent').beer_servings.max()


#  Specifying multiple aggregation functions at once
drinks_ds.groupby('continent').beer_servings.agg(['count','max','min','mean'])


# Calculating mean/max/min for all numeric columns
drinks_ds.groupby('continent').mean()


drinks_ds.groupby('continent').agg(['count','mean','max','min'])


#  Visually showing the result



get_ipython().run_line_magic('matplotlib', 'inline')
drinks_ds.groupby('continent').mean().plot(kind='bar')

