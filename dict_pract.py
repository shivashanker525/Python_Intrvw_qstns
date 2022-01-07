# A dictionary contains  key-value pair items in it.
from pprint import pprint
dict1 = {
    "name":"Shiva",
    "Profession":"Software Engineer",
    "Company":"Tesla",
    "Country": "India",
    "State": "telangana"
}

pprint(dict1)
print(len(dict1))
print(type(dict1))

# Accessing elemnts
print(dict1["name"])
print(dict1["Profession"])
print(dict1["Company"])
print(dict1.get("Country"))

for key,value in dict1.items():
    print((key,value))

# Changing/modifying items in a dictionary
dict1["Profession"] = "Information technology"
dict1.update({"State":"Telugu"})
pprint(dict1)

# Adding items into a dictionary
dict1["car"] = "volvo"
dict1.update({"brand":"Tekla"})
pprint(dict1)

# removing/deleting items into a dictionary

dict1.pop("Profession")
del dict1["Company"]
pprint(dict1)

for i in dict1:
    print(dict1[i])
print(dict1)