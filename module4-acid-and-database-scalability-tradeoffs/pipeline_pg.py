""" 
Unit 3.2.4 Assignment
Date: 2022/12/13

Functions to connect to and query with our PosgreSQL database on 
ElephantSQL.

"""


from os import getenv
from dotenv import load_dotenv
import psycopg2

# from sqlite_example import connect_to_db_cursor, execute_q, DELETE THIS
# import queries as q, DELETE THIS

# PostgreSQL connection credentials
# User & default database from ElephantSQL .env variables
load_dotenv()
DBNAME = getenv("DBNAME")
USER = getenv("USER")
# Passworld from ElephantSQL
PASSWORD = getenv("PASSWORD")
# Server from ElephantSQL
HOST = getenv("HOST")


def con_to_pg(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST):
    """Connects to pg database using info. Returns connection & cursor

    Parameters
    ----------
    dbname : str, optional
        database name, by default DBNAME
    user : str, optional
        user name, by default USER
    password : str, optional
        , by default PASSWORD
    host : str, optional
        host url, by default HOST

    Returns
    -------
    Tuple of connection & cursor objects
    """
    pg_conn = psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host
    )
    pg_curs = pg_conn.cursor()

    return pg_conn, pg_curs


def modify_db(conn, curs, statement: str | list[str]):
    """Executes sql statement against pg database using existing connection and cursor

    Parameters
    ----------
    conn : psycopg2 connection
    curs : psycopg2 cursor
    statement : str | list[str]
        SQL statement(s)
    """

    if isinstance(statement, list):
        for s in statement:
            curs.execute(s)
    else:
        curs.execute(statement)

    conn.commit()


def query_db(curs, query: str):
    """Queries posgresql db using existing connection & cursor

    Parameters
    ----------
    conn : psycopg2 connection

    curs : psycopg2 cursor

    query : str
        posgreSQL query

    Returns
    -------
    list of tuples representing rows
    """
    curs.execute(query)
    return curs.fetchall()


# TODO: delete main
if __name__ == "__main__":
    # Test table functions
    # pg_curs.execute(q.DROP_TEST_TABLE)
    # pg_curs.execute(q.CREATE_TEST_TABLE)
    # pg_curs.execute(q.INSERT_TEST_TABLE)

    # Test creating & inserting character table for rpg
    # pg_curs.execute(q.DROP_CHARACTER_TABLE)
    # pg_curs.execute(q.CREATE_CHARACTER_TABLE)
    # pg_curs.execute(q.INSERT_MICHAEL)

    # Instantiate pg db connections
    pg_conn, pg_curs = con_to_pg()

    # Create pg db character table
    modify_db(pg_conn, pg_curs, q.DROP_CHARACTER_TABLE)
    modify_db(pg_conn, pg_curs, q.CREATE_CHARACTER_TABLE)

    # Query all rows from characters table in rpg_db sqlite3
    sl_cursor = connect_to_db_cursor()
    characters_result = execute_q(sl_cursor, q.SELECT_ALL_CHARACTERS)
    # print(characters_result[:5])

    # Iterate each tuple from characters query and insert into pg db characters table
    for c in characters_result:
        modify_db(
            pg_conn,
            pg_curs,
            f"""
                INSERT INTO characterscreator_character(
                        "name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom"
                )
                VALUES(
                        '{c[1]}', {c[2]}, {c[3]}, {c[4]}, {c[5]}, {c[6]}, {c[7]}, {c[8]}
                );
            """,
        )

    # Test query
    print(
        query_db(
            pg_conn,
            pg_curs,
            query="""
            SELECT * FROM characterscreator_character
            LIMIT 5;
        """,
        )
    )

    # close
    pg_curs.close()
    pg_conn.close()
