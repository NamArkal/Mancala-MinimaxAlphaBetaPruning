from minimax import *
from mancala import *

pairs = [(2, 1), (3, 1), (3, 2), (4, 2), (5, 3), (6, 4)]
max_depth = [1, 2, 3, 4, 5, 6, 7, 8]
moves = 10
verbose = True

# for (i, j) in pairs:
#     mg = MancalaGame(size=i, count=j)
#     for x in max_depth:
#         fs = play_minimax(mg, max_depth=x, moves=moves, verbose=verbose)

for (i, j) in pairs:
    mg = MancalaGame(size=i, count=j)
    for x in max_depth:
        alg = lambda game, state: minimax_ab(game, state, max_depth=x)
        fs_ab = play(mg, alg, moves=moves, verbose=verbose)

# print("minimax: %f" % fs)
# print("ab: %f" % fs_ab)
