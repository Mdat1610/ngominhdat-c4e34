from flask import Flask, render_template
app = Flask(__name__)
all_food = [{
        "title":"Bún đậu",
        "description": "Rất ngon",
        "type": "food",
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
if __name__ == "__main__":
    app.run(debug=True)