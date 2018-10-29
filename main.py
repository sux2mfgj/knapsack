import copy

#from sa import SA
from utils import objective

if __name__ == '__main__':

    values = [120, 130, 80, 100, 250, 185]
    costs = [10, 12, 7, 9, 21, 16]
    number_of_items = [0 for i in range(0, len(values))]
    capasity = 65

    #sa = SA(capasity, values, costs, copy.deepcopy(number_of_items))
    #best_result_of_sa = sa.solve()
    #print(objective(capasity, values, costs, best_result_of_sa))
