

def decorator_simpl(func):
    print("Start Decorator")
    def inner_func(*x,**y):
        func(*x,**y)
        return func(*x,**y)
    print("End of a decorator")
    
    return inner_func
@decorator_simpl
def add(a):
    print("Sum function",a)

add(58)

