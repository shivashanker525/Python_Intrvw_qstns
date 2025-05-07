list = [1,2,3]
print(list)
list.append([4,5,6])
print(list)

a = [0] * 10
print(a)
list.reverse()
print(list)

str_1 = "the sky is blue"
# blue is sky the
def reverseWords(str_input):
    str_split = str_input.split()
    str_split = str_split[::-1]
    return " ".join(str_split)

print(reverseWords(str_1))

d = {x:0 for x in ['a','b']}
print(d)

# lambda function
x = lambda x: x+10 # here x can be considered as lambda function name and we can use wherever necessary.
print(x(5))

# insert inside a defined function
def my_func(n):
    return lambda a: a*n

s = my_func(5)
print(s(2))

print("====sort dictionary ==========")
#  sort a dictionary by it's value
dict1 = {'a':3, 'b': 0, 'c': 2, 'd':-1}
print(sorted(dict1, key=lambda x:dict1[x]))

# enumerate function
my_list = ['life','is','hard']

for i,j in enumerate(my_list):
    print("Index ",i, ':', j)

# converting to list of tuples
l_c = [(i,j) for i,j in enumerate(my_list)]
print(l_c)
# rev_enum_list = list(enumerate(my_list))
# print(list(enumerate(my_list)))
# print(rev_enum_list)

list12 = [8,9,87,1,2,3,4]


list13 = [1, 2, 3, 4, 2, 5, 2, 3, 4, 6, 5]

dict1 = {}
for i in list13:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)

# If all characters in a string are 0 or 1 then we can consider it as binary string.
def is_binary(input_str):
    for i in input_str:
        if i not in '01':
            return False
    return True
# Input string to check
input_str = "1001110"
# Check if the input string is a binary string
if is_binary(input_str):
 print(f"'{input_str}' is a binary string.")
else:
 print(f"'{input_str}' is not a binary string.")

# To find uncommon/not matching words from the given two strings we can use symmetric difference function
def uncommon_words_in_two_strs(str1, str2):
    # Split the strings into words and convert them to sets
    words1 = set(str1.split())
    words2 = set(str2.split())

    # Find uncommon words by taking the set difference
    uncommon_words_set = words1.symmetric_difference(words2)

    # Convert the set of uncommon words back to a list
    uncommon_words_list = uncommon_words_set

    return uncommon_words_list
# Input two strings
string1 = "This is the first string"
string2 = "This is the second string"
# Find uncommon words between the two strings
uncommon = uncommon_words_in_two_strs(string1, string2)
# Print the uncommon words
print("Uncommon words:", uncommon)
   
#  duplicate elements in an array
def duplicates_array(array1):
    dict1 = {}
    for i in array1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    duplicates = []
    for i,j in dict1.items():
        if dict1[i] > 1:
            duplicates.append(i)
    return duplicates

# Input a string
input_string = "piyush sharma"
# Find duplicate characters in the string
duplicate_chars = duplicates_array(input_string)
# Print the list of duplicate characters
print("Duplicate characters:", duplicate_chars)


# key value pair list to the dictionary
key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

dict2 = {}
for i,j in key_values_list:
    dict2[i] = j
print(dict2)

#  ordered dictionay will have the feature of adding dictionary at the specified index.

# dictionary sort by keys and sort by values.

sample_dict = {'apple': 3, 'mango': 11, 'banana': 1, 'cherry': 2, 'date': 4}

# so here we are taking it as sorted then result will be key value pair list.
sorted_by_dict_keys = dict(sorted(sample_dict.items()))
# so then we again convert it into dictionary.
print(sorted_by_dict_keys)
for key,value in sorted_by_dict_keys.items():
    print(f"{key}: {value}")

#  sort by values
sorted_by_dict_values = dict(sorted(sample_dict.items(), key= lambda x:x[1]))
print(sorted_by_dict_values)

# password matching


import re
def is_valid_password(password):
    # pattern = r"^(?=.*[a-z])(?=.*[A-z])(?=.*[0-9])((?=.*[$#@])"
    if len(password) >= 6 and len(password) <= 12:
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])", password):
            return True
    return False

valid_pswds = []
input1 = input("Please Enter a comma seperated passwords ").split(',')
print(input1)
for i in input1:
    if is_valid_password(i):
        valid_pswds.append(i)
print(valid_pswds)