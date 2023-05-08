import random

from pymongo import MongoClient
from pymongo.server_api import ServerApi

# initialize mongodb client
uri = "mongodb+srv://sunahn76:MONGO@cluster0.theov4s.mongodb.net/?retryWrites=true&w=majority"
mongo = MongoClient(uri, server_api=ServerApi('1'))
try:
    mongo.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# initialize emotional words database
words_db = mongo["emotional_words"]
sad = words_db["sad"]
angry = words_db["angry"]
if "emotional_words" not in mongo.list_database_names():
    sad_starter = [
        {"_id": 0, "word": "depressed"},
        {"_id": 1, "word": "unhappy"},
        {"_id": 2, "word": "angry"},
        {"_id": 3, "word": "miserable"}
    ]
    sad.insert_many(sad_starter)
    angry_starter = [
        {"_id": 0, "word": "fuck"},
        {"_id": 1, "word": "shit"},
        {"_id": 2, "word": "bitch"},
        {"_id": 3, "word": "asshole"}
    ]
    angry.insert_many(angry_starter)

# initialize emotional responses database
responses_db = mongo["responses"]
encourage = responses_db["encourage"]
calm = responses_db["calm"]
if "responses" not in mongo.list_database_names():
    encourage_starter = [
        {"_id": 0, "response": "Cheer up!"},
        {"_id": 1, "response": "Hang in there!"},
        {"_id": 2, "response": "Dont be sad!"},
        {"_id": 3, "response": "Look at the bright side!"}
    ]
    encourage.insert_many(encourage_starter)
    calm_starter = [
        {"_id": 0, "response": "CALM DOWN"},
        {"_id": 1, "response": "HEY QUIET DOWN"},
        {"_id": 2, "response": "take a deep breath...in...out..."},
        {"_id": 3, "response": "shhhhhh"}
    ]
    calm.insert_many(calm_starter)


def respond(word):
    if sad.find_one({"word": word}) is not None:
        rand_id = random.randint(0, encourage.count_documents({}) - 1)
        rand_encourage = encourage.find_one({"_id": rand_id})
        return rand_encourage["response"]

    if angry.find_one({"word": word}) is not None:
        rand_id = random.randint(0, encourage.count_documents({}) - 1)
        rand_calm = calm.find_one({"_id": rand_id})
        return rand_calm["response"]


# adds a sad word to the database
def add_sad(word):
    print("function call")
    print(sad.find_one({"word": word}))
    if sad.find_one({"word": word}) is None:
        print("inside if")
        sad.insert_one({"_id": sad.count_documents({}), "word": word})
