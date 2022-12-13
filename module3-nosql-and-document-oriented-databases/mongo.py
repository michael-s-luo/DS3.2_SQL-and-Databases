"""
Unit 3.2.3 Guided Lecutre
Date: 2022/12/12

MongoDB & PyMongo Tutorial
Pipeline for sqlite3 database -> MongoDB
"""

from dotenv import load_dotenv
from os import getenv
import pymongo
import certifi
import sqlite
import queries as q


# load environment variables
load_dotenv()
PASSWORD = getenv("PASSWORD")
DBNAME = getenv("DBNAME")


def mongo_connect(
    dbname=DBNAME, password=PASSWORD, collection_name="characters"
):
    """Creates connection to MongoDB collection

    Parameters
    ----------
    dbname : str, optional
        Name of the database, by default DBNAME
    password : str, optional
        generated password, by default PASSWORD
    collection_name : str, optional
        by default "characters"

    Returns
    -------
    pymongo collection
    """
    client = pymongo.MongoClient(
        f"mongodb+srv://michael:{password}@cluster0.ljjc2dl.mongodb.net/{dbname}?retryWrites=true&w=majority",
        tlsCAFile=certifi.where(),
    )

    return client[dbname][collection_name]


def show_all(col) -> list:
    """Queries for every document in a collection

    Parameters
    ----------
    col : pymongo Collection

    Returns
    -------
    list of documents
        tuple format for documents
    """
    return list(col.find())


if __name__ == "__main__":
    # connect to MongoDB
    collection = mongo_connect()
    collection.drop()

    # Get data from SQLite
    sl_curs = sqlite.connect_to_db_cursor()

    # Get all unique character rows
    sl_characters = sqlite.execute_q(sl_curs, q.SELECT_ALL_CHARACTERS)
    # print(sl_characters[:5]) #See the first 5 records/rows

    # For each unique character, query for weapons + items
    # Insert each sl_characters row as a document along with weapons & items
    for character in sl_characters:
        # Item/weapon for each character returned in row/tuple format
        # List will be empty for an empty query
        weapons = [
            wep[0]
            for wep in sqlite.execute_q(
                sl_curs, q.SELECT_CHARACTER_WEAPONS_FORMAT.format(character[0])
            )
        ]
        items = [
            item[0]
            for item in sqlite.execute_q(
                sl_curs, q.SELECT_CHARACTER_ITEMS_FORMAT.format(character[0])
            )
        ]

        character_document = {
            "character_id": character[0],
            "name": character[1],
            "level": character[2],
            "exp": character[3],
            "hp": character[4],
            "strength": character[5],
            "intelligence": character[6],
            "dexterity": character[7],
            "widsom": character[8],
            "items": items,
            "weapons": weapons,
        }

        collection.insert_one(character_document)

    print(show_all(collection))
