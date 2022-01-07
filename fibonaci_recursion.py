def fibonaci_recursive(number):
    if number <= 1:
        return number
    else:
        return fibonaci_recursive(number-1) + fibonaci_recursive(number-2)

# n = 5

# if n <= 0:
#     print("Please enter a positive number")
# else:
#     print("Fibonacci series")
#     for i in range(n):
#         print(fibonaci_recursive(i))


def fibonaci(number):
    a,b = 0,1
    count =0 
    sum = 0
    if number <= 0:
        print("please enter a positive number")
    elif number == 1:
        print(a)
    else:
        while count < number:
            sum += a
            c = a+b
            print(a)
            a = b
            b = c     
            count += 1
    print(f'sum of fibonaci series numbers {sum}')
    

# fibonaci(5)
if __name__ == "__main__":
    fibonaci(5)
    n = 8

    if n <= 0:
        print("Please enter a positive number")
    else:
        print("Fibonacci series")
        for i in range(n):
            print(fibonaci_recursive(i))

print(dir())