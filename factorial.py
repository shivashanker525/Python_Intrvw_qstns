def factorial(number):
    if number < 0:
        return 'Please enter numbers greater than 0'
    elif number == 0:
        return 1
    else:
        sum = 1
        for i in range(1,number+1):
            sum *= i 
        return sum
    
print(factorial(6))

def factorial_with_recursion(number):
    if number < 1: 
        return 1
    else:
        return number * factorial(number - 1)
    
print(factorial_with_recursion(5))