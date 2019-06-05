favs = ["playing game", "listening music", "reading book"]
print(*favs, sep=",")
for index, value in enumerate(favs):
    print("{0}. {1}".format(index, value))