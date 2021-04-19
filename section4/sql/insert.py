
"""
created by Nagaj at 19/04/2021
"""

import os
import sqlite3

import pandas as pd

connection = sqlite3.connect(os.path.join(os.getcwd(), "menu.db"))
cursor = connection.cursor()

menus = [
    ("white", 4, 5),
    ("white", 7, 9.8),

]

# insert to custom cols
cursor.executemany("INSERT INTO menu(bread, charge, cost) values (?,?,?)", menus)

connection.commit()

menu_df = pd.read_sql_query("SELECT bread, charge, cost from menu WHERE charge = 4", connection)


print(menu_df)

connection.close()