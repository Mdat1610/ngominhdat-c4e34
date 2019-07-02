from flask import Flask, render_template,  request
app = Flask(__name__)


@app.route("/add_bike", methods=["GET","POST"])
def add():
    if request.method == "GET":
        return render_template("addbike.html")
    elif request.method == "POST":
        form = request.form
        Model = form["model"]
        Fee = form["fee"]
        Img = form["image"]
        Year = form["year"]

        bike = {
            "Model":"Model",
            "Daily_fee":"Fee",
            "Image":"Img",
            "Year":"Year",
        }
        return("Added")
        print(bike)
if __name__ == "__main__":
    app.run(debug=True)