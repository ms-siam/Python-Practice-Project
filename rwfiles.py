# Reading and Writing Files
from pathlib import Path
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