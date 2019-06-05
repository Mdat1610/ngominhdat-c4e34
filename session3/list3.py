favs = ["playing game", "listening music", "reading book"]
for index, value in enumerate(favs):
    print("{0}. {1}".format(index+1, value))


position = int(input("position?"))
update_favs = input("New value?")
favs[position - 1] = update_favs
for index, value in enumerate(favs):
    print("{0}. {1}".format(index+1, value))

