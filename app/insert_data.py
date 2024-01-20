import json
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongo_uri = os.environ.get("DB_URL")

# Connect to MongoDB
client = MongoClient(mongo_uri)  # Replace with your MongoDB connection string
db = client['morphius']  # Replace with your MongoDB database name
collection = db['colleges']  # Replace with your desired collection name

# Read data from the file
with open('output.txt', 'r') as file:
    for line in file:
        try:
            # Parse each line as JSON
            data = json.loads(line)
            # Insert data into MongoDB
            collection.insert_many(data['results'])
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

print("Data imported successfully.")
