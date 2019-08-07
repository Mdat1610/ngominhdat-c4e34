from flask import *
from bson import ObjectId
from web_data import *
import datetime
app = Flask(__name__)
app.config["SECRET_KEY"] = "nmd1610"


# session["username"] = None
@app.route("/home")
def home():
    if "logged" in session:
        if session["logged"]:
            all_status = status.find({})
            return render_template("home.html", all_status = all_status)
        else:
            return redirect("/login")
    else:
        return redirect("/login")
    
            
@app.route("/login", methods = ["GET", "POST"])
def loggin():
    tong_nguoi_dung = user_inf.count()
    new_number = tong_nguoi_dung + 1
    if "logged" in session:
        if session["logged"]:
            return redirect ("/home")
        else:
            if request.method == "GET":
                return render_template ("login.html", new_number = new_number)
            elif request.method == "POST":
                form = request.form
                username = form["username_login"]
                password =  form["password_login"]
                check_user = user_inf.find_one({"user_name": username})
                if check_user is None:
                    session["logged"] = False
                    return redirect ("/login")

                else:
                    if password == check_user["password"]:
                        session["logged"] = True

                        print(username)
                        session["username"] = username
                        return redirect("/home")
                        
                    else:
                        return ("/login")
    else:
        session["logged"] = False
        return redirect('/login')



@app.route("/register", methods = ["POST"])
def register():
    tong_nguoi_dung = user_inf.count()
    new_number = tong_nguoi_dung + 1
    if "logged"in session:
        if session["logged"]:   
            return redirect("/home")
        else:
            
            if request.method == "POST":
                form  = request.form
                password_register = form["password_register"]
                username_register = f'User {new_number}'
                
                new_user = {
                    "user_name":username_register,
                    "password":password_register,
                }
                user_inf.insert_one(new_user)
               
                return  redirect("/login")
    else:
        session["logged"] =False
        return redirect("/login")             



@app.route("/home/<id>",)
def status_detail(id):
    status_detail = status.find_one({"_id":ObjectId(id)})
    username = session["username"]
    return render_template("status_detail.html", status_detail = status_detail, username = username)

@app.route("/post", methods = ["GET", "POST"])
def post():
    username = session["username"]
    if request.method == "GET":
        return render_template("post.html", username = username)
    elif request.method == "POST":
        form = request.form
        new_content = form["content_post"]
        timestamp = datetime.datetime.now()
        new_status = {
            "content": new_content,
            'user': username,
            'time': timestamp,
            'comment': []
        }
        status.insert_one(new_status)
        return redirect("/home")

    

@app.route("/comment/<id>", methods = ["POST"])
def comment(id):
    if request.method == "POST":
        e = status.find_one({"_id": ObjectId(id)})
        username = session["username"]
        form = request.form
        new_cmt = form["cmt_content"]

        new_comment = { "$push": {"comment": {"user": username,"content": new_cmt}}}
        status.update_one(e, new_comment)
        return redirect ("/home/{}".format(id))


@app.route("/logout")
def logout():
    del session["logged"]

    return redirect("/login")




if __name__ == "__main__":
    app.run(debug=True)

