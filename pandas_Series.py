import pandas as pd
import numpy as np
# Create a pandas Series

## From  ndarray

np_array = np.array([1, 2, 3, 4, 5])
series_from_ndarray = pd.Series(np_array)
print(series_from_ndarray)

## From List
list_data = [10, 20, 30, 40, 50]
series_from_list = pd.Series(list_data)
print(series_from_list)

## From Dictionary
dict_data = {'apple': 1, 'banana': 2, 'cherry': 3}
series_from_dict = pd.Series(dict_data, name ='Fruit Count')
print(series_from_dict)
print(series_from_dict['banana'])  # Accessing value by key

## From Scalar Value
scalar_value = 42
series_from_scalar = pd.Series(scalar_value, index=['a', 'b', 'c', 'd', 'e'])
print(series_from_scalar)



## Numpy - like operations on Series
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([10, 20, 30, 40, 50])
# Addition  
series_addition = series1 + series2
print(series_addition)

print("Series1 + 5:\n", series1 + 5)  # Adding a scalar to a Series 

print(series_from_dict + 5)  # Adding a scalar to a Series created from a dictionary    
print(series_from_dict * 2)  # Multiplying a Series by a scalar
print(series_from_dict ** 2)  # Squaring a Series
print(series_from_dict / 2)  # Dividing a Series by a scalar
print(series_from_dict.dtype)  # Checking the data type of the Series

np_arr = series_from_scalar.to_numpy()  # Converting Series to Num
print(np_arr)  # Displaying the numpy array


## dictionary-like operations on Series
print(series_from_dict.keys())  # Getting the keys of the Series
print(series_from_dict.values())  # Getting the values of the Series
print(series_from_dict.items())  # Getting the key-value pairs of the Series
print(series_from_dict.get('banana'))  # Accessing value by key using get method


## shape and size of Series
print(series_from_list.shape)  # Getting the shape of the Series
print(series_from_list.size)  # Getting the size of the Series
print(series_from_list.ndim)  # Getting the number of dimensions of the Series


## values and index of Series
print(series_from_list.values)  # Getting the values of the Series
print(series_from_list.index)  # Getting the index of the Series
print(series_from_list.name)  # Getting the name of the Series