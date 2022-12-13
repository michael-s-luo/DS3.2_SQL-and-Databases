"""
Unit 3.2.1 Guided Lecutre
Date: 2022/11/17

Sqlite3 tutorial with python
"""

# import sq lite3
import sqlite3
import queries as q


def connect_to_db_cursor(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name).cursor()


def execute_q(cursor, query):
    return cursor.execute(query).fetchall()


if __name__ == "__main__":
    curs = connect_to_db_cursor()
    print(execute_q(curs, q.SELECT_ALL_CHARACTERS)[:5])
