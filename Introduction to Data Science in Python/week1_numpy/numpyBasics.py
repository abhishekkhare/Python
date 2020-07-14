import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

print("0 dimensional array")
arr0D = np.array(42)
print(arr0D)
print(arr0D.ndim)
print('shape of array :' , arr0D.shape)


print("1 dimensional array")
arr1D = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr1D)
print('dimension of array :' , arr1D.ndim)
print('shape of array :' , arr1D.shape)
print(arr1D[0])
print(arr1D[1])
print(arr1D[2] + arr1D[3])
print(arr1D[1:4])
print(arr1D[4:])
print(arr1D[:4])
print(arr1D[-3:-1])
print(arr1D[1:5:2]) # Return every other element from index 1 to index 5:
print(arr[::2]) # Return every other element from the entire array:
print("2 dimensional array")
arr2D = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2D)
print('dimension of array :' , arr2D.ndim)
print('shape of array :' , arr2D.shape)
print('2nd element on 1st dim: ', arr2D[0, 1])
print('3rd element on 2nd dim: ', arr2D[1, 2])
print('Last element from 2nd dim: ', arr2D[1, -1])
# From the second element,
# slice elements from index 1 to index 4 (not included):
print(arr2D[1, 1:4])
print(arr2D[0:2, 2]) # From both elements, return index 2:
# From both elements,
# slice index 1 to index 4 (not included), this will return a 2-D array:
print(arr2D[0:2, 1:4])
print("3 dimensional array")
arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]] , [[13, 14, 15], [16, 17, 18]]])
print(arr3D)
print('dimension of array :' , arr3D.ndim)
print('shape of array :' , arr3D.shape)
print(arr3D[0, 1, 2])
print(arr3D[2, 1, 2])
print(arr3D[0:3, 1, 2])
print(arr3D[0:3, 1, 1:3])

print("higher dimensional array")
arr5D = np.array([1, 2, 3, 4], ndmin=5)
print(arr5D)
print('dimension of array :' , arr5D.ndim)
print('shape of array :' , arr5D.shape)
print('number of dimensions :', arr.ndim)