"""
User DAO (Data Access Object)
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from models.user import User
from bson import ObjectId

class UserDAOMongo:
    def __init__(self):
        try:
            load_dotenv()
            db_host = os.getenv("MONGODB_HOST")
            db_port = os.getenv("MONGODB_PORT")
            db_name = os.getenv("MONGODB_DB_NAME")
            db_user = os.getenv("DB_USERNAME")
            db_pass = os.getenv("DB_PASSWORD")
            self.client = MongoClient("mongodb://"+db_user+":"+db_pass+"@"+db_host+":"+db_port+"/") 
            self.db = self.client[db_name]
        except FileNotFoundError as e:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur : " + str(e))

    def select_all(self):
        """ Select all users from MongoDB """
        users = self.db["users"].find({})
        return [User(str(user["_id"]), user["name"], user["email"]) for user in users]

    def insert(self, user: User):
        """ Insert given user into MongoDB """
        result = self.db["users"].insert_one(user.__dict__)
        return result.inserted_id

    def update(self, user: User):
        """ Update given user in MongoDB """
        self.db["users"].update_one(
            {"_id": ObjectId(user.id)},
            {"$set": {"email": user.email, "name": user.name}}
        )
        

    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        result = self.db["users"].delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count
        
    def close(self):
        self.client.close()
