print(''' Guess your number game
Now think of a number from 0 to 100, then press 'Enter'
All you have to di is answer to my guess
'c' if my guess is corect
's' if my guess is smaller than your number
'l' if my guess is larger than your number ''')

low = 0
high = 100
while True:
    mid = (low + high)#2
    answer = input("is {0} your number?".format(mid))
    if answer == 'l':
        high = mid
    elif answer == 's':
        low = mid
    elif answer == 'c':
        print("I knew it")
        break