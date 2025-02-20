"""Satellite exercise"""

class Node:
    """A tree's node."""

    def __init__(self, value, parent = None, left = None, right = None, /):

        self.value = value
        self.parent = parent
        if left is not None:
            self.left = Node(left)
        else:
            self.left = None
        if right is not None:
            self.right = Node(right)
        else:
            self.right = None

    def set_left(self, left, parent, /):
        """Inserts the left child node.
 
        :param any left: The value of the left child node.
        :param Node parent: The parent node.
        """

        self.left = Node(left, parent)

    def set_right(self, right, parent, /):
        """Inserts the right child node.
 
        :param any right: The value of the right child node.
        :param Node parent: The parent node.
        """

        self.right = Node(right, parent)

    def __str__(self):

        return str(self.value)

def tree_from_traversals(preorder, inorder):
    """Rebuilds a tree from its preorder and inorder traversals.
 
    :param list preorder: The preorder traversal, defaults to [].
    :param list inorder: The inorder traversal, defaults to [].
    :return dict: The rebuilt tree.
    """

    def _get_tree(node):
        """Recursive dictionary tree builder.
 
        :param Node node: A tree node.
        :return dict: A tree or subtree.
        """

        if node is None:
            return {}
        return ({"v": node.value, "l": _get_tree(node.left), "r": _get_tree(node.right)})

    # Exit early if input is an empty traversal.
    if preorder in (None, []) and inorder in (None, []):
        return {}
    # Basic input error checking
    if inorder in (None, []) or preorder in (None, []):
        raise ValueError("Missing input.")
    if not isinstance(preorder, list) or not isinstance(inorder, list):
        raise TypeError("Traversals must be lists.")
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    for index, pre_value in enumerate(preorder):
        if pre_value not in inorder or inorder[index] not in preorder:
            raise ValueError("traversals must have the same elements")
        if preorder.count(preorder[index]) != 1:
            raise ValueError("traversals must contain unique items")

    root = Node(preorder[0])
    current = root
    node_amount = len(preorder)
    index = 1

    while index < node_amount:
        new_value = preorder[index]
        if inorder.index(new_value) < inorder.index(current.value):
            current.set_left(new_value, current)
            index += 1
            current = current.left
        else:
            if current.right is None and current.left is not None:
                current.set_right(new_value, current)
                current = current.right
                index += 1
            else:
                current = current.parent
    return _get_tree(root)
