from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient("mongodb+srv://admin:admin@clusterc4e34-cluster-oiaoe.mongodb.net/test?retryWrites=true&w=majority")

food_database = client.food_database
Foods = food_database["food_collection"]
users = food_database["Users"]
list_users = [
    {
        "username":"hduc",
        "password":"12345",
    },
    {
        "username":"mdat",
        "password":"123",
    },
    {
        "username":"haanh",
        "password":"1234",
    },

]
# users.insert_many(list_users)
