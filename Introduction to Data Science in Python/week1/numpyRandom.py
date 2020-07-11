from numpy import random
import numpy as np
import sys
for y in range(0, 5):
  print("int = ",random.randint(100), "float = ", random.rand())

# 1 D Array
print(random.randint(100, size=(5)))

# 2 D Array
print(random.randint(100, size=(3, 5)))

# The choice() method allows you to generate a random value based on an array of values.

print("choice --> ", random.choice([3, 5, 7, 9]))
print("choice, size --> ", random.choice([3, 5, 7, 9], size=(3, 5)))

# The sum of all probability numbers should be 1.
print("choice, size, probability 1D--> ", random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100)))
print("choice, size, probability 2D--> ", random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5)))

print("********* Shuffling Arrays *********")
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

print("2 dimensional array")
arr = np.array([[3, 2, 4], [5, 0, 1]])
random.shuffle(arr)
print(arr)

print("3 dimensional array")
arr = np.array([[[3, 2, 1], [4, 6, 5]], [[8, 7, 9], [12, 10, 11]] , [[13, 12, 13], [1, 1, -1]]])
random.shuffle(arr)
print(arr)

print("********* Permutation of Arrays *********")
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))

sys.exit()