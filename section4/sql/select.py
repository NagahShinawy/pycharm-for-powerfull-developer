"""
created by Nagaj at 19/04/2021
"""
import os
import sqlite3
from collections import namedtuple
import pandas as pd
from prettytable import PrettyTable

FIELDS = ["meat", "name", "bread", "charge", "cost", "stock", "in_stock"]
Menu = namedtuple("Menu", FIELDS)
menutable = PrettyTable()
menutable.field_names = FIELDS
connection = sqlite3.connect(os.path.join(os.getcwd(), "menu.db"))
cursor = connection.cursor()

cursor.execute("SELECT * FROM menu")
rows = cursor.fetchall()
print(rows)
print("#" * 100)
# print(pd.read_sql_query("SELECT * FROM menu", connection))
menutable.add_rows(rows)
for row in rows[:3]:
    menu = Menu(*row)
    print(menu.meat, menu.name, menu.bread, menu.charge, menu.cost, menu.stock, menu.in_stock)
    # menutable.add_row([menu.meat, menu.name, menu.bread, menu.charge, menu.cost, menu.stock, menu.in_stock])
    # menutable.add_row(row)

print(menutable)
print("#" * 100)
print(pd.read_sql_query("SELECT * FROM menu WHERE charge = 5", connection))
