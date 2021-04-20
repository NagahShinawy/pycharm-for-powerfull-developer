"""
created by Nagaj at 19/04/2021
"""
import sqlite3
import os
import pandas as pd


connection = sqlite3.connect(os.path.join(os.getcwd(), "menu.db"))
cursor = connection.cursor()

cursor.execute("SELECT * FROM menu")
rows = cursor.fetchall()
print(rows)

print(pd.read_sql_query("SELECT * FROM menu", connection))

print("#" * 100)
print(pd.read_sql_query("SELECT * FROM menu WHERE charge = 5", connection))
