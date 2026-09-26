import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

print(my_array)
print(type(my_array))
print(my_array.shape)
print(my_array.ndim)
print(my_array.size)
print(my_array.dtype)


np_zeros = np.zeros((5, 5), dtype=int)
print(np_zeros)


np_ones = np.ones((5,5), dtype=int)
print(np_ones)

np_arr = np.arange(25).reshape((5, 5))
print(np_arr)


np_arr = np.arange(25)
np_arr_reshaped = np_arr.reshape((5, 5))
print(np_arr_reshaped)