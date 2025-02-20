"""DOT DSL exercise"""

NODE, EDGE, ATTR = "Node", "Edge", "Attribute"

class Node:
    """A node. Stores its name and attributes."""

    def __init__(self, name, attrs):

        self.name = name
        self.attrs = attrs

    def __eq__(self, other):

        return self.name == other.name and self.attrs == other.attrs

    def __repr__(self):

        return f"Node({self.name}, {self.attrs})"

class Edge:
    """An edge. Stores its source, distance and attributes."""

    def __init__(self, src, dst, attrs):

        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):

        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)

    def __repr__(self):

        return f"Edge({self.src}, {self.dst}, {self.attrs})"

class Graph:
    """A graph. Stores its components. Valid components are nodes, edges and attributes."""

    def __init__(self, data=None):

        self._data = {NODE: [], EDGE: [], ATTR: {}}
        if data is not None:
            self._validate_data(data)
            for datum in data:
                if datum[0] == NODE:
                    self._validate_node(datum)
                    self._data[NODE].append(Node(datum[1], datum[2]))
                elif datum[0] == EDGE:
                    self._validate_edge(datum)
                    self._data[EDGE].append(Edge(datum[1], datum[2], datum[3]))
                elif datum[0] == ATTR:
                    self._validate_attr(datum)
                    self._data[ATTR][datum[1]] = datum[2]
                else:
                    raise ValueError("Invalid input.")

    def _validate_data(self, data):

        if not isinstance(data, list):
            raise TypeError("Graph data malformed")
        for datum in data:
            if not isinstance(datum, tuple):
                raise TypeError("Graph data malformed")
            if len(datum) < 1:
                raise TypeError("Graph item incomplete")
            if datum[0] not in (NODE, EDGE, ATTR):
                raise ValueError("Unknown item")
            if len(datum) < 2:
                raise TypeError("Graph item incomplete")

    def _validate_node(self, node_data):

        if not (isinstance(node_data[1], str) and isinstance(node_data[2], dict)):
            raise ValueError("Node is malformed")
        for key, value in node_data[2].items():
            if not (isinstance(key, str) and\
                    isinstance(value, str) and\
                    value is not None):
                raise ValueError("Node is malformed")

    def _validate_edge(self, edge_data):

        if not (isinstance(edge_data[1], str) and\
                isinstance(edge_data[2], str) and\
                isinstance(edge_data[3], dict)):
            raise ValueError("Edge is malformed")
        for key, value in edge_data[3].items():
            if not (isinstance(key, str) and\
                    isinstance(value, str) and\
                    value is not None):
                raise ValueError("Edge is malformed")

    def _validate_attr(self, attr_data):

        if not (isinstance(attr_data[1], str) and isinstance(attr_data[2], str)):
            raise ValueError("Attribute is malformed")

    @property
    def nodes(self):
        """The graph's nodes.
 
        :return list[Node]: The node list.
        """

        return self._data[NODE]

    @property
    def edges(self):
        """The graph's edges.
 
        :return list[Edge]: The edge list.
        """

        return self._data[EDGE]

    @property
    def attrs(self):
        """The graph's attributes.
 
        :return list[dict]: The attribute list.
        """

        return self._data[ATTR]
