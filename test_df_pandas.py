# importing pandas as pd
import pandas as pd
# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
# creating a dataframe from a dictionary 
df1 = pd.DataFrame(dict)
 
print(df1.head)
print(df1.tail)
print(df1.shape)
print(df1.size)
print(df1.info())
print(df1.describe())
print(df1.dtypes)
print(df1.isnull())
print(df1['name'])
print(df1[['name','degree']])
print(df1.iloc[:1,0:2])
print(df1[df1['score'] > 90])
df1['new'] = df1['name'] + '_' +df1['degree']
print(df1)

df1.drop(['new'], axis=1, inplace=True)
print(df1)

df1 = df1.rename(columns= {'name':'Name', 'degree': 'Degree'})
print(df1)

df1['score'] = df1['score'].replace(90,91)
print(df1)

df1.sort_values('Name',ascending=False)
print(df1)

print(df1['Degree'].unique())
print(df1['Degree'].nunique())

print(df1.groupby('score'))

data = {
    'EmployeeID': range(101, 111),  # Employee IDs from 101 to 110
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance'],
    'Salary': [50000, 70000, 65000, 72000, 68000, 62000, 53000, 71000, 69000, 60000]
}

# Create DataFrame
df2 = pd.DataFrame(data)
print(df2)

details = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Designation': ['Manager', 'Developer', 'Analyst', 'Marketer', 'Sys Admin', 
                    'Analyst', 'HR Executive', 'Content Strategist', 'Developer', 'Accountant'],
    'JoiningDate': ['2020-01-10', '2019-05-15', '2021-03-01', '2018-07-20', '2020-11-30', 
                    '2017-12-15', '2021-09-01', '2019-06-25', '2020-04-18', '2018-10-05']
}

# Create DataFrame
df3 = pd.DataFrame(details)

df4 = pd.concat([df2,df3], axis=1)
print(df4)

df5 = pd.concat([df2,df3], join='outer', axis=1)
print(df5)

df5['Salary'] = df5['Salary'].astype('float')
print(df5)
print(df5.index)
print(df5.columns)
print(df4.T)
print(df4.duplicated().any())
print(df2['Salary'].mean())
print(df2['Salary'].cumsum())
print(df2['Salary'].max())
print(df2['Salary'].min())
print(df2['Salary'].count())

print(df2.loc[df2['Salary'].idxmax()])

print(df2.at[1,'Name'])
print(df2.iat[2,1])