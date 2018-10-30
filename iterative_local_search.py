from utils import Solver, objective


class IterativeLocalSearch(Solver):
    def __init__(self, capasity, values, costs, number_of_items,
            neighbor_distance):
        super().__init__(capasity, values, costs, number_of_items)
        self.neighbor_distance = neighbor_distance

    def solve(self):
        return self.number_of_items
