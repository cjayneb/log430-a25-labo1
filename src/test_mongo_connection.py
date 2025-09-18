from pymongo import MongoClient

def test_mongo_connection():
    client = MongoClient("mongodb://user:pass@mongo:27017/?authSource=admin")
    db = client["store_manager"]
    users = list(db.users.find())
    assert len(users) >= 2
    print("MongoDB connection successful, users found:", users)
