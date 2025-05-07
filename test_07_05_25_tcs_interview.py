import pandas as pd


dict1 = {'Name':['Shiva','Shanker','anusha','praban'],
        'Age':[26,34,26,43],
        'Salary':[10000,20000,30000,55000]}
        
df = pd.DataFrame(dict1)
print(df)

s = df.groupby('Age').max()
print(s)
    
import pandas as pd

s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([1,2,6,4,5])

s = set(s1).symmetric_difference(set(s2))
print(s)


# Write a function to rotate a list to the right by N positions. If N is negative, rotate to left? (eg., i/p - lst: [1, 2, 3, 4, 5] , N: 2; o/p - [4, 5, 1, 2, 3], If N: -2; o/p - [3, 4, 5, 1, 2]) 

def rotate_list(input_list,n):
    if n ==0:
        print(input_list)
    elif n <0:
        result = input_list[-n:] + input_list[:-n]
        print(result) 
    else:
        result = input_list[n+1:] + input_list[:n+1]
        print(result) 
        
rotate_list([1, 2, 3, 4, 5], 2)
    
    