shop = ["T-Shirt", "Sweater"]
print(*shop, sep=", ")
new_item = "Jeans"
shop.append(new_item)
print(*shop, sep=", ")
shop[1] = "Skirt"
print(*shop, sep=", ")
del shop[2]
print(*shop, sep=", ")
