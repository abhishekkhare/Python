print("!!!!!!!!!! LIST !!!!!!!!!!!!!!")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print(thislist[1])
print(thislist[0])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
thislist[1] = "blackcurrant"
print(thislist)
print(len(thislist))

for x in thislist:
  print(x)

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist.append("orange")
print(thislist)
thislist.insert(1, "orange")
print(thislist)
thislist.remove("blackcurrant")
print(thislist)
thislist.pop()
print(thislist)
del thislist[0]
print(thislist)
mylist = list(thislist)
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
# note Constructor has the double round-brackets
thislist = list(("apple", "banana", "cherry"))
print(thislist)

print("!!!!!!!!!! Tuples !!!!!!!!!!!!!!")
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-5:-1])

# Change Tuple Values -
# You can convert the tuple into a list,
# change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

print("!!!!!!!!!! Set !!!!!!!!!!!!!!")
thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#thisset.remove("banana")

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
thisset.discard("banana")

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

print("!!!!!!!!!! Dictionary !!!!!!!!!!!!!!")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)
thisdict["year"] = 2018
print(thisdict)

for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y)

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print(len(thisdict))

thisdict["color"] = "red"
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

a = 33
b = 200
if b > a:
  print("b is greater than a")


a = 33
b = 200
if b > a:
  print("b is greater than a") # you will get an error