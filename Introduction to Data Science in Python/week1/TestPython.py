print("Hello World!~")
def do_math(a, b, kind=None):
  if (kind=='add'):
    return a+b
  else:
    return a-b

print(do_math(1, 2))
print(do_math(1, 2, 'add'))
