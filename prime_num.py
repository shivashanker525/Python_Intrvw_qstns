# Check whether numvber is a prime or not
def prime(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
                break
        else:
            return True
        
print(prime(22))

# Prime number series between two numbers -series
def prime_num_series(a,b):
    for i in range(a,b):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i,end=",")

prime_num_series(100,500)


list1 = [2,3,4,5,6,6,7,8,9,3,4,2,89,56,78,34,23,12,79,98]
list11 = []
for i in list1:
    list11.append(prime(i))

print(list11)
n = 59
for i in range(2,n):
    if n % i == 0:
        print("not a prime")
        break
else:
    print("prime")