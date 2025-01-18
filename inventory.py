stuff = {'rope': 1, 'torch': 3, 'light': 6, 'fan': 3, 'ac': 2, 'chair': 6}

def displayInventory(inventory):
    print('Inventory: ')
    total_item = 0
    for k,v in inventory.items():
        total_item += v
        print(str(v) + ' ' + k)
    print('Total number of items; ' + str(total_item))

displayInventory(stuff)

