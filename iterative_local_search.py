from logging import basicConfig
from utils import Solver, objective


class IterativeLocalSearch(Solver):
    def __init__(self, capasity, values, costs, number_of_items,
            neighbor_distance):
        super().__init__(capasity, values, costs, number_of_items)
        self.neighbor_distance = neighbor_distance

    def solve(self):
        return self.number_of_items


if __name__ == '__main__':
    # Parameters
    values = [120, 130, 80, 100, 250, 185]
    costs = [10, 12, 7, 9, 21, 16]
    number_of_items = [0 for i in range(0, len(values))]
    capasity = 100

    # for logging
    from logging import DEBUG
    basicConfig(level=DEBUG)

    sa = IterativeLocalSearch(capasity, values, costs, number_of_items, 2)
    best_result_of_sa = sa.solve()
    best_cost = objective(capasity, values, costs, best_result_of_sa)

    print('best conbination: ', best_result_of_sa)
    print('best cost:', best_cost)
