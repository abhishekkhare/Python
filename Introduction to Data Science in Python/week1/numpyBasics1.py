import numpy as np

print("*********** Type **************")
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')  # Create an array with data type string
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4, 5],
               dtype='i4')  # Create an array with data type 4 bytes integer
print(arr)
print(arr.dtype)
# elements can't be casted then NumPy will raise a ValueError.
# arr = np.array(['a', '2', '3'], dtype='i')

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

print("*********** Copy and View **************")
# The copy SHOULD NOT be affected by the changes made to the original array.
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

# The view SHOULD be affected by the changes made to the original array.
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

# check if an array owns it's data or not
# The copy returns None.
# The view returns the original array.

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)

print("*********** Reshape **************")
# Reshape From 1-D to 2-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
print(newarr.base)

# Reshape From 1-D to 3-D
newarr = arr.reshape(2, 3, 2)
print(newarr)
print(newarr.base)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(3, 3) this would give
# ValueError: total size of new array must be unchanged
newarr = arr.reshape(2, 2, -1)
print(newarr)

# Flattening array means converting a multidimensional array into a 1D array.
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)