def printPicnic(itemsDict, leftWidth, rightWidth):
    print('Picnic Items'.center(leftWidth + rightWidth, '-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))
picnicItems = {'Apple': 12, 'Orange': 6, 'Lemon': 5}

printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)