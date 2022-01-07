list1 = [1,4,2,7,9,4,73,85,67,7,8]


# append,insert,extend
#remove,pop,del, clear
# sort - list1.sort() and list1.sort(reverse= True)
# Reversing a list - list.reverse()

list1.append(587)
list1.insert(0,655)
list1.remove(73)
list1.pop(1) #so it will remove 1 indexed element

del list1[2]

list1.sort()
list1.sort(reverse=True)

list1.reverse()
print(list1)

copy_list = list1.copy()
contructor_list_copy = list(list1)

# Joining other list/iterable using extend method
list2 = [9,6,7,89]
list1.extend(list2)
print(list1)

d1 = list1.count(7)
print(d1)

# length of a list
print(len(list1))

#type of  alist
print(type(list1))
#To find an index of a specified value in a list
i = list1.index(8)
print(i)

#multiply two lists
print(list1*2)