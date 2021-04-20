users = [
    {"name": "John", "age": 23, "active": False},
    {"name": "Leon", "age": 20, "active": True},
    {"name": "James", "age": 25, "active": True},
    {"name": "Smith", "age": 27, "active": False},
]

active_users = [user for user in users if user['active']]

for user in active_users:
    print(user)
