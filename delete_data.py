# # Delete ALL data from the database

# import json
# from pymongo import MongoClient
# from dotenv import load_dotenv
# import os

# load_dotenv()
# mongo_uri = os.environ.get("DB_URL")

# # Connect to MongoDB
# client = MongoClient(mongo_uri)  # Replace with your MongoDB connection string
# db = client['morphius']  # Replace with your MongoDB database name
# collection = db['colleges']  # Replace with your desired collection name

# # remove all documents from the collection
# collection.delete_many({})
