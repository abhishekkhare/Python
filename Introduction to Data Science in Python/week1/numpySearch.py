import numpy as np
import sys

print("*********** Search Arrays **************")
# Find the indexes where the value is 4
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

# Find the indexes where the values are even
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

# Find the indexes where the value 7 should be inserted
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6, 8, 9])
print(x)

print("*********** Sort Arrays **************")

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

print("2 dimensional array")
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

print("3 dimensional array")
arr = np.array([[[3, 2, 1], [4, 6, 5]], [[8, 7, 9], [12, 10, 11]] , [[13, 12, 13], [1, 1, -1]]])
print(np.sort(arr))

print("*********** Filter Arrays **************")
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

# Create a filter array that will return only values higher than 42
arr = np.array([41, 42, 43, 44])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# Option 2
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# Create a filter array that will return only even elements from the original array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# Option 2
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

sys.exit()