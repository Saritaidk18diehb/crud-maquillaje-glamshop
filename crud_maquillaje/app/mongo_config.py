from pymongo import MongoClient

def get_mongo_connection():
    uri = "mongodb+srv://sofi:1920@glamshopcrud.c2uly2m.mongodb.net/?retryWrites=true&w=majority&appName=GlamShopCRUD"
    client = MongoClient(uri)
    db = client["maquillaje_db"]
    return db
