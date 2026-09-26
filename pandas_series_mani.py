import pandas as pd
import numpy as np
# Create a pandas Series

dict_data = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4, 'elderberry': 5, 'fig': 6, 'grape': 7, 'honeydew': 8, 'kiwi': 9, 'lemon': 10}
series_from_dict = pd.Series(dict_data, name ='Fruit Count')
print(series_from_dict)

## indexing and slicing
print(series_from_dict[1:2])  # Accessing value by index
print(series_from_dict['apple'])  # Accessing value by key
print(series_from_dict[1:4])  # Slicing the Series


## Mutable operations on Series
series_from_dict['banana'] = 20  # Modifying value by key
print(series_from_dict)

## More than one indexing and slicing
print(series_from_dict[['apple', 'cherry', 'fig']])  # Accessing

print(series_from_dict[series_from_dict > 5])  # Filtering values greater than 5
print(series_from_dict[series_from_dict % 2 == 0])  # Filtering even values
print(series_from_dict[series_from_dict % 2 != 0])  # Filtering odd values
print(series_from_dict[series_from_dict.isin([2, 4, 6])])  # Filtering values present in a list
print(series_from_dict[series_from_dict.between(3, 7)])  # Filtering values between 3 and 7
print(series_from_dict[series_from_dict.notnull()])  # Filtering non-null values
print(series_from_dict[series_from_dict.isnull()])  # Filtering null values
#print(series_from_dict[[0, 2, 4]])  # Accessing values by index positions


## drop and delete operations on Series
series_dropped = series_from_dict.drop('banana')  # Dropping a value by key
print(series_dropped)
print(series_from_dict.drop(['apple', 'cherry']))  # Dropping multiple values by keys