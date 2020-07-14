print("Basic Lambda")
x = lambda a : a + 10
print(type(x))
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
my_function = lambda a, b, c : a + b
print(my_function(1, 2, 3))
print("Function Lambda")
def myfunc(n):
  return lambda a : a + a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
  return y*y*y;

g = lambda x: x*x*x
print(cube(7))
print(g(7))

print(cube(5))
print(g(5))

print("Complex Lambda")
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
  return person.split()[0] + ' ' + person.split()[-1]

for person in people:
  print(split_title_and_name(person))

print("********* option 1  *********")
for person in people:
  print((lambda person: person.split()[0] + ' ' + person.split()[-1])(person))

print("********* option 2 Map *********")
print(list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people)))


my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# Program to filter out only the even items from a list
for x in my_list:
  if x%2==0:
    print(x)
print("********* option 1   *********")
for x in my_list:
  print((lambda x: x*2)(x))
print("********* option 2 Filter *********")
print(list(filter(lambda x: (x%2 == 0) , my_list)))
print("********* option 2 Map *********")
print(list(map(lambda x: x * 2 , my_list)))

# Python code to illustrate
# reduce() with lambda()
# to get sum of a list
from functools import reduce

li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)

# Python Program to find palindromes in
# a list of strings.

my_list = ["geeks", "geeg", "keek", "practice", "aa"]
print(list(map(lambda x: "".join(reversed(x)), my_list)))
# printing only palindromes
print(list(filter(lambda x: (x == "".join(reversed(x))), my_list)))

# Python Program to find all anagrams[] of str in
# a list of strings.
from collections import Counter
str = "eegsk"
print(Counter("abhishek khare"))
print(Counter(str))
print(list(map(lambda x: (Counter(x)), my_list)))
# use anonymous function to filter anagrams of x.
print(list(filter(lambda x: (Counter(str) == Counter(x)), my_list)))

arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]
# filter(lambda x: x in arr1, arr2)  -->
# filter element x from list arr2 where x
# also lies in arr1
result = list(filter(lambda x: x in arr1, arr2))
print ("Intersection : ",result)