"""
created by Nagaj at 19/04/2021
"""
import json

with open("USD.json", "r") as f:
    data: dict = json.load(f)

base_dollar = data.get("base", None)
if base_dollar is not None:
    print(f"Base Dollar: {base_dollar}")

try:

    canadian = data["rates"]["CAD"]
    print(f"to Canadian Dollars: {canadian}")

except KeyError:
    print("nothing to show")

print(type(data))
