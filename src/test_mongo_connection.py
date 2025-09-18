from pymongo import MongoClient

from models.user import User

def test_mongo_connection():
    client = MongoClient("mongodb://user:pass@127.0.0.1:27017/")
    db = client["store_manager"]
    #db["users"].insert_one(User(None, "name", "email").__dict__)
    users = list(db["users"].find({}))
    assert len(users) >= 1
    print("MongoDB connection successful, users found:", users)
