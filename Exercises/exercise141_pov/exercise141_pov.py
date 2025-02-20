"""POV exercise"""

from __future__ import annotations
from json import dumps
from functools import total_ordering
from copy import copy

@total_ordering
class Tree:
    """A tree structure. Node labels cannot be repeated."""

    def __init__(self, label: str, children: list = None, /):

        if label is None or not label:
            raise ValueError("Missing label.")
        if not isinstance(label, str):
            raise TypeError("Label must be a string.")
        if children is not None and not isinstance(children, list):
            raise TypeError("Children list must be a list.")
        for child in children or []:
            if not isinstance(child, Tree):
                raise TypeError("Children must be Tree objects.")

        self.label = label
        self.children = children or []

    def to_dict(self) -> dict:
        """Returns this tree as a dictionary."""

        return {self.label: [child.to_dict() for child in sorted(self.children)]}

    def __str__(self, indent=None, /) -> str:

        return dumps(self.to_dict(), indent=indent)

    def __lt__(self, other: Tree, /) -> bool:

        if not isinstance(other, Tree):
            raise NotImplementedError("Comparison between different types not implemented.")
        return self.label < other.label

    def __eq__(self, other: Tree, /) -> bool:

        if not isinstance(other, Tree):
            return False
        return self.to_dict() == other.to_dict()

    def __copy__(self):

        return Tree(self.label, [copy(child) for child in self.children])

    def _search_node(self, next_node: Tree, target: str, /) -> list:
        """Recursively finds a path to the target node."""

        if next_node.label == target:
            return [next_node]
        for child in next_node.children:
            path = [next_node, *self._search_node(child, target)]
            if path[-1].label == target:
                return path
        return []

    def from_pov(self, from_node: str, /) -> Tree:
        """Returns a deep copy of the tree using the target node as the root.
 
        :param str from_node: The node to be made into the root of the new tree.
        :raises ValueError: Raised when the tree can't be reoriented. This is because the target
                            node does not exixt in the tree.
        :return Tree: The new tree.
        """

        if from_node is None or not from_node:
            raise ValueError("Missing node.")
        if not isinstance(from_node, str):
            raise TypeError("Node label must be a string.")
        path = list(reversed(self._search_node(copy(self), from_node)))
        if not path:
            raise ValueError("Tree could not be reoriented")

        new_tree = path[0]
        max_index = len(path)
        for index in range(max_index):
            if index < max_index-1:
                path[index+1].children.remove(path[index])
                path[index].children.append(path[index + 1])
        return new_tree

    def path_to(self, from_node: str, to_node: str, /) -> list:
        """Returns a list of the labels of the nodes that represents a path between the given start
        and end nodes.
 
        :param str from_node: The node from which the path starts.
        :param str to_node: The node where the path ends.
        :raises ValueError: Raised when there is no possible path. This is because either the
                            starting or ending nodes don't exist in the tree.
        :return list: The path from the starting node to the end node.
        """

        if from_node is None or not from_node or to_node is None or not to_node:
            raise ValueError("Missing node.")
        if not isinstance(from_node, str) or not isinstance(to_node, str):
            raise TypeError("Node labels must be strings.")
        path = self._search_node(self.from_pov(from_node), to_node)
        if not path:
            raise ValueError("No path found")

        return [node.label for node in path]