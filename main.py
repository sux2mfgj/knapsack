from utils import objective
from sa import SimulatedAnealing
# from ta import TabuSearch
# from ils import IteratedLocalSearch
# from gls import GuidedLocalSearch

import sys


if __name__ == '__main__':

    alg_type = None
    if len(sys.argv) == 2:
        alg_type = sys.argv[1]
    else:
        sys.stderr.write('A argument is required.\n')
        sys.stderr.write('e.g.\n$ python {} sa\n'.format(sys.argv[0]))
        sys.exit(1)

    values = [120, 130, 80, 100, 250, 185]
    costs = [10, 12, 7, 9, 21, 16]
    number_of_items = [0 for i in range(0, len(values))]
    capasity = 65

    sa = SimulatedAnealing(
            capasity, values, costs, number_of_items, 2, 10000, 0.99)
    # ta = TabuSearch(...)
    # ils = IteratedLocalSearch(...)
    # gls = GuidedLocalSearch(...)
    implemented_algorithms = {
            'sa': sa
            # 'ta': ta
            # 'ils': ils
            # 'gls': gls
            }

    alg = implemented_algorithms.get(alg_type)
    if not alg:
        sys.stderr.write(
                'the algorithm "{}" is not implemented yet\n'.format(alg_type))
        sys.exit(2)

    best_result_of_sa = alg.solve()
    best_cost = objective(capasity, values, costs, best_result_of_sa)

    print('[{}]'.format(alg.__class__.__name__))
    print('best conbination: ', best_result_of_sa)
    print('best cost:', best_cost)
