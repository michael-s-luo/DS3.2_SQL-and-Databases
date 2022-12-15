"""
Unit 3.2.4 Assignment
Date: 2022/12/13

Queries to answer assignment questions for our deployed PostgreSQL database 
(titanic data) and MongoDB (dummy RPG data).

"""
import pipeline_pg
import mongo

# PostgreSQL Titanic Data queries------------------------------------------------
titanic_queries = {
    "TOTAL_SURVIVED_VS_DIED": """
        SELECT survived, COUNT(*) 
        FROM titanic 
        GROUP BY survived;
    """,
    "TOTAL_BY_CLASS": """
        SELECT pclass, COUNT(*)
        FROM titanic
        GROUP BY pclass
        ORDER BY pclass ASC
    """,
    "TOTAL_SURVIVAL_BY_CLASS": """
        SELECT pclass, 
            SUM(survived) as count_survived, 
            COUNT(*) - SUM(survived) as count_died
        FROM titanic
        GROUP BY pclass
        ORDER BY pclass ASC;
    """,
    "SURVIVED_AVG_AGE": """
        SELECT survived, AVG(age) as avg_age
        FROM titanic
        GROUP BY survived;
    """,
    "PCLASS_AVG_AGE": """
        SELECT pclass, AVG(age) as avg_age
        FROM titanic
        GROUP BY pclass
        ORDER BY pclass ASC;
    """,
    "PCLASS_AVG_FARE": """
        SELECT pclass, AVG(fare) as avg_fare
        FROM titanic
        GROUP BY pclass
        ORDER BY pclass ASC;
    """,
    "SURVIVED_AVG_FARE": """
        SELECT survived, AVG(fare) as avg_fare
        FROM titanic
        GROUP BY survived
        ORDER BY survived DESC;
    """,
    "PCLASS_AVG_SIBLING/SPOUSE": """
        SELECT pclass, AVG("siblings/spouse aboard") as avg_sibling_spouse
        FROM titanic
        GROUP BY pclass
        ORDER BY pclass ASC;
    """,
    "SURVIVED_AVG_SIBLING/SPOUSE": """
        SELECT survived, AVG("siblings/spouse aboard") as avg_sibling_spouse
        FROM titanic
        GROUP BY survived
        ORDER BY survived DESC;
    """,
    "PCLASS_AVG_PARENTS/CHILDREN": """
        SELECT pclass, AVG("parents/children aboard") as avg_parents_children
        FROM titanic
        GROUP BY pclass
        ORDER BY pclass ASC;
    """,
    "SURVIVED_AVG_PARENTS/CHILDREN": """
        SELECT survived, AVG("parents/children aboard") as avg_parents_children
        FROM titanic
        GROUP BY survived
        ORDER BY survived DESC;
    """,
    # there aren't any duplicate names
    "DUPLICATE_NAMES": """
        SELECT t1.id, t1.name
        FROM titanic as t1
        INNER JOIN titanic as t2
        ON t1.name = t2.name
        WHERE t1.id != t2.id;
    """,
}


if __name__ == "__main__":
    # QUERY postgresql titanic data #########################################
    # Connect to postgresql database
    pg_conn, pg_curs = pipeline_pg.con_to_pg()

    # Print dictionary keys and resulting queries
    print("Posgresql Titanic Data Queries: \n")
    for name, query in titanic_queries.items():
        print(f"Query {name} -> {pipeline_pg.query_db(pg_curs, query)}")

    # QUERY mongodb rpg data ################################################
    print("\nMongoDB RPG Queries: \n")

    answers = mongo.MongoAnswers()
    answers.total_characters()
    answers.total_items()
    answers.total_weapons()
    answers.total_non_weapons()
    answers.character_items_first20()
    answers.character_weapons_first20()
    answers.avg_item_per_character()
    answers.avg_weapon_per_character()
    answers.show_results()
