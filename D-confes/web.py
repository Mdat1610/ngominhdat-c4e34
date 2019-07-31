from flask import *
from bson import ObjectId
from web_data import *
web = Flask(__name__)

@web.route("/home")
def home():
    
    new_status = status.find()
    return render_template("home.html", new_status = new_status)
    
            
@web.route("/login", methods = ["GET", "POST"])
def loggin():
    
    if request.method == "GET":
        return render_template ("login.html")
    elif request.method == "POST":
        form = request.form
        username = form["username_login"]
        password =  form["password_login"]
        check_user = user_inf.find_one({"user_name": username})
        if check_user is None:
            
            return "no1" 
        else:
            if password == check_user["password"]:
                
                return "yes"
            else:
                return "no2"

        

        




@web.route("/register", methods = ["GET", "POST"])
def register():
    tong_nguoi_dung = user_inf.count()
    print(tong_nguoi_dung)
    new_number = tong_nguoi_dung + 1
    if request.method == "GET":
        return render_template ("dangki.html", new_number = new_number)
    elif request.method == "POST":
        form  = request.form
        password_register = form["password_register"]
        username_register = f'User {new_number}'
        new_user = {
            "user_name":username_register,
            "password":password_register,
        }
        user_inf.insert_one(new_user)
        return  "ok"






@web.route("/logout")
def logout():
    session["logged"] = False
    return redirect("/login")

# @web.route("/home/family")


# @web.route("/home/work")


# @web.route("/home/love")


# @web.route("/home/marriage")


# @web.route("home/life")



if __name__ == "__main__":
    web.run(debug=True)

