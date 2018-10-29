from logging import basicConfig
import argparse

from utils import objective
from sa import SimulatedAnealing
# from ta import TabuSearch
# from ils import IteratedLocalSearch
# from gls import GuidedLocalSearch

if __name__ == '__main__':

    # parameters for simulation
    values = [120, 130, 80, 100, 250, 185]
    costs = [10, 12, 7, 9, 21, 16]
    number_of_items = [0 for i in range(0, len(values))]
    capasity = 65

    # prepare solver dictionary
    sa = SimulatedAnealing(capasity, values, costs, number_of_items, 2, 10000,
                           0.99)
    # ta = TabuSearch(...)
    # ils = IteratedLocalSearch(...)
    # gls = GuidedLocalSearch(...)
    implemented_algorithms = {
        'sa': sa
        # 'ta': ta
        # 'ils': ils
        # 'gls': gls
    }

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--debug', action='store_const', const=True, default=False)
    parser.add_argument(
        '-a',
        '--algorithm',
        action='store',
        default='sa',
        type=str,
        choices=implemented_algorithms.keys())
    args = parser.parse_args()

    # configuration for logging
    if args.debug:
        from logging import DEBUG
        basicConfig(level=DEBUG)
    else:
        from logging import INFO
        basicConfig(level=INFO)

    alg = implemented_algorithms.get(args.algorithm)

    best_result_of_sa = alg.solve()
    best_cost = objective(capasity, values, costs, best_result_of_sa)

    print('[{}]'.format(alg.__class__.__name__))
    print('best conbination: ', best_result_of_sa)
    print('best cost:', best_cost)
