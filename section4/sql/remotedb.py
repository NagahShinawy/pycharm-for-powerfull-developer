"""
created by Nagaj at 19/04/2021
"""

import pyodbc
import pandas as pd
from config import server, db, user, password, driver

remotehost = "DRIVER={driver};SERVER={server};DATABASE={db};UID={user};PWD={password}".format(
    server=server, db=db, user=user, password=password, driver=driver
)
connection = pyodbc.connect(remotehost)

cursor = connection.cursor()
try:

    cursor.execute(
        "CREATE TABLE sandwiches (meat TEXT, name TEXT, bread TEXT, charge INTEGER, cost REAL)"
    )

except pyodbc.ProgrammingError:
    pass


menu = [
    ("Roast Beef", "Roasted B", "white", 10, 5.5),
    ("A", "Loaded Veggie", "wheat", 5, 2.5),
    ("B", "Hammy Lamby", "white", 12, 7.5),
]


cursor.executemany("INSERT INTO sandwiches values (?,?,?,?,?) ", menu)
connection.commit()

sandwiches = cursor.execute("SELECT * FROM sandwiches")

print(sandwiches.fetchall())

print(pd.read_sql_query("SELECT * FROM sandwiches", connection))
connection.close()