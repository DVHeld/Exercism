"""Connect exercise"""

from re import match

class ConnectGame:
    """A connect game. Stores the current board and can check if there's a winner."""

    def __init__(self, board=""):

        if board is None:
            raise ValueError("No input.")
        if not isinstance(board, str):
            raise TypeError("Input must be a string.")
        if match(r"[^ \.OX\n]", board):
            raise ValueError("Invalid character in board string.")

        self.board_map = []
        for row_no, row in enumerate(board.replace(" ", "").splitlines()):
            self.board_map.append([])
            for cell in row:
                self.board_map[row_no].append(cell)

    def get_winner(self):
        """Analyzes the current board to determine the winner, if there is one.
        
        :return str: The winner."""

        board = self.board_map
        winner = ""
        board_length = len(board[0])
        board_height = len(board)
        for cell_no in range(board_length):
            if board[0][cell_no] == "O":
                board[0][cell_no] = "A"
                if board_height == 1:
                    winner += "O"
        for cell_no in range(board_height):
            if board[cell_no][0] == "X":
                board[cell_no][0] = "B"
                if board_length == 1:
                    winner += "X"
        someone_advanced = True
        while someone_advanced:
            someone_advanced = False
            for row_no in range(board_height):
                for col_no in range(board_length):
                    adjacent = False
                    if board[row_no][col_no] == "O":
                        if row_no != 0:
                            adjacent = board[row_no-1][col_no] == "A"
                            if col_no != board_length-1:
                                adjacent = adjacent if adjacent\
                                                    else board[row_no-1][col_no+1] == "A"
                        if row_no != board_height-1:
                            adjacent = adjacent if adjacent else board[row_no+1][col_no] == "A"
                            if col_no != 0:
                                adjacent = adjacent if adjacent\
                                                    else board[row_no+1][col_no-1] == "A"
                        if col_no != board_length-1:
                            adjacent = adjacent if adjacent else board[row_no][col_no+1] == "A"
                        if col_no != 0:
                            adjacent = adjacent if adjacent else board[row_no][col_no-1] == "A"
                        if adjacent:
                            if row_no == board_height-1:
                                winner += "O"
                            board[row_no][col_no] = "A"
                            someone_advanced = True
                            adjacent = False
                    if board[row_no][col_no] == "X":
                        if row_no != 0:
                            adjacent = board[row_no-1][col_no] == "B"
                            if col_no != board_length-1:
                                adjacent = adjacent if adjacent\
                                                    else board[row_no-1][col_no+1] == "B"
                        if row_no != board_height-1:
                            adjacent = adjacent if adjacent else board[row_no+1][col_no] == "B"
                            if col_no != 0:
                                adjacent = adjacent if adjacent\
                                                    else board[row_no+1][col_no-1] == "B"
                        if col_no != board_length-1:
                            adjacent = adjacent if adjacent else board[row_no][col_no+1] == "B"
                        if col_no != 0:
                            adjacent = adjacent if adjacent else board[row_no][col_no-1] == "B"
                        if adjacent:
                            board[row_no][col_no] = "B"
                            if col_no == board_length-1:
                                winner += "X"
                            someone_advanced = True
                            adjacent = False
        return winner
