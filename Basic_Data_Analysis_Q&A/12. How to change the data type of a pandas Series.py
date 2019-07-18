import pandas as pd
drinks_ds = pd.read_csv('http://bit.ly/drinksbycountry')
drinks_ds.head(3)

drinks_ds.dtypes    # 'object' means string

drinks_ds['beer_servings'] = drinks_ds.beer_servings.astype(float)

drinks_ds.dtypes 


drinks = pd.read_csv('http://bit.ly/drinksbycountry',dtype={'beer_servings':float})
drinks.dtypes


orders_ds = pd.read_table('http://bit.ly/chiporders')  
orders_ds.head(3)


orders_ds.dtypes


# Datatype of the column 'item_price' is 'object'. We will cast it as float and then find mean of the column


orders_ds.item_price.str.replace('$','').head()

orders_ds.item_price.str.replace('$','').astype(float).mean()

# converting True and False to 1 and 0 . This is important in ML
orders_ds.item_name.str.contains('Chicken').astype(int).head()

