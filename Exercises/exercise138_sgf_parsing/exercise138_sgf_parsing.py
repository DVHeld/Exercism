"""SGF Parsing exercise"""

from re import match

class SgfTree:
    """An SGF tree node. Implements equality comparison '=='."""

    def __init__(self, properties=None, children=None):

        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):

        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):

        return not self == other

    def __str__(self):

        return f"SgfTree({self.properties}, {[str(child) for child in self.children]})"

def parse(input_string):
    """Parses a string containing an SGF tree and returns it as a SgfTree object.
 
    :param str input_string: The string containing the tree.
    """

    def _validate_tree(input_string_p):
        """Checks if the tree has nodes."""

        if not input_string_p:
            return None
        if input_string_p[0] == "(":
            input_string_p = input_string_p[1:-1]
        if input_string_p[0] != ";":
            raise ValueError("tree with no nodes")
        input_string_p = input_string_p[1:]
        return input_string_p

    def _properties_end(input_string_p):
        """Looks for the end of the current node, returning its index."""

        in_value = False
        escape_next = False
        index = 0
        input_length = len(input_string_p)
        never_opened = True

        for index, char in enumerate(input_string_p):
            if char == "[" and not in_value:
                never_opened = False
                in_value = True
            elif escape_next:
                escape_next = False
            elif char == "\\" and not escape_next:
                escape_next = True
                continue
            elif char == "]" and (index == input_length-1):
                index += 1
                break
            elif char == "]":
                in_value = False
            elif char in ";(" and not in_value:
                break
        if never_opened and input_length:
            raise ValueError("properties without delimiter")
        return index

    def _parse_properties(properties):
        """Receives a string containing the node's properties and parses them into a dictionary."""

        parsed_properties = {}
        in_property_name = False
        in_property_value = False
        property_name = ""
        property_value = ""
        current_property_name = ""
        escape_next = False

        for char in properties:
            if char == "[" and not in_property_name and not in_property_value:
                property_name = current_property_name
                in_property_value = True
            elif in_property_name or (not in_property_name and not in_property_value):
                in_property_name = True
                if len(property_name) >= 2:
                    raise ValueError("property cannot have more than 2 letters")
                if char == "[":
                    parsed_properties[property_name] = []
                    current_property_name = property_name
                    in_property_name = False
                    in_property_value = True
                elif match(r"[^A-Z]", char):
                    raise ValueError("property must be in uppercase")
                else:
                    property_name += char
            elif in_property_value:
                if char == "\\" and not escape_next:
                    escape_next = True
                elif char == "]" and not escape_next:
                    in_property_value = False
                    parsed_properties[property_name].append(property_value)
                    property_name = ""
                    property_value = ""
                elif match(r"\s", char) and char != "\n":
                    property_value += " "
                elif escape_next:
                    if char != "\n":
                        property_value += char
                    escape_next = False
                else:
                    property_value += char
        return parsed_properties

    def _parse_node(input_string_p):
        """Recursively iterates over each node, returning an SgfTree object containing its
        processed properties and child subtrees."""

        input_string_p = _validate_tree(input_string_p)
        properties_end = _properties_end(input_string_p)
        properties_processing = input_string_p[:properties_end]
        input_string_p = input_string_p[properties_end:]
        parsed_properties = _parse_properties(properties_processing)
        children = []

        if input_string_p:
            if input_string_p[0] == ";":
                children.append(_parse_node(input_string_p))
            elif input_string_p[0] == "(":
                child_data = ""
                count = 0
                for char in input_string_p:
                    if char == "(":
                        count += 1
                    elif char == ")":
                        count -= 1
                    child_data += char
                    if count == 0:
                        children.append(_parse_node(child_data))
                        child_data = ""
        return SgfTree(parsed_properties, children)
    if input_string in (None, "", ";"):
        raise ValueError("tree missing")
    if input_string == "()":
        raise ValueError("tree with no nodes")
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")
    if input_string[0] != "(":
        raise ValueError("Malformed input.")
    return _parse_node(input_string[:])
