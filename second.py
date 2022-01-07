import json

json_data1={"title": "foo", "imageData": "xyz123"},{"title": "bar", "imageData": "abc123"},{"title": "baz", "imageData": "def456"}
json_data11 = json.load(json_data1)
for element in json_data11:
    for each in element:
        if each == 'imageData':
            del json_data11[element][each]

print(json_data11)