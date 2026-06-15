
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://anikumar5858_db_user:fjg8nA5orJslCkiY@cluster0.xjgux6b.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)