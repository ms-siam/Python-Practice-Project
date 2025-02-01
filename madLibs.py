import shelve

with open('MadLibs.txt', 'w') as file:
    file.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
with open('MadLibs.txt', 'r') as file:
    content = file.read()
    print(content)
    words = content.split()
    for i, word in enumerate(words):
        if word == 'ADJECTIVE':
            adjective = input('Enter an adjective: ')
            words[i] = adjective
        elif word == 'NOUN':
            noun = input('Enter a noun: ')
            words[i] = noun
        elif word == 'VERB':
            verb = input('Enter a verb: ')
            words[i] = verb
    Story = ' '.join(words)
    print(Story)
    
with shelve.open('Madlibs_Done', 'c') as newFile:
    story_number = len(newFile) + 1
    newFile[f"Story_{story_number}"] = Story
    
print(f"Your Story has been saved as Story_{story_number} in Madlibs_Done.txt")
