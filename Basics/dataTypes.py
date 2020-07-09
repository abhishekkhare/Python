x = 5
print(x)
print(type(x))
print("************************")
x = "Hello World"
print(x)
print(type(x))
print("************************")
x = 20.5
print(x)
print(type(x))
print("************************")
x = 1j
print(x)
print(type(x))
print("************************")
x = ["apple", "banana", "cherry"]
print(x)
print(type(x))
print("************************")
x = ("apple", "banana", "cherry")
print(x)
print(type(x))
print("************************")
x = range(6)
print(x)
print(type(x))
print("************************")
x = {"name" : "John", "age" : 36}
print(x)
print(type(x))
print("************************")
x = {"apple", "banana", "cherry"}
print(x)
print(type(x))
print("************************")
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
print("************************")
x = True
print(x)
print(type(x))
print("************************")
x = b"Hello"
print(x)
print(type(x))
print("************************")
x = bytearray(5)
print(x)
print(type(x))
print("************************")
x = memoryview(bytes(5))
print(x)
print(type(x))
print("************************")

print("######## Type Conversion ############")
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))