
import pandas as pd
import numpy as np

drinks_ds = pd.read_csv('http://bit.ly/drinksbycountry')
drinks_ds.head(3)


drinks_ds_int = drinks_ds.select_dtypes(include=[np.number])
drinks_ds_int.head()