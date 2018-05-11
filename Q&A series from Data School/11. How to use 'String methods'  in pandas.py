
'hi'.upper()

import pandas as pd
orders_ds = pd.read_table('http://bit.ly/chiporders')  
orders_ds.head()


orders_ds.item_name.str.upper().head(3)

orders_ds.item_name.str.contains('Chicken').head()


# Showing only the item related to 'chicken'
orders_ds [ orders_ds.item_name.str.contains('Chicken') ].head()

# [python API for string]
# http://pandas.pydata.org/pandas-docs/stable/api.html#string-handling   

orders_ds.head()


# Removing Brackets from 'choice_description' column
orders_ds.choice_description.str.replace('[','').str.replace(']','').head()

orders_ds.head()

# Using Regular expression

orders_ds.choice_description.str.replace('[\[\]]','').head()
orders_ds.head()