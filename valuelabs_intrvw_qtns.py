

input1 = "a9b4c1"
#output = aaabbbbc

#Using for loop
f =''
for i in range(0,len(input1),2):
    f += input1[i] * int(input1[i+1])

#using while loop
j = 0
e = ''
while j < len(input1):
    e += input1[j]*int(input1[j+1])
    j = j + 2
    
print(e)
print(type(e))
print(f)