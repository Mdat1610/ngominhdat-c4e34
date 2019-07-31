n = int(input("Enter x number:"))
m = int(input("Enter y number (y!=0):"))
if m == 0:
    print("wrong")
else:
    q = 0
    p = input("Enter your calculation:")
    if p == "+":
        q = n + m
    elif p == "-":
        q = n - m
    elif p == "*":
        q = n * m
    elif p == "/":
        q = n/m
    print(q)        