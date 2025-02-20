"""Queen Attack exercise"""

BOARD_DIMENSIONS = (8,8)

class Queen:
    """A queen.
 
    :raises ValueError: Raised when the row is not positive.
    :raises ValueError: Raised when the row is outside the board's boundaries.
    :raises ValueError: Raised when the column is not positive.
    :raises ValueError: Raised when the column is outside the board's boundaries.
    :raises ValueError: Raised when the given position is already occupied by another piece.
    """

    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row > BOARD_DIMENSIONS[0]-1:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > BOARD_DIMENSIONS[1]-1:
            raise ValueError("column not on board")

        self.position = (row, column)

    def can_attack(self, another_queen):
        """Determines if this queen can attack the given piece.
 
        Queens can attack pieces that are either in the same row, in the same column,
        or in the same diagonal.
 
        :param Queen another_queen: The target piece.
        :return bool: True if the piece can be attacked, False otherwise.
        """

        if self.position == another_queen.position:
            raise ValueError("Invalid queen position: both queens in the same square")

        same_row = self.position[0] == another_queen.position[0]
        same_column = self.position[1] == another_queen.position[1]
        same_diagonal = abs(self.position[0]-another_queen.position[0]) ==\
                        abs(self.position[1]-another_queen.position[1])
        return same_row or same_column or same_diagonal
