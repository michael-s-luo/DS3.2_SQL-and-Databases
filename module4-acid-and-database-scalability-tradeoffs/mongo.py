""" 
Unit 3.2.4 Assignment
Date: 2022/12/15

Helper functions and class to connect to and query our MongoDB
containing the RPG data.

"""

from dotenv import load_dotenv
from os import getenv
import pymongo
import certifi


# load environment variables
load_dotenv()
PASSWORD = getenv("MONGOPASSWORD")
DBNAME = getenv("MONGODBNAME")


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


class MongoAnswers:
    """Class with functions to query a MongoDB containing RPG data

    Parameters
    ----------
    collection : pymongo collection"""

    def __init__(self, collection=mongo_connect()) -> None:

        self.collection = collection
        self.characters = list(collection.find())
        self.queries = {}

    def total_characters(self):
        total = len(self.characters)
        self.queries["Total characters"] = total
        return total

    def total_items(self):
        count = 0

        for character in self.characters:
            count += len(character["items"])

        self.queries["Total items"] = count
        return count

    def total_weapons(self):
        count = 0

        for character in self.characters:
            count += len(character["weapons"])

        self.queries["Total weapons"] = count
        return count

    def total_non_weapons(self):
        count = 0

        for character in self.characters:
            count += len(character["items"]) - len(character["weapons"])

        self.queries["Total non-weapons"] = count
        return count

    def character_items_first20(self):
        character_items = []
        for character in self.characters:
            character_items.append(
                (character["name"], len(character["items"]))
            )

        self.queries["Item count by character, first 20"] = character_items[
            :20
        ]
        return character_items[:20]

    def character_weapons_first20(self):
        character_weapons = []
        for character in self.characters:
            character_weapons.append(
                (character["name"], len(character["weapons"]))
            )

        self.queries[
            "Weapon count by character, first 20"
        ] = character_weapons[:20]
        return character_weapons[:20]

    def avg_item_per_character(self):
        total_items = 0

        for character in self.characters:
            total_items += len(character["items"])

        avg_item = round(total_items / len(self.characters), 2)
        self.queries["Average items per character"] = avg_item
        return avg_item

    def avg_weapon_per_character(self):
        total_weapons = 0

        for character in self.characters:
            total_weapons += len(character["weapons"])

        avg_weapon = round(total_weapons / len(self.characters), 2)
        self.queries["Average weapons per character"] = avg_weapon
        return avg_weapon

    def show_results(self):
        for name, query in self.queries.items():
            print(f"\n{name} -> {query}")
