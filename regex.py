import re


pattern = r"[a-h]."
string1 = 'shiva shanker'

d = re.findall(pattern,string1)
print(d)