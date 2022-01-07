"""A Generator is a special function which contains multiple values in it
But generator will not take the memory space for the data values which it have
It will generate each value dynamically,then it concumes
first itertion and goes for next"""

"""For example range() function is a generator function
It will have range of numbers but it will generate whenever it gioes for lop only
And Generator is also an iterator 

range is a built-in generator class

custom generator
Whenever we use yield kjeyword in our function then that can be treated as  a generator"""

def gen_func(num):
    for i in range(1,num):
        yield i**2

squares = gen_func(5)
for i in squares:
    print(i)

def gen_func_stemen():
    print("yield values")
    yield 10
    print("yield values")
    yield 20 
    print("yield values")
    yield 30

y = gen_func_stemen()

for i in y:
    print(i)