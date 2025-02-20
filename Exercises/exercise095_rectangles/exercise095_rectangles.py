"""Rectangles exercise"""

def rectangles(strings):
    """Counts the amount of rectangles in the input.
 
    The input must be a list of strings. Each string represents a row. '+' represents a vertex or
    an intersection of edges, '-' represents a horizontal edge, '|' represents a vertical edge and
    ' ' represents an empty space. A square is defined as a set of four vertexes/intersections
    connected by edges.
 
    :param list[str] strings: The input matrix.
    :raises ValueError: Raised when there is no input.
    :raises TypeError: Raised when the input is not a list.
    :raises TypeError: Raised when a row is not a string.
    :raises ValueError: Raised when the input contains invalid characters.
    :return int: The amount of rectangles in the input matrix.
    """

    if strings is None:
        raise ValueError("No input.")
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings.")

    def _test_set(coord_set, strings):

        for index in range(2):
            for char_index in range(coord_set[index*2][1]+1, coord_set[index*2+1][1]):
                if strings[coord_set[index*2][0]][char_index] not in "-+":
                    return False
            for char_index in range(coord_set[index][0]+1, coord_set[index+2][0]):
                if strings[char_index][coord_set[index][1]] not in "|+":
                    return False
        return True
    
    vertex_map = []
    for row, line in enumerate(strings):
        if not isinstance(line, str):
            raise TypeError("Input must be a list of strings.")
        for column, char in enumerate(line):
            if char not in "|-+ ":
                raise ValueError("Invalid characters in input.")
            if char == "+":
                vertex_map.append((row, column))

    count = 0
    coord_sets = []
    map_a = vertex_map + []
    for coord_a in vertex_map:
        map_a.remove(coord_a)
        for coord_b in map_a:
            map_b = map_a + []
            map_b.remove(coord_b)
            if coord_b[0] == coord_a[0]:
                for coord_c in map_b:
                    map_c = map_b + []
                    map_c.remove(coord_c)
                    if coord_c[1] == coord_a[1]:
                        for coord_d in map_c:
                            if coord_d[1] == coord_b[1] and coord_d[0] == coord_c[0]:
                                coord_set = (coord_a, coord_b, coord_c, coord_d)
                                if _test_set(coord_set, strings):
                                    count += 1
                                    coord_sets.append(coord_set)
    return count
