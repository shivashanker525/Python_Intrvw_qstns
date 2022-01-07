class A:
    def __init__(self):
        print("Self")

    @staticmethod
    def method1():
        print("I.m static")
    def method2(self):
        print("I.m dynamic")

A.method1()
