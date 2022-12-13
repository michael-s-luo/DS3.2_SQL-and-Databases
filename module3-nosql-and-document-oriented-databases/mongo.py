"""
Unit 3.2.3 Guided Lecutre
Date: 2022/12/08

MongoDB & Pymongo tutorial
"""

from dotenv import load_dotenv
from os import getenv
import pymongo, certifi, sqlite_example


# load environment variables
load_dotenv()
PASSWORD = getenv("PASSWORD")
DBNAME = getenv("DBNAME")


def mongo_connect(
    dbname=DBNAME, password=PASSWORD, collection_name="characters"
):
    client = pymongo.MongoClient(
        f"mongodb+srv://michael:{password}@cluster0.ljjc2dl.mongodb.net/{dbname}?retryWrites=true&w=majority",
        tlsCAFile=certifi.where(),
    )

    db = client[dbname]
    collection = db[collection_name]
    return collection


if __name__ == "__main__":
    test_collection = mongo_connect(collection_name="people")
    result = test_collection.find_one({"name": "Michael"})
    print(result)
