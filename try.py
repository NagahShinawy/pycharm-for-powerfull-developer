
import pandas as pd

states = []

with open("states.txt") as f:
    lines = [line.strip() for line in f.readlines()]


for state in lines[1:]:
    st, x, y = state.split(",")
    states.append({"state": st, "x": x, "y": y})


pd.DataFrame(states).to_csv("states.csv", index=False)