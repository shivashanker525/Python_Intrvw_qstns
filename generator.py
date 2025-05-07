

def generate(number):
    for i in range(number):
        yield i

for i in generate(6):
    print(i)

