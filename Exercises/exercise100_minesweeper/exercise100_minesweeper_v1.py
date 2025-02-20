"""Minesweeper exercise"""

from re import match

def annotate(minefield):
    """Adds the mine count numbers to a minesweeper board that is missing them.
 
    :param list[str] minefield: The board. It must be formatted as a list of strings, each string
                                representing a row and each character representing the contents
                                of a cell. Valid contents are ' ' or '*'.
    :raises ValueError: Raised when the input is left blank.
    :raises ValueError: Raised when there are invalid characters or the rows are of different
                        lengths.
    :return list[str]: The board with the mine count numbers added.
    """

    directions = (
        (-1,-1), ( 0,-1), ( 1,-1),
        (-1, 0),          ( 1, 0),
        (-1, 1), ( 0, 1), ( 1, 1)
        )

    if minefield is None:
        raise ValueError("No input.")

    if minefield:
        row_len = len(minefield[0])
        for row_no, row_str in enumerate(minefield):
            if match(r"[^\ *]", row_str) or len(row_str) != row_len:
                raise ValueError("The board is invalid with current input.")
            row = list(row_str)
            for col_no, cell in enumerate(row):
                if cell == " ":
                    count = 0
                    for direction in directions:
                        x_pos = col_no + direction[0]
                        y_pos = row_no + direction[1]
                        if 0 <= y_pos < len(minefield) and\
                        0 <= x_pos < len(row) and\
                        minefield[y_pos][x_pos] == "*":
                            count += 1
                        if count:
                            row[col_no] = str(count)
            minefield[row_no] = ''.join(row)
    return minefield
