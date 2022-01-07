string1 = "Hello ShivashankerI'mPythonHowareyopudoingwithyourjoband be happy fore"

# Here counting each element/character in string and representing them as key-value pairs
#and creating a dictionary with that key-value pairs
dict1 = {}
for element in string1:
    if element in dict1:
        dict1[element] += 1
    else:
        dict1[element] = 1
print(dict1)
max_values = list(set(dict1.values()))
v = max_values.sort(reverse=True)
print(max_values)

#For getting second largest elemnt from the dictionary

for i in dict1:
    if dict1[i] == max_values[1]:
        print(i)
        break # Here I have multiple keys having same second largest so I used here break
                # if only one present then there is no need of break keyword here