Yob = int(input("Enter yor year of birth" ))
Age = 2019 - Yob
print(Age)


if Age < 10:
    print("baby")
elif Age < 18:
    print("teenager")
elif Age <25:
    print("khong biet")
else:
    print("adult")