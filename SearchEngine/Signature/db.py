import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
class DB:
    def __init__(self):
        self.client = MongoClient(os.environ['MONGODB_URL'])

    def getDBName(self):
        for db_info in self.client.list_database_names():
            print(db_info)

    def saveSingleInfo(self, data, dataName):
        db = self.client[dataName]
        collection = db[dataName]
        collection.insert_one(data)

    def saveMultipleInfo(self, data: list, dataName):
        db = self.client[dataName]
        collection = db[dataName]
        collection.insert_many(data)

    def findSingleItem(self, ToFind: dict, WhichDB):
        db = self.client[WhichDB]
        results = db.find(ToFind)
        for result in results:
            print(result)

    def deleteDB(self, dbToDelete):
        self.client.drop_collection(dbToDelete)
        print("Done deleting database")