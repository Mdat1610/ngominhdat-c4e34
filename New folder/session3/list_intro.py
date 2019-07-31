# food1 = 'com'
# foo2 = "chao"
# food3 = 'thit'
# food4 = 'rau'
# food5 = 'dau'

# # list/array
#menu = ["com", "chao", "thit", "rau", "dau"]
# index
#print(menu[-1])
#CRUD
#creat
#Read
#update
#delete
# 1.CREAT
# new_food = "tom"
# menu.append(new_food)
#print(*menu, sep=", ")
# 2. READ one
# print(menu[2])
#2.2 Read many
#loop by value:
# for food in menu:
#     print(food)
#loop by index
# for i in range(len(menu)):
#     print(i)
#     print(menu[i])
#loop by value, index:
# for index, value in enumerate(menu):
#     print(index, value)
#3. update
menu = ["com", "chao", "thit", "rau", "dau"]
# menu[1] = "bun"
# print(menu)
# 4. Delete
# delete by index
#del menu[2]
#delete by value
menu.remove("dau")
print(menu)

