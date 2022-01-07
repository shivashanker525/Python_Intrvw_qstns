#Decorator with arguments
def decorator1(a,b):
    print("We are inside the decorator space")
    def wrapper(funct):
        print(a+b)
        print("We are out of the decorator space")
        return funct
    return wrapper

@decorator1(1,2)
def add(num):
    print(num)

add(5)

