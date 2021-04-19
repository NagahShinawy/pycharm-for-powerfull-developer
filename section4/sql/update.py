"""
created by Nagaj at 19/04/2021
"""


import os
import sqlite3

import pandas as pd

connection = sqlite3.connect(os.path.join(os.getcwd(), "menu.db"))
cursor = connection.cursor()

rows = cursor.execute("SELECT bread, charge FROM menu  WHERE charge = 4")

# before update


print(rows.fetchall())
cursor.execute("UPDATE menu SET bread='UPDATE-WHITE' where charge = 4")


print("#" * 100)

# after update
rows = cursor.execute("SELECT bread, charge FROM menu  WHERE charge = 4")

print(rows.fetchall())