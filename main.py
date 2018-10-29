from functools import reduce
import copy

def objective(capasity, values, costs, number_of_items):
    total_value = reduce(
            lambda s, x: s + x[0] * x[1],
            zip(values, number_of_items),
            0)
    cost = reduce(lambda s, x: s + x[0] * x[1],
            zip(costs, number_of_items), 0)

    return (capasity >= cost, total_value)

def bruteforce(values, number_of_items):
    pass

if __name__ == '__main__':

    values = [120, 130, 80, 100, 250, 185]
    costs = [10, 12, 7, 9, 21, 16]
    number_of_items = [0 for i in range(0, len(values))]
    capasity = 65

    #result = bruteforce(values, copy.deepcopy(number_of_items))
    print(objective(capasity, values, costs, number_of_items))
