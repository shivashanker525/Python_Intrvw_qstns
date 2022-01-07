
# copy vs Deep copy
list1 = [[1,2],1,2,3,4]

list_copy = list1.copy()

list_copy[0][1] = 5
print(list_copy)
print(list1)

import copy

list2 = [[2,8],5,2,3,4]

list_copy = copy.deepcopy(list2)

list_copy[0][1] = 6
print(list_copy)
print(list2)


# Finding duplicates and print duplicate numbers 
li = [1,2,3,4,5,6,7,3,6]

list_comp = [i for i in li if li.count(i) > 1]
print(list_comp)
print(list(set(list_comp)))

# Flattening a nested list
li = [[1,2,3],['e','r']]

list_comp1 = [i for j in li for i in j]

print(list_comp1)

def fib(number):
    if number <=1:
        return number
    else:
        return fib(number-1)+ fib(number-2)


for i in range(15):
    print(fib(i))

def fibn(number):
    a,b = 0,1
    count = 0
    sum = 0
    if number < 1:
        print("Invalid input")
    elif number == 1:
        print(a)
    else:
        while count < number:
            c = a + b
            sum += a
            print(a)
            a = b
            b = c
            
            count += 1
    print(sum)

fibn(8)


def prime_numm(number):
    for i in range(2,number):
        if number % i == 0:
            break
    else:
        print(number)

print(prime_numm(15))
print(prime_numm(25))
print(prime_numm(13))
print(prime_numm(53))
print(prime_numm(58))

def primme(a,b):
    for number in range(a,b):
        for i in range(2,number):
            if number % i == 0:
                break
        else:
            print(number)
primme(100,252)