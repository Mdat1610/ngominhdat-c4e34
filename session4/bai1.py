dic = {"hc": "học",
"ng": "người",
"bt": "biết",
"fb": "facebook",
"bl": "block",
"unf": "unfriend",
"stt": "status",
"ms": "mới",
}
while True:
    for key in dic:
        print(key, end=" ")
    print()
    n = input("enter your teencode: ")
    if n in dic:
        print(dic[n])
    else:
        print("Not Found")
        answer = input("contribute?(Y/N): ")
        if answer == "y" or answer == "Y":
            mean = input("Meaning?: ")
            dic[n] = mean
            print(dic)
        else:
            print("GoodBye")
            break















































# for key in dic:
#     if n == key:
#         m = dic[n]
#         print(m)
#     elif n != key:
#         print("Not Found")
#         g = input("Do you want to add (Y/N): ")
#         if g == "N":
#             print("GoodBye")
#         elif g == "Y":
#             p = input("Enter your translation:")
#             dic[n] = p
#             print(dic)      

    
    