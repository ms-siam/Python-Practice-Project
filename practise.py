'''import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') #instead of (r'Batman | Batmobile | Batcopter | Batbat')
matchObject = batRegex.search('Batman lost his bat while driving Batmobile')
print(matchObject.group())
print(matchObject.group(1)) #group(1) will return the first group of the matched string

batRegex1 = re.compile(r'Bat(wo)?man') # ? means optional 
matchObject1 = batRegex1.search('The adventures of Batman')  
print(matchObject1.group()) # Batman
matchObject2 = batRegex1.search('The adventures of Batwoman')
print(matchObject2.group()) # Batwoman

from pathlib import Path
import os
print(Path.cwd())
os.chdir('C:\\Windows')
print(Path.cwd())
print(Path.home())
print(Path.cwd().is_absolute())
print(Path('Spam/bacon/eggs').is_absolute())

import send2trash
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not siam')
baconFile.close()
send2trash.send2trash('bacon.txt')'''

import os
for folderName, subFolders, filenames in os.walk('C:\\Users\\Mobarok Siam\\Desktop'):
    print(f"The folder name is: {folderName}")
    for subFolder in subFolders:
        print(f"Subfolder of {folderName}: {subFolder}")
    for filename in filenames:
        print(f"File inside of {folderName} : {filename}")
        
    print('')