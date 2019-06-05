import random
n = random.randint(1, 100)
print(n)
loop = True
count = 0

while loop:
    answer = int(input("enter a number(0-100) "))
    count += 1
    if answer < n:
        print("too small!")
    elif answer >n:
        print("too large")
    else:
        print("bingo")
        break
    if count == 7:
        print("Game over!")
        break