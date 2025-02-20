"""Satellite exercise"""

class Node:
    """A tree's node."""

    def __init__(self, value, /):

        self.value = value
        self.left = None
        self.right = None

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
    if set(inorder) != set(preorder):
        raise ValueError("traversals must have the same elements")
    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")

    root = Node(preorder[0])
    current = root
    node_amount = len(preorder)
    index = 1
    parents = []
    inorder_index = {value: idx for idx, value in enumerate(inorder)}

    while index < node_amount:
        new_value = preorder[index]
        if inorder_index[new_value] < inorder_index[current.value]:
            current.left = Node(new_value)
            index += 1
            parents.append(current)
            current = current.left
        else:
            if current.right is None and current.left is not None:
                current.right = Node(new_value)
                parents.append(current)
                current = current.right
                index += 1
            else:
                current = parents.pop()
    return _get_tree(root)
