from flask import *
from bson import ObjectId
from web_data import *
web = Flask(__name__)

@web.route("/home")
def home():

    all_status = status.find()
    return render_template("home.html", all_status = all_status)
    
            
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
            
            return redirect ("/login")

        else:
            if password == check_user["password"]:
                
                return redirect("/home")
            else:
                return ("/login")

        

@web.route("/post", methods = ["GET", "POST"])
def post():
    if request.method == "GET":
        return render_template("post.html")
    elif request.method == "POST":
        form = request.form
        new_content = form["content_post"]
        new_status = {
            "content": new_content,
        }
        status.insert_one(new_status)
        return redirect("/home")

        




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
        return  redirect("/login")



@web.route("/home/<id>", methods = ["GET" "POST"])
def comment(id):
    status_detail = status.find_one({"_id":ObjectId(id)})
    if request.method == "GET":
        return render_template("status_detail.html", status_detail = status_detail)
    elif request.method == "POST":
        form = request.form
        new_comment = form["content_comment"]
        status.insert_one(new_comment)
        return redirect("/home/status_detail/<id>")



@web.route("/logout")
def logout():
    
    return redirect("/login")




if __name__ == "__main__":
    web.run(debug=True)

