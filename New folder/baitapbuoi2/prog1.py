height1 = int(input("enter ur height (cm):"))
height = height1/100
weight = int(input("enter ur weight (kg):"))
BMi = weight/height/height
if BMi < 16:
    print("Severely underweight")
elif BMi < 18.5:
    print("Underweigh")
elif BMi < 25:
    print("Normal")
elif BMi < 30:
    print("Overweight")
elif BMi > 30:
    print("Obese")

