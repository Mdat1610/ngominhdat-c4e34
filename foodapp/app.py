from flask import Flask, render_template, redirect, request
app = Flask(__name__)
all_food = [{
        "title":"Bún đậu",
        "description": "Rất ngon",
        "type": "drink",
        "link": "https://andemdanang.com/wp-content/uploads/2018/09/b%C3%BAn-%C4%91%E1%BA%ADu-m%E1%BA%AFm-t%C3%B4m-%C4%91n.jpg",},
        {
        "title":"bún bò huế",
        "description": "Rất ngon",
        "type": "food",
        "link": "https://scm-assets.constant.co/scm/unilever/e9dc924f238fa6cc29465942875fe8f0/84024100-4767-4006-a26f-ec8ff577d9fa.jpg",},
        {
        "title":"bún cá",
        "description": "Rất ngon",
        "type": "food",
        "link": "https://beptruong.edu.vn/wp-content/uploads/2014/06/bun-ca-ha-noi.jpg",}]
@app.route("/foods")
def home():
    return render_template("allfoods.html", ALL_FOOD = all_food )
@app.route("/foods/<int:index>")
def food_detail(index):
    food = all_food[index]
    return  render_template("food_detail.html", FOOD=food)
@app.route("/foods/delete/<int:index>")
def delete_food(index):
        del all_food[index]
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
                all_food.append(b)


                return redirect("/foods")
@app.route("/foods/edit_food/<int:index>", methods=["GET", "POST"])
def edit_food(index):
        e = all_food[index]
        if request.method == "GET":
                return render_template("edit_food.html",E = e)
        elif request.method == "POST":
                form = request.form
                new_food ={
                        "title": form["title"],
                        "description": form["description"],
                        "link": form["link"],
                        "type": form["type"],
                }
                all_food[index]= new_food
                return redirect("/foods")
if __name__ == "__main__":
    app.run(debug=True)