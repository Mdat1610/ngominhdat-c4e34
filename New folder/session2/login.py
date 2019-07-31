username = "c4e"
passwork = "codethechange"
username_login = input("enter username:")

if username_login == username:
    password_login = input("enter password:")
    if password_login == password:
        print("welcom {}".format(username_login))
    else:
        print("wrong password")
else:
    print("not found")

