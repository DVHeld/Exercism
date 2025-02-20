"""Pascal's Triangle exercise"""

def _number(row, index, /):

    if row != index and index:
        return _number(row - 1, index - 1) + _number(row - 1, index)
    return 1

def _row(row, index, /):

    if row != index:
        return [_number(row, index), *_row(row, index + 1)]
    return [1]

def _rows(row_count, /):

    if row_count:
        return [*rows(row_count - 1), _row(row_count - 1, 0)]
    return []

def rows(row_count, /):
    """Generates Pascal's triangle using recursion.
 
    :param int row_count: The amount of rows to be generated.
    :raises ValueError: Raised when there is no input.
    :raises TypeError: Raised when the row count is not an integer
    :raises ValueError: Raised when the row count input is negative.
    :return list[list[int]]: Pascal's triangle as a list of rows of integers.
    """

    if row_count is None:
        raise ValueError("Missing input.")
    if not isinstance(row_count, int):
        raise TypeError("Row count must be an integer.")
    if row_count < 0:
        raise ValueError("number of rows is negative")

    return _rows(row_count)
