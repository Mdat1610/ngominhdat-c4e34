def eval(p,n,m):  
    q = 0
    if p == "+":
        q = n + m
    elif p == "-":
        q = n - m
    elif p == "*":
        q = n * m
    elif p == "/":
        q = n/m
    return q
