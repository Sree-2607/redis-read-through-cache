import os
from pymongo import MongoClient

# MongoDB connection
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://localhost:27017"
)

# Create MongoDB client
mongo_client = MongoClient(MONGO_URI)

# Select database
database = mongo_client["todo_db"]

# Select collection
todos_collection = database["todos"]