"""
Unit 3.2.1 Guided Lecutre
Date: 2022/11/17

Sqlite3 tutorial with python
"""

# import sq lite3
import sqlite3
import queries as q


# step 1: connect to database
# make sure spelling is correct
# assumes rpg_db is in the cwd
connection = sqlite3.connect(
    "rpg_db.sqlite3"
)  # returns Connection object, same as sqlite3.Connection()

# step 2: Make the "cursur" / accessor
cursor = connection.cursor()

# step 3: Write the query
# see queries.py

# step 4: Execute the query & fetch the results
results = cursor.execute(q.SELECT_ALL).fetchall()


if __name__ == "__main__":
    print(results[:5])
