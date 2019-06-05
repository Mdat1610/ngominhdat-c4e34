words = ["r", "w", "s", "o", "r"]
print(words)
print("Let's guess")
answer = input("Enter your answer:")
while True:
    if answer == 'sorrow':
        print("exactly")
        break
    else:
        print("Wrong!!! Answer again")
        answer = input("Enter your answer:")
        