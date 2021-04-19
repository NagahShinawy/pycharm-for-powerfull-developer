"""
created by Nagaj at 19/04/2021
"""
import json

with open("menu.json", 'r') as f:
    data: dict = json.load(f)

if data:
    print(data[0])
print(data)