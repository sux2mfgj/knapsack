from abc import ABC, abstractmethod
import copy
import random
from functools import reduce
from logging import getLogger


class Solver(ABC):
    def __init__(self, capasity, values, costs, number_of_items):
        self.capasity = capasity
        self.values = values
        self.costs = costs
        self.number_of_items = number_of_items
        self.best_set = number_of_items
        self.logger = getLogger(__name__)

    @abstractmethod
    def solve(self):
        pass

    @property
    def best_set(self):
        return self._best_set

    @best_set.setter
    def best_set(self, number_of_items):
        self._best_set = copy.deepcopy(number_of_items)

    @property
    def best_score(self):
        (_, _, total) = objective(self.capasity, self.values, self.costs,
                                  self.best_set)
        return total

    @property
    def current_score(self):
        (_, _, total) = self.objective(self.capasity, self.values, self.costs,
                                       self.number_of_items)
        return total


def objective(capasity, values, costs, number_of_items):
    total_value = reduce(lambda s, x: s + x[0] * x[1],
                         zip(values, number_of_items), 0)
    cost = reduce(lambda s, x: s + x[0] * x[1], zip(costs, number_of_items), 0)

    return (capasity >= cost, cost, total_value)


def generate_random_result(capasity, values, costs, number_of_items):
    for _ in range(0, 50):
        n = random.randint(0, len(number_of_items) - 1)
        number_of_items[n] += 1
    is_ok = False
    while not is_ok:
        (is_ok, cost, total_value) = objective(capasity, values, costs,
                                               number_of_items)
        remove_n = random.randint(0, len(number_of_items) - 1)
        if number_of_items[remove_n] != 0:
            number_of_items[remove_n] -= 1

    return number_of_items
