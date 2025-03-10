from pymongo import MongoClient

import json
import os
from time import time

from bson.objectid import ObjectId


client = MongoClient("mongodb://localhost:27017/")
db = client["prooktatas"]
collection = db['my_collection']

'''
Minden sql like utasítást a collection objecten keresztül adunk ki:
 - create - insert
 - select - read
 - update - upsert
 - delete - delete
'''

folder_path = r"C:\WORK\Prooktatas\2024-november-project\tutorials\jsons"
files = os.listdir(folder_path)
start_dt = time()

def insert_data():
    my_data = []
    cnt = 0
    for item in files:
        cnt += 1
        file_path = f"{folder_path}/{item}"

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        my_data.append(data)

        # if cnt % 100 == 0:
        #     collection.insert_many(my_data)
        #     my_data = []
        # else:
        #     ...
        # collection.insert_one(data)
    collection.insert_many(my_data)

    print(f"{time() - start_dt} sec")


def select_data():
    data = collection.find({'circuitRef': "albert_park"})
    data = collection.find({'$or': [{'circuitId':1, 'circuitId':2}]})

    # data2 = collection.find_one({'$or': [{'circuitId':1, 'circuitId':2}]})

    print(list(data))

def delete_delete():
    data = collection.delete_one({"kulcs": "ertek"})
    collection.delete_many({'$or': [{'circuitId':1}, {'circuitId':2}]})

def update_data():
    myquery = { "circuitId": {"$gt": 10}}
    newvalues = { "$set": { "kulcs": "Ricsi voltam" } }
    update_statement = collection.update_one(myquery, newvalues)
    update_statement = collection.update_many(myquery, newvalues)

    print(update_statement.modified_count)

def my_func():
    data = collection.find_one({"_id": ObjectId("67cf2d23666f3dd807b5d875")})
    print(data)

if __name__ == '__main__':
    my_func()