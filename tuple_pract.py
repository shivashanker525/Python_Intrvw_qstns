tuple1 = (2,3,4,5,6,7,98,1,45,67,23,5,6,8,2,3,7)

# We can use count and index methods here

e = tuple1.index(5)
print(e)
f = tuple1.count(3)
print(f)

# It is immutable so we cannot use add/delete realetd methods


# Unpacking tuples 

fruits = ("apple","banana","orange") # It is single element to single unpacking
(red,yellow,blue) = fruits
print(red)
print(yellow)
print(blue)
print()
# If we are having multiple values gretaer than packing values then 
#we can use * befor any value according to your requirment
fruits1 = ("apple","banana","orange","pop","kiwi","lemon")
(red,*yellow,blue) = fruits1
print(red)
print(yellow)
print(blue)


# Join two tuples

tuple2 = (4,5,8,69,12,54,78,1,2,3)
tup3 = tuple1 + tuple2
print(tup3)
# multiply tuple

print(tuple1*2)
print(len(tuple1))

print(len(tup3))
print(type(tup3))

list22 = [1,2,3,5,6,89,78,45,12,36,45,12,]
tup_constuctor = tuple(list22)
print(tup_constuctor)
print(type(tup_constuctor))

import sys

g = sys.getsizeof(tup3)

print(g)