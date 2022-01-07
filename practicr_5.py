# array of 5 numbers: 43, 31, 76, 12, 5
# find the largest number in the array

array1 = [43, 31, 76, 12, 5]


max = 0 
for element in array1:
    if element > max:
        max = element
        
print(max)

# Remove "dg7" from string - "snapdg7blocs"
# output: 'snapblocs'



string1 = "snapdg7blocs"
samp_str = "dg7"

# list_str = string1.split()

# for item in list_str:
#     if item in samp_str:
#         list_str.remove(item)
        
# str2 = "".join(list_str)
# print(str2)

str1 = string1.replace('dg7', '')
print(str1)
print()

print('solution 3 & 4')

# Reverse a string "scolbpans"    
#Using indexing
sample_string = "scolbpans"  
rev_string = sample_string[::-1]
print(rev_string)

# using function reversed
r = ''.join(reversed(sample_string))
print(r)