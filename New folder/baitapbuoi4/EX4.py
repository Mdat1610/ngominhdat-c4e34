math = {
    "a": 35,
    "b": 36,
    "c": 40,
    "d": 44,
}

print("if x = 8, then what is value of 4(x+3) ?")
for n,m in math.items():
    print(n,":", m)
a = input("Enter your answer:")
count = 0
if a == "d":
    count = count +1
    print("Correct")    
else:
    print("Wrong!!!")
score = [49,81,72,66,52]
a = {"a":55,
"b":65,
"c":75,
"d":85,
}
print("Estimate this answer (exact calculation not needed: ")
print("Jack  scored these  marks in 5 math tests:",score,"What is the mean?")
for p,q in a.items():
    print(p,":",q)
o = input("Enter your answer:")
if o == "b":
    count = count +1
    print("Correct")
else:
    print("Wrong!!!")
if count == 2:
    print("you correctly answer 2 out of 2 questions")
elif count == 1:
    print("you correctly answer 1 out of 2 questions")
    