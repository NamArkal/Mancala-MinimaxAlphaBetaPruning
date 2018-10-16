from minimax import *
from mancala import *
from nr import *

game_size = [(2, 1), (3, 1), (3, 2), (4, 2), (5, 3), (6, 4)]
max_depth = [1, 2, 3, 4, 5, 6, 7, 8]
moves = 10
verbose = True

for (i, j) in game_size:
    mg = MancalaGame(size=i, count=j)
    for k in max_depth:
        print ("***** calculating play minimax *****")
        alg = lambda game, state: minimax(game, state, max_depth=k)
        fs_ab = play(mg, alg, moves=moves, verbose=verbose)
        print ("***** calculating node count *****")
        _, _, nc = minimax(mg, mg.initial(), max_depth=k)
        b0 = (nc + 1) ** (1. / k)
        b = newton(b0, g, dg, nc, k)
        print ("Branching factor: ", b[-1])
