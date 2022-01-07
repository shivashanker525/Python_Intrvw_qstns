string1 = "shivashanker"

from collections import OrderedDict


d = OrderedDict()
for i in string1:
    if i in d:
        d[i] += 1 
    else:
        d[i] = 1 
        
print(d)




name = ['a','d','b','c']
id = [1,4,2,3]
dict2 = {}
dict1 = OrderedDict()
for i,j in zip(name,id):
    dict1[i] = j 
    dict2[i] = j 
    
    
print(dict1)
print(dict2)
id1 = [1,2,3,4,5,6,7,8,9]

funct = list(filter(lambda x: x % 2 == 0, id1))

print(funct)

#sorting list elemnts usng numbers 
p = [('a',2),('b',1),('c',3)]


p.sort(key = lambda x: x[1])
print(p)
print(dict(p))


