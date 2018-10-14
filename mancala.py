"""
A game state is represented by a tuple.  The leading elements of
the tuple are the number of stones in each position, from position 0
to the final position. The last element of the tuple is the current
player, either 0 or 1.
"""

class MancalaGame:

    def __init__(self, size=6, count=4):
        self.size = size
        self.count = count

    def initial(self):
        """
        Return the initial game state.
        """
        return ((self.count,) * self.size + (0,)) * 2 + (0,)

    # def player(self, state):
    #     """
    #     Return the current player in the given game state.
    #     """
    #     return state[-1]

    def actions(self, state):
        """
        Return a list of all actions available in the current game state.
        Each action is the position number of a non-empty small position
        on the current player's half of the board.
        """

        action_list = []
        if 0 == state[-1]:
            tup_player = state[0:5]
            count = 0
            for val in tup_player:
                if 0 != val:
                    action_list.append(count)
                count += 1
        elif 1 == state[-1]:
            tup_player = state[7:12]
            count = 7
            for val in tup_player:
                if 0 != val:
                    action_list.append(count)
                count += 1
        else:
            raise (Exception("Invalid player."))

        return action_list


    def result(self, state, action):
        """
        Return the new game state that results from playing the given
        action in the given state.  Be sure to account for the special
        cases where a player's last stone lands in one of their own small
        positions, and when a player's last stone lands in their own mancala.
        """

        # get moves
        moves = state[action]
        # get list of possible next steps and their values as enumerate
        board = list(enumerate(list(state)))
        if 0 == state[-1]:
            board.remove(len(board)-1)
            board.remove(len(board)-2)
        else:
            board.remove(len(board)-1)
            board.remove(self.size+1)

        # for each enumerate, do rotation+add score from starting position till end of action
        # mostly as mod of size of board
        pivot = 0
        for i, j in enumerate(board):
            if j[0] == action:
                pivot = i

        board[pivot][1] = 0
        i = 1
        while i != (moves+1):
            if pivot == len(board):
                pivot = -1
            pivot += 1
            board[pivot][1] += 1
            i += 1

        # Add the other players mancala back to the board
        if state[-1] == 0:
            board.insert(((self.size * 2) + 1), state[(self.size * 2) + 1])
        else:

        # at the position we end up on board, do the following
        if (board[pivot][1]) == 1:
            board.insert(len(board), ((len(state)-1), state[-1]))

            if
            board += board[(self.size * 2) - pivot][1]

    def is_over(self, state):
        """
        Return True if the game is over in the given state, False otherwise.
        The game is over if either player has no stones left in their small positions.
        """

        tup_sum = 0
        if 0 == state[-1]:
            tup = state[0:5]
        elif 1 == state[-1]:
            tup = state[7:12]
        else:
            raise (Exception("Invalid player."))

        for val in tup:
            tup_sum += val

        if 0 == tup_sum:
            return True
        else:
            return False

    def player_sum(self, state):
        res = []

        tup0 = state[0:5]
        player_sum = 0
        for val in tup0:
            player_sum += val
        res.insert(0, player_sum)

        tup1 = state[7:12]
        player_sum = 0
        for val in tup1:
            player_sum += val
        res.insert(1, player_sum)

        return res

    def score(self, state):
        """
        Return the score in the current state, from player 0's perspective.
        If the game is over and one player still has stones on their side,
        those stones are added to that player's score.
        """

        score0 = 0
        score1 = 0

        if self.is_over(state):
            res = self.player_sum(state)
            score0 = res[0]
            score1 = res[1]

        score = (state[6]+score0) - (score1+state[13])

        return score

    def string(self, state):
        """
        Display current state as a game board.  The current player's mancala
        is marked with *.
        """
        z = self.size
        s = " ".join(["%2d" % m for m in state[-2:z:-1]] + [" *" if state[-1] == 0 else "  "])
        s += "\n"
        s += " ".join(["  " if state[-1] == 0 else " *"] + ["%2d" % m for m in state[:(z + 1)]])
        return s


if __name__ == "__main__":
    """
    Scratch pad for informal tests
    """

    # mg = MancalaGame(size=3, count=2)
    mg = MancalaGame()

    s = mg.initial()
    # a = mg.actions(s)
    print(mg.string(s))
    print(s)
    # print(a)
    # print("Is over: %s" % mg.is_over(s))
    # print("Score = %d" % mg.score(s))
    print("")

    # s = mg.result(s, 2)
    # a = mg.actions(s)
    # print(mg.string(s))
    # print(s)
    # print(a)
    # print("Is over: %s" % mg.is_over(s))
    # print("Score = %d" % mg.score(s))
    # print("")

