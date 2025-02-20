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
        self.board_map = [[cell for cell in row] for row in board.replace(" ", "").splitlines()]

    def get_winner(self):
        """Analyzes the current board to determine the winner, if there is one.
        
        :return str: The winner."""

        board = self.board_map
        winner = ""
        board_length = len(board[0])
        board_height = len(board)
        players = (("O", "A", board_length, board_height), ("X", "B", board_height, board_length))
        for player in players:
            for cell_no in range(player[2]):
                if (board[0][cell_no] if player[0] == "O" else board[cell_no][0]) == player[0]:
                    if player[0] == "O":
                        board[0][cell_no] = player[1]
                    else:
                        board[cell_no][0] = player[1]
                    if player[3] == 1:
                        winner += player[0]
        someone_advanced = True
        while someone_advanced and not winner:
            someone_advanced = False
            for row_no in range(board_height):
                for col_no in range(board_length):
                    for player in players:
                        adjacent = False
                        if board[row_no][col_no] == player[0]:
                            if row_no != 0:
                                adjacent = board[row_no-1][col_no] == player[1]
                                if col_no != board_length-1:
                                    adjacent = adjacent if adjacent else board[row_no-1][col_no+1] == player[1]
                            if row_no != board_height-1:
                                adjacent = adjacent if adjacent else board[row_no+1][col_no] == player[1]
                                if col_no != 0:
                                    adjacent = adjacent if adjacent else board[row_no+1][col_no-1] == player[1]
                            if col_no != board_length-1:
                                adjacent = adjacent if adjacent else board[row_no][col_no+1] == player[1]
                            if col_no != 0:
                                adjacent = adjacent if adjacent else board[row_no][col_no-1] == player[1]
                            if adjacent:
                                if (row_no if player[0] == "O" else col_no) == player[3]-1:
                                    winner += player[0]
                                board[row_no][col_no] = player[1]
                                someone_advanced = True
                                adjacent = False
        return winner
