import numpy as np
import sys
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

print("*********** Arrange **************")
print(np.arange(0,30,2))
print("*********** LinSpace **************")
print(np.linspace(0,30,5))
print(np.linspace(0,30,6))
print(np.linspace(0,30,7))
print(np.linspace(0,30,100))

print("*********** resize **************")
arr = np.arange(0,30,2)
arr.resize(3,3)
print(arr)
print("*********** reshape **************")
arr = np.arange(0,30,2)
print(arr.reshape(3,5)) # reshape has to be exact number of items

print("*********** Others **************")
print("ones --> ",np.ones((3,2)))
print("zeros --> ",np.zeros((2,3)))
print("eye --> ", np.eye(3))
print("diag --> ", np.diag(y))
print("array multiply --> " ,np.array([1,2,3]*3))
print("array repeat --> " ,np.array([1,2,3]*3))

print("*********** Operations **************")
x = np.array([1,2,3,4])
y = np.array([9,8,7,6])
print("add --> ",x+y)
print("sub --> ",y-x)
print("mul --> ",x*y)
print("div --> ",y/x)
print("pow --> ",x**2)
print("dot --> ",x.dot(y))
print("1D-->2D --> ",np.array([x,x**2]))
print("1D-->2D Transpose --> ",np.array([x,x**2]).T)
print("*********** Math **************")
arr = np.arange(-5,10,2)
print(arr)
print("sum --> ", arr.sum())
print("max --> ", arr.max())
print("min --> ", arr.min())
print("mean --> ", arr.mean())
print("std --> ", arr.std())
print("argmax --> ", arr.argmax())
print("argmin --> ", arr.argmin())

old = np.array([[1, 1, 1],
                [1, 1, 1]])

new = old.copy()
new[:, 0] = 0

print(old)

sys.exit()
