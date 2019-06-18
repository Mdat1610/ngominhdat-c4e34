import random
from bai3 import eval

a = ["+","-","*","/"]
p = random.choice(a)
c = 0
n = random.randint(0,9)
m = random.randint(0,9)

g = random.randint(-1,1)
k = ""

t = eval(p,n,m)
q = q + g
# q = 0
# if p == "+":
#     q = n + m
# elif p == "-":
#     q = n - m
# elif p == "*":
#     q = n * m
# elif p == "/":
#     q = n/m


print("{0} {1} {2} = {3}".format(n,p,m,q))
h = input("Enter your answer (Y/N):")
if k == "":
    if g == 0 and h == "Y":
        print("Yay")
    elif g == 0 and h == "N":
        print("Wrong")
    elif g != 0 and h == "Y":
        print("Wrong")
    elif g != 0 and  h == "N":
        print("Yay")
else:
    print(k)
    
    


        
        
    

