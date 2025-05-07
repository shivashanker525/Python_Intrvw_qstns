

def prime_number(number):
    if number < 2:
        return 'Given number is not in range between 2 and above'
    if number == 2:
        return 'Number is a prime number'
    else:
        for i in range(2,number):
            if number % i == 0:
                return 'Number is not a prime number'
                break
        else:
            return 'Number is a prime number'
        
# print(prime_number(23))
# print(prime_number(21))
# print(prime_number(15))
# print(prime_number(151))
# print(prime_number(125))

def prime_series(number1,number2):
    for i in range(number1, number2):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")
        
prime_series(100,200)