"""
created by Nagaj at 19/04/2021
"""
import sqlite3
import os
import pandas as pd


connection = sqlite3.connect(os.path.join(os.getcwd(), "menu.db"))
menu = [
    ("Roast Beef", "Roasted B", "white", 10, 5.5),
    ("A", "Loaded Veggie", "wheat", 5, 2.5),
    ("B", "Hammy Lamby", "white", 12, 7.5),
]
connection.executemany("INSERT INTO menu values (?,?,?,?,?)", menu)

print(pd.read_sql_query("SELECT * FROM menu", connection))
connection.commit()

connection.close()
