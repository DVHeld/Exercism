"""Go Counting exercise"""

BLACK = "B"
WHITE = "W"
NONE = " "

class Board:
    """Count territories of each player in a Go game.
 
    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):

        if not isinstance(board, list):
            raise TypeError("Board must be a list.")

        self._board_length = len(board[0])
        self._board_heigth = len(board)
        self._board = ["*" * (self._board_length+2)]

        for row in board:
            if not isinstance(row, str):
                raise TypeError("Rows must be strings.")
            for space in row:
                if space not in " WB":
                    raise ValueError("Invalid space token. Valid tokens are ' ', 'W' and 'B'.")
            self._board.append("*" + row + "*")
        self._board.append("*" * (self._board_length+2))

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board.
 
        Args:
            x (int): Column on the board
            y (int): Row on the board
 
        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
            """

        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Coordinates must be integers.")
        if x < 0 or x >= self._board_length or y < 0 or y >= self._board_heigth:
            raise ValueError('Invalid coordinate')

        x += 1
        y += 1
        if self._board[y][x] != NONE:
            return (NONE, set())
        directions = (
                 ( 0,-1),
        (-1, 0),          ( 1, 0),
                 ( 0, 1)
        )
        spaces = [(x,y)]
        stone = False

        for space in spaces:
            for direction in directions:
                pos = (space[0]+direction[0], space[1]+direction[1])
                if pos not in spaces and self._board[pos[1]][pos[0]] == NONE:
                    spaces.append((pos[0], pos[1]))
                if self._board[pos[1]][pos[0]] not in "* ":
                    if stone != NONE:
                        if not stone and self._board[pos[1]][pos[0]] == BLACK:
                            stone = BLACK
                        elif not stone and self._board[pos[1]][pos[0]] == WHITE:
                            stone = WHITE
                        elif self._board[pos[1]][pos[0]] != stone:
                            stone = NONE
        territory = set()
        for space in spaces:
            territory.add((space[0]-1, space[1]-1))
        return (NONE if not stone else stone, territory)

    def territories(self):
        """Find the owners and the territories of the whole board
 
        Args:
            none
 
        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """

        result = {WHITE : set(), BLACK: set(), NONE: set()}
        for row_no, row in enumerate(self._board):
            for col_no, space in enumerate(row):
                if space not in "WB*" and\
                   (col_no-1, row_no-1) not in (result[WHITE] | result[BLACK] | result[NONE]):
                    stone, territory = self.territory(col_no-1, row_no-1)
                    result[stone] |= territory
        return result
