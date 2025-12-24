import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_database_instance():
    client = MongoClient(os.environ.get("MONGO_URL"))
    return client["Mercadobot"]