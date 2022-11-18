"""
Unit 3.2.1 Assignment
Date: 2022/11/17

Practice SQL queries for the rpg_db database
"""
import sqlite3


queries = {
    # How many total characters are there?
    "TOTAL_CHARACTERS": """SELECT COUNT(*) FROM charactercreator_character;""",
    # How many of necromancer?
    "TOTAL_SUBCLASS": """SELECT COUNT(*) FROM charactercreator_necromancer;""",
    # How many total Items?
    "TOTAL_ITEMS": """SELECT COUNT(*) FROM armory_item;""",
    # How many of the Items are weapons?
    "WEAPONS": """SELECT COUNT(*) FROM armory_weapon;""",
    # How many of the items are not weapons?
    "NON_WEAPONS": """SELECT COUNT(*) FROM armory_item WHERE item_id NOT IN 
    (SELECT item_ptr_id FROM armory_weapon);""",
    # How many Items does each character have? (Return first 20 rows)
    "CHARACTER_ITEMS": """SELECT character_id, COUNT(*) 
    FROM charactercreator_character_inventory 
    GROUP BY character_id 
    LIMIT 20;""",
    # How many Weapons does each character have? (Return first 20 rows)
    "CHARACTER_WEAPONS": """
    SELECT char.character_id, COUNT(inv.item_id) as num_weapons 
    FROM charactercreator_character as char 
    LEFT JOIN 
    (SELECT character_id, item_id FROM charactercreator_character_inventory WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)) as inv ON char.character_id = inv.character_id 
    GROUP BY char.character_id 
    LIMIT 20;""",
    # On average, how many Items does each Character have?
    "AVG_CHARACTER_ITEMS": """
    SELECT 1.0 * COUNT(inv.item_id ) / COUNT(DISTINCT char.character_id) 
    FROM charactercreator_character as char 
    LEFT JOIN charactercreator_character_inventory as inv 
    ON char.character_id = inv.character_id""",
    # On average, how many Weapons does each character have?
    "AVG_CHARACTER_WEAPONS": """
    SELECT 1.0 * COUNT(weapon_inv.item_id ) / COUNT(DISTINCT char.character_id) 
    FROM charactercreator_character as char 
    LEFT JOIN 
    (SELECT character_id, item_id FROM charactercreator_character_inventory WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)) as weapon_inv 
    ON char.character_id = weapon_inv.character_id""",
}


if __name__ == "__main__":
    curs = sqlite3.connect("rpg_db.sqlite3").cursor()
    for name, query in queries.items():
        print(f"{name} Query: {curs.execute(query).fetchall()}")
