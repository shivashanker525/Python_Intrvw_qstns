

set1 = {1,5,6,9,78,45,36,58,45,21,2,3}

# Accessing sets only way - for loop

for i in set1:
    print(i)

# Checkimg wheteher the element is there in a set or not
print(58 in set1)
print(5825 in set1)


#add and update methods add - add one element to set 
# update - add any another iterable/set to the current set

set1.add(499)
print(set1)

set2 = {589,599} # add another set
set3 = [5896,2584] # add any iterable

set1.update(set2)
set1.update(set3)
print(set1)

# for joining two sets we have union method also there
set4 = {"a","b"}
set3 = set1.union(set4) # but union only works with two sets joining
                        # and also it creates new set 
print(set3)

# remove,discard, del ,clear  methods are to delete the set items /set

set1.remove(2)
set1.discard(3)
# del will totally delete the set and there is no chnace for deleteing each element in a set
# clear will empties the set

print(set1)

