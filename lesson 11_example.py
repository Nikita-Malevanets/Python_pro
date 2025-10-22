from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["test_collection"]

collection.insert_one({"name": "Nikita", "age": 33})

for doc in collection.find():
    print(doc)
