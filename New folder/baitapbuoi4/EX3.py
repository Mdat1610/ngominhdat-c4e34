
math = {
    "a": 35,
    "b": 36,
    "c": 40,
    "d": 44,
}

print("if x = 8, then what is value of 4(x+3) ?")
for n,m in math.items():
    print(n,":", m)
while True:
    a = input("Enter your answer:")
    if a == "d":
        print("Correct")
        break
    else:
        print("Wrong. Pls answer again!!!")
