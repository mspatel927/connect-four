#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player:
    """ a data type (object) to represent a player of the Connect
        Four game
    """
    def __init__(self, checker):
        """ constructs a new Player object by initializing the
            attributes for checker and num_moves
            checker: a one-character string representing the
                     gamepiece for the player, specified by the
                     input checker
            num_moves: an integer storing how many moves the
                       player has made so far (initially 0)
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns a string representation of a Player object
            (indicating which checker the Player object is using)
        """
        s = 'Player' + ' ' + str(self.checker)
        return s

    def opponent_checker(self):
        """ returns a one-character string representing the checker
            of the Player object's opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        """ returns the column where the player wants to make the
            next move by asking the user to enter a column number
            representing where the user wants to place a checker
            on the board (until a valid column number is given)
            input board: a Board object
        """
        self.num_moves += 1

        while True:
            col = int(input('Enter a column: '))
            if board.can_add_to(col) == True:
                return col
            else:
                print('Try again!')
