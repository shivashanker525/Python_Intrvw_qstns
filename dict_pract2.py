input1= {'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10, 'z' : {"m":'20'}}}, 'd': [1, 2, 3]}
# output - {'a': 1, 'c_a': 2, 'c_b_x': 5, 'c_b_y': 10, 'c_b_z_m': '20', 'd': [1, 2, 3]}

print(type(input1['c']))
print(input1['c']['a'])
print(input1['c']['b']['x'])
print(input1['c']['b']['z']['m'])
dict1 = {}
for i in input1:
    if type(input1[i]) is dict:
        for j in input1[i]:
            k = str(i) + '_'+ str(j)
            dict1[k] = input1[i][j]
            print(k)
            if type(input1[i][j]) is dict:
                for m in input1[i][j]:
                    k = str(i) + '_'+ str(j)+ '_' + str(m)
                    dict1[k] = input1[i][j][m]
                    print(k)
                    
                    if type(input1[i][j][m]) is dict:
                        for n in input1[i][j][m]:
                            k = str(i) + '_'+ str(j)+ '_' + str(m) + '_' + str(n)
                            dict1[k] = input1[i][j][m][n]
                            print(k)
    else:
        dict1.update({i:input1[i]})

# print(input1)
# for i in dict1:
#     if type(dict1[i]) is dict:
#         dict1.pop(i)
        
print(dict1)