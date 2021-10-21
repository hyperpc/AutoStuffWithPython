print('***** # 5.6.1 *****')
stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inventory):
    print("Inventory:")
    item_totle =0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_totle += v
    print('Total number of items: ' + str(item_totle))

displayInventory(stuff)

print('***** # 5.6.2 *****')
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory.setdefault(item, 1)
    return inventory

inv = {'gold coin': 42, 'rope':1}
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
