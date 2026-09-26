import numpy as np

my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

print(my_array)

my_array_reshaped = np.reshape(my_array, (4, 5), order='F')
print(my_array_reshaped)