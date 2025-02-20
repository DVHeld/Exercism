"""OCR Numbers"""

def convert(input_grid):
    """Transforms numbers in binary font to plaintext numbers.
 
    Lines in multiline inputs are separated by a comma.
 
    :param list[str] input_grid: The binary font representation of numbers.
    :raises ValueError: Raised when there is no input.
    :raises TypeError: Raised when the input is not a list.
    :raises ValueError: Raised when amount of lines on the input is not a multiple of 4.
    :raises ValueError: Raised when the amount of columns in the input is not a multiple of 3.
    :raises TypeError: Raised when a line is not a string.
    :raises ValueError: Raised when there are extraneous characters in the input.
    :return str: The numbers.
    """

    def _get_number(number_grid):

        numbers = (
            [[2,2,2], [[0,1],[2,0],[2,1],[0,0]], 1], #0
            [[0,0,2], [[0,0],[1,0],[1,0],[0,0]], 0], #1
            [[1,3,1], [[0,1],[1,1],[1,1],[0,0]], 0], #2
            [[0,3,2], [[0,1],[1,1],[1,1],[0,0]], 0], #3
            [[1,1,2], [[0,0],[2,1],[1,0],[0,0]], 1], #4
            [[1,3,1], [[0,1],[1,1],[1,1],[0,0]], 1], #5
            [[2,3,1], [[0,1],[1,1],[2,1],[0,0]], 1], #6
            [[0,1,2], [[0,1],[1,0],[1,0],[0,0]], 0], #7
            [[2,3,2], [[0,1],[2,1],[2,1],[0,0]], 1], #8
            [[1,3,2], [[0,1],[2,1],[1,1],[0,0]], 1]  #9
        )
        number = [[], [], 0]
        columns = tuple(zip(*number_grid))

        for column in columns:
            number[0].append(column.count("|") + column.count("_"))
        for row in number_grid:
            number[1].append([row.count("|"), row.count("_")])
        if number_grid[1][0] == "|":
            number[2] = 1
        if number in numbers:
            return str(numbers.index(number))
        return "?"

    if input_grid is None:
        raise ValueError("No input.")
    if not isinstance(input_grid, list):
        raise TypeError("Input must be a list of strings.")
    if len(input_grid)%4:
        raise ValueError("Number of input lines is not a multiple of four")
    for line in input_grid:
        if len(line)%3:
            raise ValueError("Number of input columns is not a multiple of three")

    grid_line_amount = len(input_grid)//4
    numbers = list("" for line in range(grid_line_amount))
    while input_grid[0]:
        current_number = list([] for line in range(grid_line_amount))
        for line_no, line in enumerate(input_grid):
            if not isinstance(line, str):
                raise TypeError("Numbers must be represented as strings.")
            for character in line:
                if character not in " |_":
                    raise ValueError("Extraneous characters in string.")
            current_number[line_no//4].append(line[:3])
            input_grid[line_no] = line[3:]
        for i in range(grid_line_amount):
            numbers[i] += _get_number(current_number[i])
    return ",".join(numbers)
