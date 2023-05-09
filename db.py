import random
import re

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

# database for quotes
quotes_db = mongo["quotes"]



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
    if sad.find_one({"word": word}) is None:
        sad.insert_one({"_id": sad.count_documents({}), "word": word})

# adds an angry word to the database
def add_angry(word):
    if angry.find_one({"word": word}) is None:
        angry.insert_one({"_id": angry.count_documents({}), "word": word})

# adds an encouraging phrase to the database
def add_encourage(response):
    if encourage.find_one({"response": response}) is None:
        encourage.insert_one({"_id": encourage.count_documents({}), "response": response})

# adds a calming phrase to the database
def add_calm(response):
    if calm.find_one({"response": response}) is None:
        calm.insert_one({"_id": calm.count_documents({}), "response": response})

def add_quote(string):
    quote = string.split("-")
    if len(quote) != 2:
        return -1
    else:
        # eliminating duplicate collections for the same author
        for author in quotes_db.list_collections():
            if author["name"] in quote[1] or quote[1] in author["name"]:
                quote[1] = author["name"]

        # removes all non-alphabetic characters, goes to lowercase, and removes trailing/leading spaces
        regex = re.compile('[^a-zA-Z ]')
        author_col = quotes_db[regex.sub('', quote[1]).lower().strip()]
        if author_col.find_one({"content": quote[0]}) is None:
            author_col.insert_one({"_id": author_col.count_documents({}), "content": quote[0], "label": quote[1]})

def get_quote(target):
    found = False
    for author in quotes_db.list_collections():
        if target.lower() in author["name"].lower() or author["name"].lower() in target.lower():
            target = author["name"]
            found = True
    if found:
        target_col = quotes_db[target]
        rand_id = random.randint(0, target_col.count_documents({}) - 1)
        rand_quote = target_col.find_one({"_id": rand_id})
        return rand_quote["content"] + " - " + rand_quote["label"]
    else:
        return None











