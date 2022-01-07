

n = 6
for i in range(1,n):
    print('*' * i)
for i in range(1,n):
    print('*' * int(n-i))

for i in range(0,n):
    print(" " * (n-i),'*'*i)

for i in range(1,n):
    print(" " * (i),'*'*(n-i))


m = 8
k = m-1
for i in range(0,m):
    
    for j in range(0,k):
        print(end=" ")
    k = k-1
    for j in range(0,i+1):
        print("* ", end="")
    
    print('\r')
m = 8
k = m+1
for i in range(0,m):
    
    for j in range(0,i):
        print(end=" ")
    k = k-1
    for j in range(0,k):
        print("* ", end="")
    
    print('\r')