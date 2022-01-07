# Looping through the sets and findding the index of a particular 
#number using enumerate function

set1 = {11,2,3,4,5,6,7,44,3,3,3,3,4,4,5,5,5,5,5,6,6,7,7,7,77,7,7}
print(set1)

for count,i in enumerate(set1):
    if i == 7:
        print((count,i))