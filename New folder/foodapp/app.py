from flask import *
from bson import ObjectId
from food_database import Foods, users
app = Flask(__name__)

app.config["SECRET_KEY"] = "nmd1610"

@app.route("/foods")
def home():
        if "logged" in session:
                if session["logged"]:

                        all_food = Foods.find()
                        return render_template("allfoods.html", ALL_FOOD = all_food)
                else:
                        return redirect("/login")
        else:
                return redirect("/login")

@app.route("/foods/<id>")
def food_detail(id):
        food = Foods.find_one({"_id": ObjectId(id)})
        
        return render_template("food_detail.html", FOOD= food)


@app.route("/foods/delete/<id>")
def delete_food(id):
        delete = Foods.find_one({"_id": ObjectId(id)})
        Foods.delete_one(delete)
        return redirect("/foods")


@app.route("/foods/add_food", methods=["GET","POST"])
def add_food():
        if request.method == "GET":
                return render_template("add_food.html")
        elif request.method == "POST":
                form = request.form
                title = form["title"]
                description = form["description"]
                link = form["link"]
                food_type = form["type"]
                
                b = {"title":title,
                "description":description,
                "link":link,
                "type":food_type,
                }
                Foods.insert_one(b)


                return redirect("/foods")


@app.route("/foods/edit_food/<id>", methods=["GET", "POST"])
def edit_food(id):
        e = Foods.find_one({"_id": ObjectId(id)})
        if request.method == "GET":
                return render_template("edit_food.html",E = e)
        elif request.method == "POST":
                form = request.form
                new_food ={ "$set": {
                        "title": form["title"],
                        "description": form["description"],
                        "link": form["link"],
                        "type": form["type"],
                }}
                Foods.update_one(e, new_food)
                return redirect("/foods")
@app.route('/login', methods=["GET", "POST"])
def login():
    if "logged" in session:
        if session["logged"]:
            return redirect("/foods")
        else:
            if request.method == "GET":
                return render_template("login.html")
            elif request.method == "POST":
                form = request.form
                username = form["username_login"]
                password =  form["password_login"]
                user = users.find_one({"username": username})
                if user is None:
                    session["logged"] = False
                    return redirect('/login')
                else:
                    if password == user["password"]:
                        session["logged"] = True
                        return redirect("/foods")
                    else:
                        return redirect('/login')
    else:
        session["logged"] = False
        return redirect('/login')

@app.route("/register", methods=["GET", "POST"])
def register():
        if "logged"in session:
                if session["logged"]:
                        return redirect("/foods")
                else:
                        if request.method =="GET":
                                return render_template("register.html")
                        elif request.method == "POST":
                                form = request.form
                                username_register = form["username_register"]
                                password_register = form["password_register"]
                                userregister = users.find_one({"username": username_register})
                                if userregister is None:

                                        user_register = {
                                                "username":username_register,
                                                "password":password_register,
                                        }
                                        users.insert_one(user_register)
                                        return redirect("/login")
                                else:
                                        return "username has been used"
        else:
                session["logged"] =False
                return redirect("/login")                       
@app.route("/logout")
def logout():
        session["logged"] = False
        return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)