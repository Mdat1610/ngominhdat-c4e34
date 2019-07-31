favs = ["playing game", "listening music", "reading book"]
for index, value in enumerate(favs):
    print("{0}. {1}".format(index+1, value))
position = int(input("position?"))
del favs[position-1]
for index, value in enumerate(favs):
    print("{0}. {1}".format(index+1, value))
