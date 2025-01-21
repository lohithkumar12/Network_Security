import pymongo
import certifi
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
mongo_db_url = os.getenv("MONGO_DB_URL")

try:
    ca = certifi.where()
    client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
    db_names = client.list_database_names()
    print("Connected successfully. Databases:", db_names)
except Exception as e:
    print(f"MongoDB connection failed: {str(e)}")
