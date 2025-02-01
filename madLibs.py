
with open('MadLibs.txt', 'w') as file:
    file.write('The ADJECTIVE panda walked to the NOUN and then VERB . A nearby NOUN was unaffected by these events.')
with open('MadLibs.txt', 'r') as file:
    content = file.read()
    print(content)
    words = content.split()
    for word in words:
        if word == 'ADJECTIVE':
            adjective = input('Enter an adjective: ')
            words[words.index(word)] = adjective
        if word == 'NOUN':
            noun = input('Enter a noun: ')
            words[words.index(word)] = noun
        if word == 'VERB':
            verb = input('Enter a verb: ')
            words[words.index(word)] = verb
    Story = ' '.join(words)
    print(Story)