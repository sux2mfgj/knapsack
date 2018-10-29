from abc import *
from functools import reduce
import copy

class Solver(ABC):

    def __init__(self, capasity, values, costs, number_of_items):
        self.capasity = capasity
        self.values = values
        self.costs = costs
        self.number_of_items = number_of_items

    @abstractmethod
    def solve(self):
        pass

def objective(capasity, values, costs, number_of_items):
    total_value = reduce(
            lambda s, x: s + x[0] * x[1],
            zip(values, number_of_items),
            0)
    cost = reduce(lambda s, x: s + x[0] * x[1],
            zip(costs, number_of_items), 0)

    return (capasity >= cost, total_value)
