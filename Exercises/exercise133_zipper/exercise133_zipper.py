"""Zipper exercise"""

class Zipper:
    """A zipper that navigates a binary tree.
 
    The tree's nodes must follow the format "{'value': any, 'right': node/None, 'left': node/None}".
 
    :raises TypeError: Raised when the tree is not a dictionary.
    :raises ValueError: Raised when there are malformed keys.
    :raises TypeError: Raised when the leaves are malformed.
    :return Zipper: The new zipper.
    """

    RIGHT = True
    LEFT = False

    def __init__(self, focus, previous = None, side = None):

        self._focus = focus
        self._previous = previous
        self._side = side

    @staticmethod
    def _check_tree(tree):

        if tree is not None:
            if not isinstance(tree, dict):
                raise TypeError("The tree must be a dictionary.")
            for key in tree.keys():
                if key not in ("value", "right", "left"):
                    raise ValueError("Malformed keys.")
            if tree["right"] is not None and not isinstance(tree["right"], dict):
                raise TypeError(f"Malformed right leaf {tree['right']}.")
            if tree["left"] is not None and not isinstance(tree["left"], dict):
                raise TypeError(f"Malformed left leaf: {tree['left']}.")
            Zipper._check_tree(tree["right"])
            Zipper._check_tree(tree["left"])

    @staticmethod
    def from_tree(tree):
        """Creates a zipper from the provided binary tree.
 
        :param dict tree: A dictionary representation of a binary tree.
        :return Zipper: The zipper.
        """

        Zipper._check_tree(tree)
        return Zipper(tree)

    def value(self):
        """Returns the focused node's value.
 
        :return any: The stored value.
        """

        return self._focus["value"]

    def set_value(self, value):
        """Sets the current node's value and returns a new Zipper with the updated tree.
 
        :param any value: The new value.
        :return Zipper: The new zipper.
        """

        self._focus["value"] = value
        return Zipper(self._focus, self._previous, self._side)

    def left(self):
        """Shifts the focus down a level to the left child.
 
        :return Zipper: A new zipper focused in the left child. 
        """

        if self._focus["left"] is None:
            return None
        return Zipper(self._focus["left"], self, self.LEFT)

    def set_left(self, left):
        """Inserts a subtree into the left child of the focused node.
 
        :param dict left: The new subtree to be inserted.
        :return Zipper: A new updated zipper.
        """

        Zipper._check_tree(left)
        self._focus["left"] = left
        return Zipper(self._focus, self._previous, self._side)

    def right(self):
        """Shifts the focus down a level to the right child.
 
        :return Zipper: A new zipper focused in the left child. 
        """

        if self._focus["right"] is None:
            return None
        return Zipper(self._focus["right"], self, self.RIGHT)

    def set_right(self, right):
        """Inserts a subtree into the right child of the focused node.
 
        :param dict right: The new subtree to be inserted.
        :return Zipper: A new updated zipper.
        """

        Zipper._check_tree(right)
        self._focus["right"] = right
        return Zipper(self._focus, self._previous, self._side)

    def up(self):
        """Moves the zipper's focus back up a level in the tree.
 
        :return Zipper, None: The zipper with the new focus. Returns none when going up a level
        from the tree's root.
        """

        if self._previous is not None:
            if self._side == self.RIGHT:
                return self._previous.set_right(self._focus)
            return self._previous.set_left(self._focus)
        return None

    def to_tree(self):
        """Converts the zipper into a tree.
 
        :return dict: The zipper's tree. 
        """

        if self._previous is not None:
            if self._side == self.RIGHT:
                return self._previous.set_right(self._focus).to_tree()
            return self._previous.set_left(self._focus).to_tree()
        return self._focus
