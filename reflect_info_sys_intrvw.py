# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

for i in range(6):
    print("*" * i)
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end = " ")
    print()

# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# for i,j in sample_dict.items():
#     if j == min(sample_dict.values()):
#         print(i,j)
        
import re
my_string = "The session was amazing! @Vib%!n @Ar&&n @jyothi30"
# # output = ['@Vib!n', '@Ar&&n', '@jyothi30']

pattern = r'@\b[A-Za-z0-9!&%]+'
serach1 = re.findall(pattern, my_string)
print(serach1)
        