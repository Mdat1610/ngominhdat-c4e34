n = int(input("nhap so n"))
is_prime = True
if n<2:
    print("not prime")
else:
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print("prime")
    else:
        print("not prime")
    

       

