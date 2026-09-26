import numpy as np
np_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np_array)

np_condarray = np_array[np_array > 3]
print(np_condarray)
print(np_array>3)