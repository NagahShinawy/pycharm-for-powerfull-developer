import numpy


def weekly_avg(costs):
    num_day = len(costs)
    total_costs = sum(costs)
    return total_costs / num_day


if __name__ == '__main__':
    weekly_costs = [20.00, 50.00, 40.00, 10.00]
    print(weekly_avg(weekly_costs))
    # using numpy
    print(numpy.average(weekly_costs))