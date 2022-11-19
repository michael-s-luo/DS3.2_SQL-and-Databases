"""
Unit 3.2.2 Project
Date: 2022/11/18
"""

import pipeline as pipe
import pandas as pd
import queries as q


def csv_to_db(
    connection, cursor, csv_path="titanic.csv", table_name="titanic"
):
    """Writes to a postgresql db the contents of a csv file. Uses an intermediary pandas DataFrame.

    This function assumes the table ALREADY EXISTS with the correct schema!

    Parameters
    ----------
    connection : psycopg2 connection

    cursor : psycopg2 cursor

    csv_path : str, optional
        path to csv, by default "titanic.csv"

    table_name : str, optional
        , by default "titanic"
    """

    # Read csv into DataFrame and do some cleaning
    df = pd.read_csv(csv_path)
    # replace single quote, not compatible with posgresql text fields
    # TODO: replace with generalized code for all object/string columns
    df = df.assign(Name=df["Name"].str.replace("'", "*"))  # TODO
    df.columns = df.columns.str.lower()

    # # DEBUG: check df, DONE
    # print(df.head(n=5))
    # print(df.info())
    # # END DEBUG

    # Iterate each row of df and insert into database
    for row_tuple in df.itertuples(index=True, name=None):
        # titanic format: (Index=0, survived=0, pclass=3, name='Mr. Owen Harris Braund', sex='male', age=22.0, _6=1, _7=0, fare=7.25)

        # DEBUG: check tuples, DONE
        # print(row_tuple)
        # END DEBUG

        insert_statement = q.insert_titanic_template(row_tuple)
        pipe.modify_db(connection, cursor, query=insert_statement)


if __name__ == "__main__":

    # postgresql db conection + cursor from our previous pipeline.py module
    pg_conn, pg_curs = pipe.con_to_pg()

    # Make enumerated types & titanic table
    # Queries are in queries.py
    titanic_schema_statements = [
        # only need to create enumerated types once!
        # q.CREATE_SURVIVED_TYPE,
        # q.CREATE_PCLASS_TYPE,
        # q.CREATE_SEX_TYPE,
        q.DROP_TITANIC_TABLE,
        q.CREATE_TITANIC_TABLE,
    ]
    pipe.modify_db(pg_conn, pg_curs, query=titanic_schema_statements)

    # Write csv to database
    csv_to_db(connection=pg_conn, cursor=pg_curs)

    # Query the pg db and print results:
    pg_curs.execute(q.TITANIC_COUNT_SEX)
    print(f"Count by sex: {pg_curs.fetchall()}")

    # Close connections
    pg_conn.close()
    pg_curs.close()
