import copy
from logging import basicConfig

from utils import Solver, objective, generate_random_result


class HillClimbing(Solver):
    def __init__(self, capasity, values, costs, number_of_items,
                 neighbor_distance):
        super().__init__(capasity, values, costs, number_of_items)
        self.neighbor_distance = neighbor_distance

    def solve(self) -> [int]:
        self.best_set = generate_random_result(
            self.capasity, self.values, self.costs,
            copy.deepcopy(self.number_of_items))
        #         self.best_set = self.number_of_items

        items_num = len(self.best_set)
        last_best_score = 0
        self.logger.debug('inital score: {}'.format(self.best_score))
        self.logger.debug('inital set: {}'.format(self.best_set))
        while last_best_score != self.best_score:
            neighbor_results = [[
                1 if x == y else 0 for x in range(0, items_num)
            ] for y in range(0, items_num)]

            last_best_score = self.best_score
            neighbor_results.extend(
                get_neighbor_results(items_num, self.neighbor_distance,
                                     copy.deepcopy(neighbor_results)))
            for xs in neighbor_results:

                updated_list = list(map(lambda x, y: x + y, self.best_set, xs))
                if self.best_score < self.__current_score(updated_list):
                    self.best_set = updated_list
                    self.logger.debug('update best {} {}'.format(
                        self.best_score, self.best_set))

                # updated_list = list(
                #       map(lambda x, y: 0 if x - y else x - y
                #           , self.best_set, xs))
                # if self.best_score < self.__current_score(l):
                #    self.best_set = updated_list

            self.logger.debug('best_score: {}'.format(self.best_score))
        return self.best_set

    def __current_score(self, li):
        (is_valid, _, total) = objective(self.capasity, self.values,
                                         self.costs, li)
        if is_valid:
            self.logger.debug('valid score: {} {}'.format(total, li))
            return total
        else:
            return 0


def get_neighbor_results(ln, n, d) -> [[int]]:
    result = []
    for i in range(0, ln):
        local_result = []
        for j in range(0, i + 1):
            tmp = copy.deepcopy(d[i])
            tmp[j] += 1
            if (n - 1) > 0:
                local_result.append(copy.deepcopy(tmp))
        if (n - 2) > 0:
            result.extend(
                get_neighbor_results(i + 1, n - 1,
                                     copy.deepcopy(local_result)))
        else:
            result.extend(copy.deepcopy(local_result))

    return result


if __name__ == '__main__':
    # Parameters
    values = [120, 130, 80, 100, 250, 185]
    costs = [10, 12, 7, 9, 21, 16]
    number_of_items = [0 for i in range(0, len(values))]
    capasity = 100

    # for logging
    from logging import DEBUG
    basicConfig(level=DEBUG)

    hc = HillClimbing(capasity, values, costs, number_of_items, 4)
    best_result_of_sa = hc.solve()

    best_cost = objective(capasity, values, costs, best_result_of_sa)

    print('best conbination: ', best_result_of_sa)
    print('best cost:', best_cost)
    # ln = 5
    # result_list = [
    #       [1 if x == y else 0 for x in range(0, ln)] for y in range(ln)]
    # result_list.extend(
    #       get_neighbor_results(ln, 3, copy.deepcopy(result_list)))
    # for xs in result_list:
    #    print(' '.join(map(str, xs)))
