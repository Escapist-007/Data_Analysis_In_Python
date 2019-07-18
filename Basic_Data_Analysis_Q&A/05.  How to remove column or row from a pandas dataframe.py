import pandas as pd

ufo_ds = pd.read_csv('http://bit.ly/uforeports')
ufo_ds.head()

ufo_ds.shape
ufo_ds.columns


# We will drop the column : "Colors Reported"
# axis = 0 means row 
# axis = 1 means column

ufo_ds.drop('Colors Reported', axis=1, inplace=True)
ufo_ds.columns
ufo_ds.head(3)

# Drop multiple columns
ufo_ds.drop(['City','Time'], axis=1, inplace=True)

ufo_ds.head(3)

# Removing rows :
ufo_ds.drop([0, 1] , axis = 0, inplace = True)   # Index no of the rows
ufo_ds.head()
