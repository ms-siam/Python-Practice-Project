# Reading and Writing Files
from pathlib import Path
print(Path('spam', 'bacon', 'eggs'))
print(str(Path('spam', 'bacon', 'eggs')))

#Join names from a list of filenames to end of a folder's name:
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path('C:\\Users\\Mobarok', filename))
    