"""Tree Building exercise"""

class Record:
    """A forum record. Stores it's ID and it's parent's ID.
    """

    def __init__(self, record_id, parent_id):

        self.record_id = record_id
        self.parent_id = parent_id

    def __str__(self) -> str:

        return f"({self.record_id}, {self.parent_id})"

    def __repr__(self) -> str:

        return f"Record({self.record_id}, {self.parent_id})"

class Node:
    """A forum's record node. Stores it's own ID and a list of it's children nodes.
    """

    def __init__(self, node_id):

        self.node_id = node_id
        self.children = []

    def __str__(self) -> str:

        return f"ID: {self.node_id} -- Children: {self.children}"

    def __repr__(self) -> str:

        return f"Node({self.node_id})"

def BuildTree(records):
    """Builds a forum's records tree.
 
    :param list[Record] records: A list of a forum's records.
    :raises ValueError: Raised when a record's ID is invalid or there are missing records.
    :raises ValueError: Raised when a record other than the root record is it's own parent.
    :raises ValueError: Raised when a record's parent has an ID smaller than it's own.
    :return Node: The root record's node.
    """

    records.sort(key=lambda record: record.record_id)
    nodes = []
    if records:
        for identifier, record in enumerate(records):
            if record.record_id != identifier:
                raise ValueError("Record id is invalid or out of order.")
            if record.record_id !=0 and record.record_id == record.parent_id:
                raise ValueError("Only root should have equal record and parent id.")
            if (record.record_id == 0 and record.parent_id != 0) or\
                record.record_id < record.parent_id:
                raise ValueError("Node parent_id should be smaller than it's record_id.")
            node = Node(record.record_id)
            nodes.append(node)
            if node and record.record_id != 0:
                nodes[record.parent_id].children.append(node)
    return nodes[0] if nodes else None
