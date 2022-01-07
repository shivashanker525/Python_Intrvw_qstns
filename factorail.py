def factor_recursive(number):
    if number < 0:
        return 'please enter a positive number'
    if number == 1 or number == 0:
        return 1
    else:
        return number * factor_recursive(number-1)

print(factor_recursive(3))

def factor(number):
    n = 1 
    if number < 0:
        return 'please enter a positive number'
    elif number == 1 or number == 0:
        return 1
    else:
        for i in range(1,number+1):
            n = n * i
    return n

print(factor(5))