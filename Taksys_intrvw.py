s = "shivashanker525@gmail.com"

l = []
for i in s:
    if i == '@' or type(i) == int:
        break
    else:
        l.append(i)
import re 
pattern = r'\A[a-zA-Z]+'
find1 = re.findall(pattern,s)
print(find1)
print(l)
print(len(l))

import pandas


data = {"a":1,
"b":2,
"c":3
}

df = pandas.DataFrame(data,index=[1,2,3])
print(df)
print(type(df))

d = df['a']






list1 = [1,2,4,2,5,6,8,4,2,1,5,8,9]

l = []
for i in list1:
    if i not in l:
        l.append(i)
        
print(l)
