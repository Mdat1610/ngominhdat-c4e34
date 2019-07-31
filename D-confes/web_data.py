from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient("mongodb+srv://admin:admin@clusterc4e34-cluster-oiaoe.mongodb.net/test?retryWrites=true&w=majority")
d_confes_data = client.D_confes_database

user_inf = d_confes_data["list_user"]
status = d_confes_data["list_status"]



list_users = {
    
    "user_name":"",
    "password":"",
}
list_status = {
    
    "content":"vai",
    "time":"",
    "comment":[
        {
            "id_comment":" Ku",
            "content_cmt":"Phe vai",
        },
        {
            "id_comment":"Cac Ku",
            "content_cmt":"Dit",
        }

    ]
}

# status.delete_many({})
# user_inf.delete_many({})
# user_inf.insert_one(list_users)
# status.insert_one(list_status)
