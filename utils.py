from abc import ABC, abstractmethod
import copy
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


def objective(capasity, values, costs, number_of_items):
    total_value = reduce(
            lambda s, x: s + x[0] * x[1],
            zip(values, number_of_items),
            0)
    cost = reduce(lambda s, x: s + x[0] * x[1], zip(costs, number_of_items), 0)

    return (capasity >= cost, cost, total_value)
