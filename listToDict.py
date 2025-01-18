# display the inventory
def displayInventory(inventory):
    print('Inventory: ')
    total_item = 0
    for k,v in inventory.items():
        total_item += v
        print(str(v) + ' ' + k)
    print('Total number of items; ' + str(total_item))
# add to the inventory
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby', 'gold coin']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)
