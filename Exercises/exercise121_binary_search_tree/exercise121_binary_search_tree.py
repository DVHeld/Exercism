"""Binary Search Tree exercise"""

class TreeNode:
    """A binary tree's node"""

    def __init__(self, data, left=None, right=None):

        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        """Inserts data into the node's subtrees. If the data is greater or equal to the own
        node's data, it's inserted into the left subtree, or into the right subtree otherwise.
 
        :param _type_ datum: The data to be inserted.
        """

        if self.data >= data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        if self.data < data:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)

    def __str__(self):

        return  f'TreeNode("{self.data}", {self.left}, {self.right})'

class BinarySearchTree:
    """A binary search tree"""

    def __init__(self, tree_data):

        self._root = TreeNode(tree_data[0])
        for data in tree_data[1:]:
            self._root.insert(data)

    def data(self):
        """Returns the tree in string form.
 
        :return str: The tree.
        """

        return self._root

    def sorted_data(self):
        """Returns a list of the data stored in the tree ordered ascending."""

        def _sorted_data(node):

            if node is None:
                return []
            return [*_sorted_data(node.left), node.data, *_sorted_data(node.right)]

        return [*_sorted_data(self._root)]
