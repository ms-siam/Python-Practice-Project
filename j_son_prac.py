'''import json

data = {
    "Date" : "09 Feb, 2025",
    "Learning" : ['JSON', 'SQLITE3', 'PyQt'],
    "Doing" : "To-Do List Project"
}

#Writing to a json file

with open('data.json', 'w') as file:
    json.dump(data, file, indent = 4)
    
print('data.json file has been created.')'''


'''import json

with open('data.json', 'r') as file:
    data = json.load(file)
    
print(data)
print(data["Date"])

import json

data = {"name": "Mobarok", "age": 20}
print(data)
json_string = json.dumps(data, indent=4)
print(json_string)

import json

json_string = '{"name": "Mobarok", "age": 20}'

data = json.loads(json_string)  # Convert string to dictionary
print(data["name"])  # Accessing values'''

