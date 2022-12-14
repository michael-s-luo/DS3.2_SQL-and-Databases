""" 
Unit 3.2.4 Assignment
Date: 2022/12/13

Helper functions to connect to and query our PosgreSQL database on 
ElephantSQL containing the titanic dataset.

"""


from os import getenv
from dotenv import load_dotenv
import psycopg2

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
