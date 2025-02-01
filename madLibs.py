
import re

with open('MadLibs.txt', 'w') as file:
    file.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')

words = file.split()
for word in words:
    if word == 'ADJECTIVE':
        adjective = input('Enter an adjective: ')
        words[word] = adjective
    