print("%%%%%%%%%%% Multiline Strings %%%%%%%%%%%")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)
print("%%%%%%%%%%% Strings are Arrays %%%%%%%%%%%")
a = "Hello, World!"
print(a[1])
print(a[5])
print(a[9])
print("%%%%%%%%%%% Slicing %%%%%%%%%%%")
b = "Hello, World!"
print(b[2:5])
print(b[3:9])
print("%%%%%%%%%%% Negative Indexing %%%%%%%%%%%")
b = "Hello, World!"
print(b[-5:-2])
print(b[-9:-3])
print("%%%%%%%%%%% String Methods %%%%%%%%%%%")
a = " Hello, World!  "
print(len(a))
print(a.strip())
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(","))
print("%%%%%%%%%%% Check String %%%%%%%%%%%")
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
x = "ain" not in txt
print(x)
print("%%%%%%%%%%% String Concatenation %%%%%%%%%%%")
a = "Hello"
b = "World"
c = a + b
print(c)
a = "Hello"
b = "World"
c = a + " " + b
print(c)
print("%%%%%%%%%%% String Format %%%%%%%%%%%")
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))