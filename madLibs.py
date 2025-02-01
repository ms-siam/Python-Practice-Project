
with open('MadLibs.txt', 'w') as file:
    file.write('The ADJECTIVE panda walked to the NOUN and then VERB . A nearby NOUN was unaffected by these events.')
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
    
with open('Madlibs_Done.txt', 'w') as newFile:
    newFile.write(Story)