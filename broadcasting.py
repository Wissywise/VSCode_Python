import numpy as np
np_arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np_arr2 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(np_arr1 + np_arr2)

np_arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np_arr4 = np.array([[10], [11], [12]])
print(np_arr3 + np_arr4)

np_array1 = np.array([[1, 3, 5]])
np_array2 = np.array([[3, 3, 3]])
print(np_array1 * np_array2)

np_array3 = np.array([[1, 2, 5]])
np_array4 = np_array3 * 20
print(np_array4)

np_array5 = np_array4 * 10
print(np_array5)