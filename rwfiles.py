# Reading and Writing Files
'''from pathlib import Path
print(Path('spam', 'bacon', 'eggs'))
print(str(Path('spam', 'bacon', 'eggs')))

#Join names from a list of filenames to end of a folder's name:
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path('C:\\Users\\Mobarok', filename))
    
from pathlib import Path
print(Path('spam') / 'bacon' / 'eggs')
print(Path('spam') / Path('bacon/eggs'))
print(Path('spam') / Path('bacon', 'eggs'))

homeFolder = Path('C:/Users/Mobarok')
subFolder = Path('spam')
print(homeFolder / subFolder / 'eggs.txt')


import os
print(Path.cwd())
#os.chdir('C:\\Windows\\System32')
print(Path.cwd())

print(Path.home())


import os
print(os.path.abspath('.'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

p = Path('C:/User/Mobarok/spam.txt')
print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)

print(Path.cwd())
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])

calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(calcFilePath))
print(os.path.dirname(calcFilePath))
print(os.path.split(calcFilePath))
print(calcFilePath.split(os.sep))

print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
#print(os.listdir('C:\\Windows\\System32'))

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)

import glob

files = glob.glob("*.txt")  # Find all .txt files in the current directory
print(files)

# Find files with a specific pattern

log_files = glob.glob("log_?.txt")  # Matches log_1.txt, log_2.txt, etc.
print(log_files)'''

'''winDir = Path('C:/Windows')
notExistDir = Path('C:/This/Folder/Does/Not/Exist')
calcFile = Path('C:/Windows/System32/calc.exe')
print(winDir.exists())       # True
print(notExistDir.exists())  # False
print(calcFile.exists())     # True
print(calcFile.is_file())    # True
print(calcFile.is_dir())     # False

from pathlib import Path
p = Path('spam.txt')

print(p.write_text('Hello, world?'))
print(p.read_text())

#First we have created a text file in our home folder outside of coding

helloFile = open(Path.home() / 'hello.txt')  # It will open the file in read mode 
                                              #When a file is opend in read mode, you                                                  can't write or modify it. However, if we                                                pass a string value 'r'  as a second                                                    argument to open()
                                              
helloContent = helloFile.read()
print(helloContent)

sonnetFile = open(Path.home() / 'sonnet29.txt')
print(sonnetFile.readlines())

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello, Siam!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)'''


'''import shelve

# Open a shelve file (creates one if it doesn’t exist)
with shelve.open("mydata") as db:
    db["name"] = "Mobarok Sarker"  # String
    db["age"] = 20  # Integer
    db["hobbies"] = ["Photography", "Programming"]  # List

print("Data stored successfully!")


# Open the shelve file in read mode
with shelve.open("mydata") as db:
    print("Name:", db["name"])
    print("Age:", db["age"])
    print("Hobbies:", db["hobbies"])

with shelve.open("mydata", writeback=True) as db:
    db["age"] = 21  # Modify existing data
    db["hobbies"].append("Gaming")  # Modify list inside shelve

print("Data updated!")


with shelve.open("mydata") as db:
    print(list(db.keys()))  # Output: ['name', 'age', 'hobbies']
    
with shelve.open("mydata") as db:
    print(list(db.values()))  # Output: ['Mobarok Sarker', 21, ['Photography', 'Programming', 'Gaming']]

with shelve.open("mydata") as db:
    if "name" in db:
        print("Key found!")

with shelve.open("mydata") as db:
    del db["age"]
    print("Age deleted!")
    
    
import shelve

# Open shelve file
db = shelve.open("myData")

# Store data
db["name"] = "Mobarok Sarker"
db["age"] = 20

# Close the file manually
db.close()'''


'''import pprint

data = {"name": "Mobarok", "age": 20, "hobbies": ["Photography", "Coding"]}

formatted_data = pprint.pformat(data)  # Converts the dictionary into a formatted string
print(formatted_data)  # See the output'''

import pprint

data = {"name": "Mobarok", "age": 20, "hobbies": ["Photography", "Coding"]}

# Convert dictionary to a formatted string
formatted_data = pprint.pformat(data)

# Save it to a Python file
with open("mydata.py", "w") as file:
    file.write(f"data = {formatted_data}\n")  # Save as a Python variable
import mydata

print(mydata.data)  # Access the stored dictionary
