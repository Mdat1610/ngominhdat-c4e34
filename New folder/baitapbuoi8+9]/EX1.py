from flask import Flask, render_template,  request
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient("mongodb+srv://admin:admin@clusterc4e34-cluster-oiaoe.mongodb.net/test?retryWrites=true&w=majority")
bike_data = client.Bike_Database
bike_collection = bike_data["Bike_Collection"]
app = Flask(__name__)
allbike = [
    {
        "model":"Honda Vision",
        "fee": "100000",
        "img": "",
        "year": "2015",
    }
]
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
        newbike = {
            "model": Model,
            "fee": Fee,
            "img": Img,
            "year": Year,
        }
        allbike.append(newbike)
        bike_collection.insert_many(allbike)  
        return("Added")
     
if __name__ == "__main__":
    app.run(debug=True)