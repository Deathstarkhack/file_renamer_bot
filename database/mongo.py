from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.file_renamer
user_collection = db.users

def set_sequence(user_id, status):
    user_collection.update_one(
        {"_id": user_id}, {"$set": {"active": status, "count": 0}}, upsert=True
    )

def increase_count(user_id):
    user = user_collection.find_one({"_id": user_id})
    count = user.get("count", 0) + 1
    user_collection.update_one({"_id": user_id}, {"$set": {"count": count}})
    return count

def is_active(user_id):
    user = user_collection.find_one({"_id": user_id})
    return user.get("active", False)
