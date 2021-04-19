"""
created by Nagaj at 19/04/2021
"""
import os
import sqlite3

DB_DIR = os.path.join(os.getcwd(), "menu.db")
connection = sqlite3.connect(DB_DIR)

SQL = """
CREATE TABLE IF NOT EXISTS menu (
            meat BLOB, 
            name TEXT, 
            bread TEXT,
            charge INTEGER, 
            cost REAL
);
"""

connection.execute(SQL)

connection.commit()
connection.close()
