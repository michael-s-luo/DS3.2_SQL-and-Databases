"""
Unit 3.2.2 Guided Project / Lecture
Date: 2022/11/18
"""


# Table Functions --------------------------------------------------------------

CREATE_TEST_TABLE = """
        CREATE TABLE IF NOT EXISTS test_table
        ("id" SERIAL NOT NULL PRIMARY KEY,
        "name" VARCHAR(200) NOT NULL,
        "age" INT NOT NULL,
        "country_of_origin" VARCHAR(200) NOT NULL);
"""

INSERT_TEST_TABLE = """
        INSERT INTO test_table ("name", "age", "country_of_origin")
        VALUES ('Michael L', 27, 'USA');
"""

DROP_TEST_TABLE = """
        DROP TABLE IF EXISTS test_table;
"""

CREATE_CHARACTER_TABLE = """
        CREATE TABLE IF NOT EXISTS characterscreator_character(
                "character_id" SERIAL NOT NULL PRIMARY KEY,
                "name" VARCHAR(30) NOT NULL,
                "level" INT NOT NULL,
                "exp" INT NOT NULL,
                "hp" INT NOT NULL,
                "strength" INT NOT NULL,
                "intelligence" INT NOT NULL,
                "dexterity" INT NOT NULL,
                "wisdom" INT NOT NULL
        );
"""

DROP_CHARACTER_TABLE = """
        DROP TABLE IF EXISTS characterscreator_character;
"""

# INSERT statements for rpg_db--------------------------------------------------
INSERT_MICHAEL = """
        INSERT INTO characters(
                "name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom"
        )
        VALUES(
                'Michael L', 69, 420, 420, 420, 420, 420, 420
        );
"""


# Queries for rpg_db-------------------------------------------------------------

SELECT_ALL_CHARACTERS = """
        SELECT * 
        FROM charactercreator_character
"""


# Queries and statements for titanic.csv assignment ----------------------------

CREATE_SURVIVED_TYPE = """
        CREATE TYPE survived as ENUM('0', '1')
"""

CREATE_PCLASS_TYPE = """
        CREATE TYPE pclass as ENUM('1', '2', '3')
"""

CREATE_SEX_TYPE = """
        CREATE TYPE sex as ENUM('male', 'female')
"""

CREATE_TITANIC_TABLE = """
        CREATE TABLE IF NOT EXISTS titanic(
                id INT NOT NULL PRIMARY KEY, 
                name text NOT NULL,
                sex sex NOT NULL,
                age FLOAT NOT NULL,
                "siblings/spouse aboard" INT NOT NULL,
                "parents/children aboard" INT NOT NULL,
                fare FLOAT NOT NULL,
                survived survived NOT NULL,
                pclass pclass NOT NULL
        )
"""

DROP_TITANIC_TABLE = """
        DROP TABLE IF EXISTS titanic;
"""


def insert_titanic_template(row_tuple):
    id, survived, pclass, name, sex, age, ss, pc, fare = row_tuple

    return f"""
        INSERT INTO titanic
        VALUES(
                {id}, '{name}', '{sex}', {age}, {ss}, {pc}, {fare}, '{survived}', '{pclass}'
        )
    """


TITANIC_COUNT_SEX = """
        SELECT sex, COUNT(*)
        FROM titanic
        GROUP BY sex;
"""
