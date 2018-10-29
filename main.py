from functools import reduce
import copy

def objective(values, number_of_items):
    return reduce(
            lambda s, x: s + x[0] * x[1],
            zip(values, number_of_items),
            0)

def bruteforce(values, number_of_items):
    number_of_items[0] += 1

if __name__ == '__main__':

    values = [120, 130, 80, 100, 250, 185]
    number_of_items = [0 for i in range(0, len(values))]
    #result = bruteforce(values, copy.deepcopy(number_of_items))
    #print(objective(values, number_of_items))
    #print(number_of_items)
