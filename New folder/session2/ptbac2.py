
a = int(input("enter a: "))
b = int(input("enter b:"))
c = int(input("enter c:"))
delta = b**2 - 4*a*c 
x = -b/2*a
x1 = (-b - delta**0.5)/2*a
x2 = (-b + delta**0.5)/2*a
if delta<0:
    print("vo_nghiem")
elif delta==0:
    print("PT_co_nghiem_kep: {0}".format(x))
elif delta>0:
    print("PT_co_2_nghiem_phan_biet: x1={0} va x2={1}". format(x1, x2))

