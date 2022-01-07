from collections import Counter

#Counting vowels in string

def count_vowels(str1):
    vowels = 'aeiou'
    str2 = str1.lower()
    s = []
    for i in range(len(str2)):
        if str2[i] in vowels:
            s.append(str2[i])
        else:
            pass  
    print(Counter(s))
        
count_vowels("WElcome to hcl")

# Finding a missing number in particular range
#Here we taken a range of 1 to 10
s = [1,2,3,4,6,7,8,9,10]
def miss_list_numberf(list1):
    for i in range(list1[0],list1[-1]+1):
        if i not in list1:
            print(i)

miss_list_numberf(s)      