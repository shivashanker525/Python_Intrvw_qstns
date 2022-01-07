from collections import Counter
import logging

s = [1,1,2,2,3,3,3,3,3,1,2,4,5,3,4,5,5]

d = Counter(s)
print(d.most_common)
print(max(d))

d = lambda a,b : a ** b
print(d(5,3))



