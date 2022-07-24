import pymongo
import datetime

# declare global variables
def dbConnect():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["certisign"]
    return db
