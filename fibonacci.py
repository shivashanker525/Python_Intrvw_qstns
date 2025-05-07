def fibonaci(number):
    a,b = 0,1

    if number < 0:
        print('ENter a number  greater than or equal to 1')
    elif number == 0:
        print(a)
    elif number == 1:
        print(b)
    else:
        for i in range(number):
            c = a + b
            a = b
            print(a, end= " ")
            b = c

fibonaci(5)

def recursive_fibonacci(number):
    if number <= 1:
        return number
    else:
        return recursive_fibonacci(number-1) + recursive_fibonacci(number-2)
print()
n = 6
if n < 0:
    print("enter a number greater than 0")
else:
    for i in range(n):
        print(recursive_fibonacci(i))