"""Simple Linked List exercise"""

class Node:
    """A linked list's node.
    """

    def __init__(self, value, next_node):

        self.stored_value = value
        self.next_node = next_node

    def __str__(self) -> str:

        return f"Node({self.stored_value}, {self.next_node})"

    def __repr__(self) -> str:

        return str(self.stored_value)

    def value(self):
        """The node's value.
 
        :return any: The value.
        """

        return self.stored_value

    def next(self):
        """The next node in the linked list.
 
        :return Node: The next node.
        """

        return self.next_node

class LinkedList:
    """A linked list that can store values of any type and combination thereof.
    """

    def __init__(self, values=[]):

        self.nodes = {}
        index = None
        if isinstance(values, list):
            for index, value in enumerate(values):
                next_node = self.nodes[f"node_{index-1}"] if index else None
                self.nodes[f"node_{index}"] = Node(value, next_node)
        else:
            next_node = self.nodes[f"node_{index-1}"] if index else None
            for index, value in enumerate(list(values)):
                next_node = self.nodes[f"node_{index-1}"] if index else None
                self.nodes[f"node_{index}"] = Node(value, next_node)
        self.head_node = None if index is None else self.nodes[f"node_{index}"]

    def __len__(self):

        count = 0
        for _ in self:
            count += 1
        return count

    def __iter__(self):

        return self.__next__()

    def __next__(self):

        current_node = self.head_node
        while current_node is not None:
            yield current_node.value()
            current_node = current_node.next()

    def __repr__(self) -> str:

        repr_list = []
        for node in self:
            repr_list.append(node)
        repr_list.reverse()
        return f"LinkedList({repr_list})"

    def __str__(self) -> str:

        str_list = []
        for node in self:
            str_list.append(node)
        return ' --> '.join(str(item) for item in str_list)

    def head(self):
        """Returns the head's value.
 
        :raises EmptyListException: Raised when the list is empty.
        :return any: The head's value.
        """

        if not self.head_node:
            raise EmptyListException("The list is empty.")
        return self.head_node

    def push(self, value):
        """Inserts a value into the linked list. It becomes the head.
 
        :param any value: The value to be inserted.
        """

        new_node = Node(value, self.head_node)
        self.head_node = new_node

    def pop(self):
        """Returns the head and removes it from the list.
 
        :return any: The head's value.
        """

        popped_node = self.head()
        self.head_node = popped_node.next()
        return popped_node.value()

    def reversed(self):
        """Returns a copy of the linked list in reverse order.
 
        :return LinkedList: The new reversed list.
        """

        reversed_list = LinkedList()
        for node in self:
            reversed_list.push(node)
        return reversed_list

class EmptyListException(Exception):
    """Exception raised when the linked list is empty.
 
    message: explanation of the error.
    """

    def __init__(self, message):
        self.message = message
