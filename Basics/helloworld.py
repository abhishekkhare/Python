# This is a comment.
print("Hello, World!")
if 5 > 2:
  print("Five is greater than two!")

x = 5
y = "Hello, There!"

print(x)
print(y)

print("Hello, India!")  # This is a comment

# print("Hello, World!")
print("Cheers, Mate!")

# This is a comment written in more than just one line
print("Hello, Hi!")

# Since Python will ignore string literals that are not assigned to a
# variable, you can add a multiline string (triple quotes) in your code,
# and place your comment inside it:
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

x = 4 # x is of type int
print(x)
x = "Sally" # x is now of type str
print(x)

x = "John"
# is the same as
x = 'John'
print(x)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z = x + y
print(z)

x = 5
y = 10
print(x + y)

print("############# Global Variable ####################")
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)

print("###### global keyword ################")
def myfunc():
  global x
  x = "Superb"

myfunc()

print("Python is " + x)