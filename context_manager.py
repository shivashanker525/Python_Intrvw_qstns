# In python the resources like file opertions or data base connections usage is very common
# So the usage of resources should be limited/upto required extent
# Else there will be leakage of data and it will lead to the system slow or crash

# In python we use context manager 'with' to auto close file/db after it's usage.

# Example

with open('sample.txt') as f:
    print(f.read())

# So here file will be closed automatically after it's call/uasge
