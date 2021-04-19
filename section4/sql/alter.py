
"""
created by Nagaj at 19/04/2021
"""

import os
import sqlite3

import pandas as pd

connection = sqlite3.connect(os.path.join(os.getcwd(), "menu.db"))
cursor = connection.cursor()
try:

    cursor.execute("ALTER TABLE menu ADD stock INT ")

except sqlite3.OperationalError as err:
    print(err)

print(pd.read_sql_query("SELECT bread, charge, stock FROM menu", connection))

# cursor.execute('ALTER TABLE menu DROP COLUMN stock')  # sqlite3.OperationalError: near "DROP": syntax error
# sqlite not support drop

print("#" * 100)


print(pd.read_sql_query("SELECT * FROM menu", connection))