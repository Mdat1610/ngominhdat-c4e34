from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient("mongodb+srv://admin:admin@clusterc4e34-cluster-oiaoe.mongodb.net/test?retryWrites=true&w=majority")


# Create/ get database
first_database = client.demo_database

# Create / get collection
first_collection = first_database["demo_collection"]


first_document = {
    "name":"FO4",
    "description": "Football game",
}
list_document = [
    {
        "name": "Dota autochess",
        "description": "Valve",
    },
    {
        "name": "Pubg",
        "description":"battle royal",
    },
    {
        "name":"jump king",
        "description": "funny",
    },
]
# 1.Create
# 1.1 create one
# first_collection.insert_one(first_document)

#1.2 create many
# first_collection.insert_many(list_document)


# 2. Read
# 2.1 Read all
# 3 lazy loading
# games = first_collection.find()

# for game in games:
#      print(game)
# fo4_games = first_collection.find({"name": "FO4"})
# for fo4 in fo4_games:
#     print(fo4)
# 2.2 Read one

# dota_game = first_collection.find_one({"_id": ObjectId("5d2058e814d155b2507c25c2")})
# print(dota_game)


#3 Update
# query
# pubg_game = first_collection.find_one({"_id": ObjectId("5d2058e814d155b2507c25c2")})
# new_value = {"$set": {"name": "Player Unkown Battle Ground"}}
# first_collection.update_one(pubg_game, new_value)


# 4 Delete
pubg_game = first_collection.find_one({"_id": ObjectId("5d2058e814d155b2507c25c2")})
if pubg_game is not None:
    first_collection.delete_one(pubg_game)
elif:
    print("Not Found")
