from random import *

def generate_quiz():
    x = randint(0,100)
    y = randint(0,100)
    a = choice(["+", "-","*","/"])
    t = 0
    y = choice([5,4,3,2,1,0,0,0,0,-1,-2,-3,-4,-5])
    if a == "+":
        t = x + y
    elif a == "-":
        t = x - y
    elif a == "*":
        t = x * y
    elif a == "/":
        t = x/y
    t = t + y
    return [x, y, a, t]

def check_answer(x, y, op, result, user_choice):
    pass
