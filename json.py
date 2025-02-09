import json

data = {
    "Date" : "09 Feb, 2025",
    "Learning" : ['JSON', 'SQLITE3', 'PyQt'],
    "Doing" : "To-Do List Project"
}

#Writing to a json file

with open('data.json', 'w') as file:
    json.dump(data, file, indent = 4)