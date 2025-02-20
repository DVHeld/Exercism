"""Simple Linked List exercise"""

class Node:
    """A linked list's node.
    """

    def __init__(self, value, next_node):
        self._value = value
        self._next_node = next_node
    def __str__(self) -> str:
        return f"Node({self._value}, {self._next_node})"
    def __repr__(self) -> str:
        return str(self._value)

    def value(self):
        """The node's value.
 
        :return any: The value.
        """

        return self._value

    def next(self):
        """The next node in the linked list.
 
        :return Node: The next node.
        """

        return self._next_node

class LinkedList:
    """A linked list that can store values of any type and combination thereof.
    """

    def __init__(self, values=[]):

        self._len, self._head = 0, None
        for value in values:
            self.push(value)

    def __len__(self):

        return self._len

    def __iter__(self):

        return self.__next__()

    def __next__(self):

        current_node = self._head
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
        return ' -> '.join(str(item) for item in str_list)

    def head(self):
        """Returns the head's value.
 
        :raises EmptyListException: Raised when the list is empty.
        :return any: The head's value.
        """

        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value):
        """Inserts a value into the linked list. It becomes the head.
 
        :param any value: The value to be inserted.
        """

        self._head = Node(value, self._head)
        self._len += 1

    def pop(self):
        """Returns the head and removes it from the list.
 
        :return any: The head's value.
        """

        popped_node = self.head()
        self._head = popped_node.next()
        self._len -= 1
        return popped_node.value()

    def reversed(self):
        """Returns a copy of the linked list in reverse order.
 
        :return LinkedList: The new reversed list.
        """

        return LinkedList(self)

class EmptyListException(Exception):
    """Exception raised when the linked list is empty.
 
    message: explanation of the error.
    """

    def __init__(self, message):

        super().__init__(message)
