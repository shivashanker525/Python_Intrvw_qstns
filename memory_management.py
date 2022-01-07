""" Here we are assigning one data value 5 to two variables 
So here only one object will be created in memory space 
that object will be referenced by both the variables
"""

a = 5
b = a
c = b
d = c
e = d
b = 7    # HEre only b gets changed to 7 data value But whatever expressions represented 
x = 5   # before will refer to the same data value 5
y = x
print(id(x))
print(id(y))
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))