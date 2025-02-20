"""Dominoes exercise"""

from collections import defaultdict

def can_chain(bones, /):
    """Checks if a valid circuit can be generated from the provided bones.
 
    :param list(tuple(int,int)) bones: A list of domino bones.
    """

    def _flip(bone, /):

        return (bone[1], bone[0])

    def _validate(bones, /):

        # Fast check if numbers are balanced (even).
        # Necessary but insufficient condition that is cheap to check.
        # Can be safely skipped.
        numbers = defaultdict(int)
        for bone in bones:
            for number in bone:
                numbers[number] += 1
        for number in numbers.values():
            if number % 2 != 0:
                return False
        # Use DFS to check if there are closed chains/unreachable chips.
        # Necessary and sufficient condition.
        graph = defaultdict(list)
        for a, b in bones:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()

        def _dfs(node):
            """Recursive DFS"""

            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(next(iter(graph)))
        if len(visited) != len(graph):
            return False
        # Valid if both checks pass.
        return True

    if bones is None:
        raise ValueError("Missing input.")
    if not isinstance(bones, list):
        raise TypeError("The input must be a list.")
    # Escape condition.
    if bones == []:
        return []
    # Basic error checking.
    for bone in bones:
        if not isinstance(bone, tuple):
            raise TypeError("bones must be tuples.")
        if len(bone) != 2:
            raise ValueError("bones must have 2 ends.")
        for end in bone:
            if not isinstance(end, int):
                raise TypeError("Ends must be integers.")
            if end not in range(7):
                raise ValueError("The amount of pips has to be in the range 0-6.")

    # Checking if a valid circuit can be generated.
    if not _validate(bones):
        return None

    bones_editing = bones[:]
    chain = [bones_editing.pop()]
    backtracked = []
    while bones_editing:
        added = False
        for bone in bones_editing:
            if chain[-1][1] == bone[0]:
                chain.append(bone)
                bones_editing.remove(bone)
                added = True
                break
            if chain[-1][1] == bone[1]:
                chain.append(_flip(bone))
                bones_editing.remove(bone)
                added = True
                break
        if not added:
            backtracked.append(chain.pop())
        if not bones_editing:
            bones_editing = backtracked
            backtracked = []
        if not backtracked and not added:
            return None
    return chain
