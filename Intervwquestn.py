#string1 = "aabcjkasfhoieksdkasbjsajksaksajioasiwuweuu27378329983982398"
string1 = "aabbccddeeffgghhiijj"
from collections import Counter

s = dict(Counter(string1))

f = list(s.values())
print(f)
if len(f) == f.count(f[0]):
    print("True")
else:
    print("False")
























# #string1 = "aabcjkasfhoieksdkasbjsajksaksajioasiwuweuu27378329983982398"
# string1 = "aabbccddeeffgghhiijjkklloommnn"
# from collections import Counter

# s = Counter(string1)

# f = list(dict(s).values())

# for i in range(len(f)):
#     for j in range(i+1,len(f)):
#         if f[i] != f[j]:
#             print("True")
#             break   
            
#         else:
#             print("False")
#             break