import math


class Calculator:

    def __init__(self, costs):
        self.costs = costs

    def markup(self, rt):
        mark = math.sqrt(rt)
        return self.costs * mark

    def __str__(self):
        return f"{self.costs}"


def main():
    # 2 slices of bread, peanut butter, jelly
    costs = [1.00 * 2, 1.5, 0.66]
    menu = Calculator(sum(costs))
    charge = menu.markup(4)
    print(f"PBJ Cost: {charge}")


if __name__ == '__main__':
    main()
