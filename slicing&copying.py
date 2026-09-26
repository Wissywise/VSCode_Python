import numpy as np

np.random.seed(0)
np_rand = np.random.rand(5, 5)
print(np_rand)

np_sub_rand = np_rand[0:3, 0]
print(np_sub_rand)

np_sub_rand[0] = 1000
print(np_sub_rand)