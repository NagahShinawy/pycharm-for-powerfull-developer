"""
created by Nagaj at 19/04/2021
"""
import pyodbc

from config import server, db, user, password, driver

remotehost = "DRIVER={driver};SERVER={server};DATABASE={db};UID={user};PWD={password}".format(
    server=server, db=db, user=user, password=password, driver=driver
)
connection = pyodbc.connect(remotehost)

cursor = connection.cursor()

try:
    cursor.execute(
        "CREATE TABLE students (name TEXT, age INTEGER, cls_room TEXT)"
    )

except pyodbc.ProgrammingError:
    pass

students = [
    ("john", 13, "c11"),
    ("leon", 14, "c21"),
    ("james", 13, "c14"),
    ("sara", 15, "c35"),
]

cursor.executemany("INSERT INTO students values (?, ?, ?)", students)
connection.commit()

print(cursor.execute("SELECT * FROM students").fetchall())
