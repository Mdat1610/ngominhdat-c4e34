from random import randint
n = randint(0, 100)
print(n)
if n<=30:
    print("sunny")
elif n<=70:
    print("rainy")
elif n<=100:
    print("loudy")