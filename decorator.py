
def decorate(func):
    def wrapper(*args):
        print("Enter the decorator module")
        modified_args = [arg + 10 for arg in args]
        print("adding 10 to the arguments")
        print("Getting out of the decorator module")

        func(*modified_args)
    return wrapper

@decorate
def func_to(a,b):
    print("Inside actual function")
    print(a+b)

func_to(2,5)