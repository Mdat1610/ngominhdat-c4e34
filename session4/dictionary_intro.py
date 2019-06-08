#Dictionary
person = { 
    "name": "Duc",
    "age": 22,
    "ex": 3,
    "university": "FTU",
}
# Key: Value

#CRUD
# 1.Read

# 1.1 Read one


# name = person["name"]
# age = person["age"]
# print(name)
# print(age)


# 1.2 Read many

# loop by key
# for key in person.key():
#     print(key)

# # loop by value
# for value in person.values():
#     print(value)


#loop by items
# for key,value in person.items():
#     # print(key, value)
#     print("{0}: {1}".format(key, value))


# 2. Creat/ Update:
# person["major"] = "Chinese"
# print(person)
# person["age"] = 25
# print(person)



# 3. Delete:
# del(person["ex"])
# print(person)