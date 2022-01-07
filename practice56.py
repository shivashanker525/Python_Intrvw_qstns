import time
import datetime
import math
import random
print(time.time())
p = time.localtime()
o = list(time.localtime())
print(p)
print(o)

milliseconds = str(int(round(time.time() * 1000)))
print(milliseconds)
def rand_range(a,b):
    i = b - int(str(int(round(time.time() * 1000)))[-1] + str(int(round(time.time() * 1000)))[2])
    
    j = b - int(str(int(round(time.time() * 1000)))[-1] + str(int(round(time.time() * 1000)))[1])
    
    print(abs(i),abs(j))
    
    

rand_range(495, 560)  

print(random.randint(25,58))
print(random.randint(25,58))

