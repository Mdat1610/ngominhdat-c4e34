inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf',]
}
inventory["pocket"] = ['seashell', 'strange berry', 'lint']
inventory["backpack"].remove('dagger')
print(inventory)
inventory["gold"] = 550
print(inventory)
