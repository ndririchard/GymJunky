
# IMPORTS
import time
from pymongo import MongoClient


# GLOBAL VARIABLE
CREDENTIAL = {"password" : "aW1BdIODAfP3Hv5M"}


# GLOBAL FUNCTIONS

def token(length):
    """
        OUTPUT -> str
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz \
        ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    res = ""
    i = 0
    while i < length:
        res += alphabet[i % len(alphabet)]
        i += 1
    return res

def checkTimestamp(timestamp):
    try:
        timestamp = int(timestamp)
        current_time = int(time.time())

        if timestamp <= current_time:
            return True
        else:
            return False

    except ValueError:
        return False

def Timestamp():
    return int(time.time())

def getInDatabase(object, collection):
    return collection.find_one(object)

def updateItem(collection, search_filter, new_item):
    res = collection.update_one(search_filter, {'$set': new_item})
    return res.modified_count

def addItem(collection, item):
    existing_item = collection.find_one(item)
    if existing_item:
        return None
    result = collection.insert_one(item)
    return result.inserted_id

def removeItem(collection, critere_recherche):
    existing_item = collection.find_one(critere_recherche)
    if not existing_item:
        return None
    result = collection.delete_one(critere_recherche)
    return result.deleted_count