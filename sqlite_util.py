# Helper functions for working with SQLite
import sqlite3
from sqlite3 import Error

def create_connection(path: str) -> (sqlite3.Connection | None):
    connection: (sqlite3.Connection | None) = None
    try:
        connection = sqlite3.connect(path)
        print("Successfully connected to Database!")
    except Error as err:
        print(f"Failed to connect to Database with error: {err}")
    # Turn on foreign keys, a key concept in relational databases
    connection.execute("PRAGMA foreign_keys = ON;")
    return connection


def execute_query(connection: sqlite3.Connection, query: str) -> (list[any]|None):
    cursor: sqlite3.Cursor = connection.cursor()
    result: (list[any]|None) = None
    try:
        result = cursor.execute(query).fetchall()
        connection.commit()
    except Error as err:
        print(f"Query failed with error: {err}")
    cursor.close()
    return result


def execute_script(connection: sqlite3.Connection, path: str) -> (list[any]):
    with open(path, "r") as sqlf:
        script: str = sqlf.read()
    cursor: sqlite3.Cursor = connection.cursor()
    result: list[any] = cursor.executescript(script).fetchall()
    connection.commit()
    cursor.close()
    return result

if __name__ == "__main__":
    con: sqlite3.Connection = create_connection('pets.db')
    if con == None:
        exit()
    
    cursor: sqlite3.Cursor = con.cursor()
    print(cursor.execute("PRAGMA foreign_keys;").fetchall())
    con.close()
