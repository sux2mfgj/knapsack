import random
import math
from logging import basicConfig

from utils import Solver, objective


class SimulatedAnealing(Solver):
    def __init__(
            self,
            capasity,
            values,
            costs,
            number_of_items,
            neighbor_distance,
            T,
            cool):
        super().__init__(capasity, values, costs, number_of_items)
        self.neighbor_distance = neighbor_distance
        self.T = T
        self.cool = cool

    def solve(self) -> [int]:
        self.generate_random_list()
        self.best_set = self.number_of_items

        while self.T > 0.0001:
            self.generate_random_list()
            if self.best_score < self.current_score:
                self.best_set = self.number_of_items
            else:
                p = pow(
                        math.e,
                        -abs(self.current_score - self.best_score) / self.T)
                if random.random() < p:
                    self.best_set = self.number_of_items

            self.logger.debug('{} {}'.format(self.T, self.best_score))
            self.T *= self.cool
        return self.best_set

    @property
    def best_score(self):
        (_, _, total) = objective(
                self.capasity, self.values, self.costs, self.best_set)
        return total

    @property
    def current_score(self):
        (_, _, total) = self.__objenctive()
        return total

    def __objenctive(self) -> (True, int, int):
        return objective(
                self.capasity,
                self.values,
                self.costs,
                self.number_of_items)

    def generate_random_list(self):
        for i in range(1, 50):
            self.__change()

    def __change(self):

        for i in range(0, self.neighbor_distance):
            n = random.randint(0, len(self.number_of_items) - 1)
            self.number_of_items[n] += 1

        is_ok = False
        while not is_ok:
            (is_ok, cost, total_value) = self.__objenctive()
            remove_n = random.randint(0, len(self.number_of_items) - 1)
            if self.number_of_items[remove_n] != 0:
                self.number_of_items[remove_n] -= 1


if __name__ == '__main__':
    # Parameters
    values = [120, 130, 80, 100, 250, 185]
    costs = [10, 12, 7, 9, 21, 16]
    number_of_items = [0 for i in range(0, len(values))]
    capasity = 100

    # for logging
    # from logging import DEBUG
    # basicConfig(level=DEBUG)
    from logging import INFO
    basicConfig(level=INFO)

    sa = SimulatedAnealing(
            capasity, values, costs, number_of_items, 2, 10000, 0.99)
    best_result_of_sa = sa.solve()
    best_cost = objective(capasity, values, costs, best_result_of_sa)

    print('best conbination: ', best_result_of_sa)
    print('best cost:', best_cost)
