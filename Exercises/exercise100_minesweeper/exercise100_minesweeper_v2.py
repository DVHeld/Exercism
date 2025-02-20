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
        minefield_length = len(minefield[0])
        minefield_height = len(minefield)
        rows = []
        for row in minefield:
            if match(r"[^\ *]", row) or len(row) != minefield_length:
                raise ValueError("The board is invalid with current input.")
            rows.append([cell if cell == "*" else 0 for cell in row])
        for row_no, row in enumerate(rows):
            for col_no, cell in enumerate(row):
                if cell == "*":
                    for direction in directions:
                        x_pos = col_no + direction[0]
                        y_pos = row_no + direction[1]
                        if 0 <= y_pos < minefield_height and\
                        0 <= x_pos < minefield_length and\
                        isinstance(rows[y_pos][x_pos], int):
                            rows[y_pos][x_pos] += 1
        return [''.join([str(cell) if cell else " " for cell in row]) for row in rows]
    return minefield
