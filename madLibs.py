
import re

with open('MadLibs.txt', 'w') as file:
    file.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
with open('MadLibs.txt', 'r') as file:
    file = file.read()
    words = file.split()
    for word in words:
        if word == 'ADJECTIVE':
            adjective = input('Enter an adjective: ')
            words[word] = adjective
        elif word == 'NOUN':
            noun = input('Enter a noun: ')
            words[word] = noun
        elif word == 'VERB':
            verb = input('Enter a verb: ')
            words[word] = verb
    Story = ' '.join(words)
    print(Story)