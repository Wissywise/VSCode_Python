import numpy as np
np_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
print(np_array)

np_array_deleted = np.delete(np_array, 0, axis=1)
print(np_array_deleted)

np_array_deleted = np.delete(np_array, 1, axis=0)
print(np_array_deleted)

np_array = np.delete(np_array, [1, 3], axis=0)
print(np_array)

np_array_insert = np.insert(np_array, 1, [[100, 200, 300]], axis=0)
print(np_array_insert)

np_array_insert_ = np.insert(np_array, 1, [[1000], [2000], [3000], [4000], [5000]], axis=1)
print(np_array_insert_)

np_array_append = np.append(np_array, [[100, 200, 300]], axis=0)
print(np_array_append)

np_array_append_ = np.append(np_array, [[1000], [2000], [3000], [4000], [5000]], axis=1)
print(np_array_append_)

