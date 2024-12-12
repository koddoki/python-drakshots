from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

uri = os.getenv('MONGO_URI')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["drakshots"]
shot_log_collection = db["shot_log"]


def insert_shot_log(shot_text):
    today = datetime.date.today()
    post = {
                "shot": shot_text,
                "date": today.isoformat()
            }
    try:
        shot_log_collection.insert_one(post)
    except Exception as e:
        print(f"Error inserting document: {e}")


def get_shot_count():
    return shot_log_collection.count_documents({})


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
