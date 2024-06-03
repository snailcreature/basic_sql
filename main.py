from sqlite_util import *
import sqlite3

con: sqlite3.Connection = create_connection("pets.db")

###
for res in execute_query(con, "SELECT * FROM Pets;"):
    print(res)

###

con.close()