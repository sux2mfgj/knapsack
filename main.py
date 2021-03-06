from logging import basicConfig
import argparse

from utils import objective
from simulated_annealing import SimulatedAnealing
from hill_climbing import HillClimbing
# from ta import TabuSearch
from iterative_local_search import IterativeLocalSearch
# from gls import GuidedLocalSearch

if __name__ == '__main__':

    # parameters for simulation
    values = [120, 130, 80, 100, 250, 185]
    costs = [10, 12, 7, 9, 21, 16]
    number_of_items = [0 for i in range(0, len(values))]
    capasity = 65
    neighbor_distance = 2

    # prepare solver dictionary
    sa = SimulatedAnealing(capasity, values, costs, number_of_items,
                           neighbor_distance, 10000, 0.99)
    hc = HillClimbing(capasity, values, costs, number_of_items,
                      neighbor_distance)
    # ta = TabuSearch(...)
    ils = IterativeLocalSearch(capasity, values, costs, number_of_items, neighbor_distance)
    # gls = GuidedLocalSearch(...)
    implemented_algorithms = {
        'sa': sa,
        'hc': hc,
        # 'ta': ta
        'ils': ils,
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
