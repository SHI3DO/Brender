from pymongo import MongoClient

from api.printer import print_
from api.token import data

mongo_data = data.get("mongo")

host = mongo_data.get("host")
user = mongo_data.get("user")
password = mongo_data.get("password")
db = mongo_data.get("db")


Mongo_URI = f"mongodb+srv://{user}:{password}@{host}/{db}?retryWrites=true&w=majority"
client = MongoClient(Mongo_URI)

print_(f"Connecting to MongoDB as {user}...")


database = client[db]
