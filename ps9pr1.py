#
# Problem Set 9, Problem 1
#
# A Connect Four Board class

class Board:
    """ a data type (object) for a Connect Four board with
        arbitrary dimensions
    """
    def __init__(self, height, width):
        """ constructs a new Board object by initializing the
            attributes of height, width, and slots
            attribute height: the number of rows in the board
            attribute width: the number of columns in the board
            attribute slots: a reference to a two-dimensional list with
                             height rows and width columns used to store
                             the current contents of the board
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    def __repr__(self):
        """ returns a string representation of a Board object
        """
        s = ''
        
        for row in range(self.height):
            s += '|'

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'

        s += '-' * self.width * 2 + '-'
        s += '\n'
        
        for col in range(self.width):
            s += ' ' + str(col % 10)

        s += '\n'   
        return s
    
    def add_checker(self, checker, col):
        """ adds the checker specified by input checker to the
            column number of the Board (called by self) specified
            by input col to the appropriate row
            input checker: a one-character string that specifies
                           which checker to add to the board (either 'X' or 'O')
            input col: an integer specifying the index of the column
                       to which the checker should be added to
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        row = 0
        while self.slots[row][col] == ' ':
            if row >= (self.height - 1):
                row += 1
                break
            row += 1

        self.slots[row - 1][col] = checker

    def reset(self):
        """ resets the called Board object by setting all slots
            to contain a space character
        """
        self.slots = [[' '] * self.width for row in range(self.height)]

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'
    
        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
    
            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the
            column specified by col on the called Board object,
            and returns False otherwise
            input col: an integer specifying the index of the column
                       that will be checked
        """
        if col < 0 or col > self.width - 1:
            return False
        if self.slots[0][col] != ' ':
            return False
        else:
            return True

    def is_full(self):
        """ returns True if the called Board object is completely
            full of checkers, and returns False otherwise
        """
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        return True

    def remove_checker(self, col):
        """ removes the top checker from the column specified by col
            of the called Board object (but does nothing if the
            column is empty)
            input col: an integer specifying the index of the column
                       of which a checker will removed
        """
        if self.slots[self.height - 1][col] != ' ':
            row = 0
            while self.slots[row][col] == ' ':
                row += 1
            self.slots[row][col] = ' '

    def is_win_for(self, checker):
        """ returns True if there are four consecutive slots 
            containing the input checker on the board, and otherwise
            returns False
            input checker: either 'X' or 'O'
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False
    
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
    
        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a downward (left to right) diagonal win
            for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        """ Checks for an upward (left to right) diagonal win
            for the specified checker
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False
