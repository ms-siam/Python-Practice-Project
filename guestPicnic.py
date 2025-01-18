allGuests = {'Mishad': {'Chanachur': 1, 'Chips': 4},
             'Siam': {'Egg': 4, 'Coke': 1},
             'Lehri': {'Soup': 2, 'Juice': 1}}
def totalBrought(guests, item):
    numBrought = 0
    for k,v in guests.items():
        numBrought += v.get(item, 0)
    return numBrought
print('Number of things being brought: ')
print(' -Chips        ' + str(totalBrought(allGuests, 'Chips')))
print(' -Chanachur    ' + str(totalBrought(allGuests, 'Chanachur')))
print(' -Coke         ' + str(totalBrought(allGuests, 'Coke')))
print(' -Eggs         ' + str(totalBrought(allGuests, 'Egg')))
print(' -Juice        ' + str(totalBrought(allGuests, 'Juice')))
print(' -Soup         ' + str(totalBrought(allGuests, 'Soup')))