for i in range(1,6):
    print(" " * i ,end="")
    print("*" * i )

i = 6
while i > 1:
    print("*" * i)
    i -= 1 
n = int(input("Enter number : "))
k = n-1
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k = k-1
    for j in range(0,i+1):
        print("* ",end="")
    print()


n = int(input("Enter number : "))
k = 0
for i in range(n,0,-1):
    for j in range(0,k):
        print(end=" ")
    k = k+1
    for j in range(i,0,-1):
        print("*",end="")
    for j in range(i,1,-1):
        print("*",end="")
    print()

