# Lambda with filter
s1 = [i for i in range(10)]            
w = list(filter(lambda x : x % 2 == 0,s1))
w1 = list(filter(lambda x : x % 2 != 0,s1))
print(w)
print(w1)

# Lambda with map

a = list(map(lambda x: x ** 3, s1))
print(a)


# Lambda with reduce
from functools import reduce
b = reduce(lambda x,y : x + y, s1)
print(b)

c = reduce(lambda x,y : x if x > y else y,s1)
print(c)

# Lambda with list comprehension
d = [lambda x=x: x*10 for x in range(5)]
for i in d:
    print(i())
