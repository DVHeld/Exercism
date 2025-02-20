"""Saddle Points exercise"""

def saddle_points(forest):
    """Finds the potential locations for a tree house in the given forest.
 
    :param list forest: A list containing the forest's trees' heights.
    :raises ValueError: Raised when there is no input.
    :raises TypeError: Raised when the input is not a list.
    :raises ValueError: Raised when the forest is shaped irregularly.
                        The forest must be a rectangle.
    :raises TypeError: Raised when there are trees with negative height.
    :return list[dict]: A list of the coordinates of the potential locations.
    """

    if forest is None:
        raise ValueError("Input must not be empty.")
    if not isinstance(forest, list):
        raise TypeError("Input must be a list.")

    candidates = []
    forest_length = len(forest[0])-1 if forest else 0

    for y, row in enumerate(forest):
        if forest_length != len(row)-1:
            raise ValueError("irregular matrix")
        candidate = max(row)
        for x, tree in enumerate(row):
            if not isinstance(tree, int) or tree < 0:
                raise TypeError("Tree heights must be positive integers.")
            if  tree == candidate:
                check = True
                for r in forest:
                    if r[x] < candidate:
                        check = False
                if check:
                    candidates.append({"row": y+1, "column": x+1})
    return candidates
