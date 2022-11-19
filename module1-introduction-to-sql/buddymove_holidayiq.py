"""
Unit 3.2.1 Assignment
Date: 2022/11/17

Practice making database from CSV using sqlite3
"""

import sqlite3
import pandas as pd  # for df.to_sql

# Key is the description
queries = {
    "TOTAL_ROWS": """SELECT COUNT(*) FROM review""",
    "TOTAL_>100NATURE_OR_>100SHOPPING": """SELECT COUNT(*) FROM review
    WHERE Shopping >= 100 AND Nature >= 100""",
    "AVG_BY_CATEGORY": """SELECT AVG(Sports), AVG(Religious), AVG(Nature),AVG(Theatre), AVG(Shopping), AVG(Picnic) FROM review """,
}


def csv_to_db(
    con,
    csv_name="module1-introduction-to-sql\buddymove_holidayiq.csv",
):
    """Using an existing sqlite3 connection, writes contents of a csv to a new table.

    Parameters
    ----------
    con : sqlite3 connection
    csv_name : str, optional
        by default "buddymove_holidayiq.csv"
    """
    # Read in csv to dataframe
    df = pd.read_csv(csv_name)
    # print(df)  # for testing

    # write new table to db using pandas
    df.to_sql(name="review", con=con, if_exists="replace", index=False)


def execute_queries(con, queries):
    """Executes and prints queries using an existing connection

    Parameters
    ----------
    con : sqlite3 connection

    queries : dict
        dictionary in the format {'<name>':'<sql query>'}
    """
    curs = con.cursor()
    for name, query in queries.items():
        print(f"{name} query: {curs.execute(query).fetchall()}")

    curs.close()


if __name__ == "__main__":
    con = sqlite3.Connection("buddymove_holidayiq.sqlite3")
    csv_to_db(con)

    execute_queries(con, queries)
