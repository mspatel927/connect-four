#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ a data type (object) to represent an intelligent computer
        player of Connect Four that will look ahead some number
        of moves to assess the impact of every possible move
        for its next move and assigns a score to each possible move
        and chooses its next move as the one with the highest score.
        Possible column scores are -1 (full column), 0 (will result
        in a loss for the player at some point in the lookahead), 100
        (will result in a win for the player during the lookahead), or
        50 (will result in neither a win nor a loss in the lookahead)
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object by inheriting
            attributes from the Player class and initializing
            attributes for tiebreak and lookahead
            attribute tiebreak: a string specifying the player's
                                tiebreaking strategy
            attribute lookahead: an integer specifying how many
                                 moves that player looks ahead in
                                 order to evaluate possible moves
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ returns a string representing an AIPlayer object
        """
        s = 'Player' + ' ' + str(self.checker) + ' '
        s += '(' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
        return s

    def max_score_column(self, scores):
        """ takes the input (list) scores containing a score for
            each column of the board and returns the index of the
            column with the maximum score (using the appropriate
            tiebreaking strategy as necessary)
        """
        max_score = max(scores)
        indices = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                indices += [i]
        if self.tiebreak == 'LEFT':
            return indices[0]
        if self.tiebreak == 'RIGHT':
            return indices[-1]
        if self.tiebreak == 'RANDOM':
            return random.choice(indices)

    def scores_for(self, board):
        """ determines the called AIPlayer's scores for the columns
            in the called Board object and returns a list
            containing one score for each column
        """
        scores = [50] * board.width

        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker) == True:
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(board)
                if max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 50:
                    scores[col] = 50
                board.remove_checker(col)
        return scores

    def next_move(self, board):
        """ returns the called AIPlayer's judgement of its best
            possible move
        """
        self.num_moves += 1

        scores = self.scores_for(board)
        best_move = self.max_score_column(scores)
        return best_move
            
