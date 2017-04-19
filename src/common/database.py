import pymongo
class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client["fullstack"]

    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection,data):
       return  Database.DATABASE[collection].find_one(data)


    @staticmethod
    def from_mongo(id):
       return Database.DATABASE[collection].find_one(collection = "contents", query ={"id":id })


    @staticmethod
    def from_blog(id):
       return [content for content in Database.DATABASE[collection].find(collection = "contents", query = {"id":id})]