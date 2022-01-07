class A:
    def __init__(self):
        print("Self")

class B(A):
    def __init__(self):
        print("I'm class B")

#issubclass method will check whether a class is child of parent class or not
parent = A()
child = B()
print(issubclass(B,A))
print(isinstance(parent,A)) # It will check for whether it is an instance of an A class or not
