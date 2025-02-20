"""Spiral Matrix exercise"""

def spiral_matrix(size):
    """Creates a spiral matrix of the given size.
 
    :param int size: The size.
    :raises TypeError: Raised when the input is not an integer.
    :raises ValueError: Raised when the value is negative.
    :return list[list[int]]: The spiral matrix.
    """

    if not isinstance(size, int) and size is not None:
        raise TypeError("Input must be an integer.")
    if size < 0:
        raise ValueError("Input must be non-negative.")

    matrix = [[0 for _ in range(size)] for _ in range(size)]
    number = 1
    y_pos = 0
    if size:
        for rotation in range(1, 2*size):
            for x_pos, cell in enumerate(matrix[y_pos]):
                if not cell:
                    matrix[y_pos][x_pos] = number
                    number += 1
            matrix = [list(item) for item in zip(*matrix)][::-1]
            y_pos = y_pos+1 if rotation%4 == 0 else y_pos
        while matrix[0][0] != 1:
            matrix = [list(item) for item in zip(*matrix[::-1])]
    return matrix
