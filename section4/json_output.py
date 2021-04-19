"""
created by Nagaj at 19/04/2021
"""
import json


def make_item(name, bread, meat, cost, charge):
    return {
        "name": name,
        "bread": bread,
        "meat": meat,
        "cost": cost,
        "charge": charge
    }


menu = list()
menu.append(make_item(name="Roasted B", bread="white", meat="Roasted Beef", cost=5.00, charge=7.00))
menu.append(make_item(name="Loaded Veggie", bread="wheat", meat=None, cost=3.00, charge=5.00))
menu.append(make_item(name="Hammy Lamby", bread="wheat", meat=["ham", "lamb"], cost=8.00, charge=10.00))

with open("menu.json", "w") as f:
    json.dump(menu, f, indent=4)


