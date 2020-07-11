import numpy as np

print("*********** Iterating Arrays **************")
print("1 dimensional array")
arr = np.array([1, 2, 3])
for x in arr:
  print("-->",x)

for x in np.nditer(arr):
  print('==>',x)

for idx, x in np.ndenumerate(arr):
  print('## ',idx, x)

print("2 dimensional array")
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print("-->",x)

for x in arr:
  for y in x:
    print("-->",y)

for x in np.nditer(arr):
  print('==>',x)

for idx, x in np.ndenumerate(arr):
  print('## ',idx, x)
print("3 dimensional array")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print("-->",x)

for x in arr:
  for y in x:
    for z in y:
      print("-->",z)

for x in np.nditer(arr):
  print('==>',x)

for idx, x in np.ndenumerate(arr):
  print('## ',idx, x)