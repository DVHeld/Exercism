"""Matrix exercise"""

class Matrix:
    """A matrix."""

    def __init__(self, matrix_string):

        self.matrix = []
        matrix_lines = matrix_string.splitlines()
        for line_number, line in enumerate(matrix_lines):
            self.matrix.append([])
            for element in line.split():
                self.matrix[line_number].append(int(element))

    def row(self, row):
        """Returns the given row.
 
        :param int row: The row number to be retrieved.
        :raises TypeError: Raised when the input is not an integer.
        :raises ValueError: Raised when the input is outside the matrix's range.
        :return list[int]: The row.
        """

        if not isinstance(row, int):
            raise TypeError("Input must be an integer.")
        if len(self.matrix) < row-1 < 0:
            raise ValueError("Row number out of range.")

        return self.matrix[row-1]

    def column(self, column):
        """Returns the given column.
 
        :param int column: The column number to be retrieved.
        :raises TypeError: Raised when the input is not an integer.
        :raises ValueError: Raised when the input is outside the matrix's range.
        :return list[int]: The column.
        """

        if not isinstance(column, int):
            raise TypeError("Input must be an integer.")
        if len(self.matrix[0]) < column-1 < 0:
            raise ValueError("Column number out of range.")

        return [self.matrix[row][column-1] for row in range(len(self.matrix))]
