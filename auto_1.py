import os
import time
import tkinter
import sys

os.system("Visual Studio Code")

file_path  = '/home/srisailam/Desktop/FlaskProject'
k = []
s1= time.time()
for filename in os.listdir(file_path):
    filepath = os.path.join(file_path, filename)
    if filename[-2] + filename[-1] == 'py':
        l = (file_path + f'/{filename}')
        k.append(l)
        os.system(l)
        time.sleep(1)


print(k)

a = time.time()
d = a - s1
print(d)