"""
created by Nagaj at 19/04/2021
"""

import os
import sqlite3

import pandas as pd

connection = sqlite3.connect(os.path.join(os.getcwd(), "menu.db"))
cursor = connection.cursor()

cursor.execute("SELECT meat, name, cost FROM menu")
rows = cursor.fetchall()
print(rows)

print("#" * 100)

menu_df = pd.read_sql_query("SELECT bread, charge, cost FROM menu", connection)
print(menu_df)

print("#" * 100)
print(pd.read_sql_query("SELECT * FROM menu WHERE charge = 5", connection))
