from pymongo import MongoClient

def test_mongo_connection():
    client = MongoClient("mongodb://user:pass@127.0.0.1:27017/")
    db = client["store_manager"]
    users = list(db["users"].find({}))
    assert len(users) >= 2
    print("MongoDB connection successful, users found:", users)
