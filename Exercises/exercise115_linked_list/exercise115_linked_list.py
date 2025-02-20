"""Linked List exercise"""


class Node:

    def __init__(self, value, succeeding=None, previous=None):

        self._value = value
        self._succeeding = succeeding
        self._previous = previous

    @property
    def value(self):

        return self._value

    @value.setter
    def value(self, value):

        self._value = value

    @property
    def succeeding(self):

        return self._succeeding

    @succeeding.setter
    def succeeding(self, node):

        self._succeeding = node

    @property
    def previous(self):

        return self._previous

    @previous.setter
    def previous(self, node):

        self._previous = node

    def __str__(self):

        return str(self.value)

class LinkedList:

    def __init__(self):

        self._root = None
        self._length = 0

    def push(self, value):

        if self._root:
            for node in self:
                if node.succeeding is None:
                    node.succeeding = Node(value, None, node)
        else:
            self._root = Node(value)
        self._length += 1

    def insert(self, iterable):

        if not isinstance(iterable, (list, tuple, dict,\
                                     str, set, range,\
                                     enumerate, zip, map,\
                                     filter, reversed)):
            self.push(iterable)
        else:
            for element in iterable:
                self.push(element)

    def pop(self):

        if len(self) == 0:
            raise IndexError("List is empty")
        for node in self:
            if not node.succeeding:
                if node.previous:
                    node.previous.succeeding = None
                self._length -= 1
                return node.value

    def shift(self):

        if self._length == 0:
            raise IndexError("List is empty")
        output_value = self._root.value
        self._root = self._root.succeeding
        self._length -= 1
        return output_value

    def unshift(self, value):

        if self._root is not None:
            self._root.previous = Node(value)
            self._root.previous.succeeding = self._root
            self._root = self._root.previous
            self._length += 1
        else:
            self.push(value)

    def delete(self, value):

        found = False
        for node in self:
            if node.value == value:
                found = True
                if node.previous:
                    node.previous.succeeding = node.succeeding
                if node.succeeding:
                    node.succeeding.previous = node.previous
                self._length -= 1
                break
            node = next(self)
        if not found:
            raise ValueError("Value not found")

    def __iter__(self):

        return next(self)

    def __next__(self):

        current_node = self._root
        while current_node is not None:
            output_node = current_node
            current_node = output_node.succeeding
            yield output_node

    def __len__(self):

        return self._length

    def __str__(self):

        node_list = []
        if len(self) > 0:
            for node in self:
                node_list.append(node.value)
        return str(node_list)

    def __repr__(self):

        output_str = "LinkedList().insert(("
        for item in self:
            if isinstance(item.value, str):
                output_str += f"'{item.value}', "
            else:
                output_str += f"{item.value}, "
        return output_str[:-2] + "))"
