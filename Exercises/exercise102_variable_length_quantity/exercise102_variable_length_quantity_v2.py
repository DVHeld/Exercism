"""Variable Length Quantity exercise"""

def encode(numbers):
    """Encodes a list of non-negative integers into a VLQ list.
 
    :param list[int] numbers: The list of numbers.
    :raises ValueError: Raised when there is no input.
    :raises TypeError: Raised when The input is not a list.
    :raises TypeError: Raised when A number is not an integer.
    :raises ValueError: Raised when a  umber is negative.
    :return list[int]: The encoded output list.
    """

    if not numbers:
        raise ValueError("No input.")
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    encoded = []
    for number in numbers:
        if not isinstance(number, int):
            raise TypeError("Numbers must be integers.")
        if number < 0:
            raise ValueError("Numbers can't be negative.")
        number = bin(number)[2:]
        first = True
        segments = []
        while number:
            if first:
                segments.insert(0, int("0" + number[-7:].zfill(7), 2))
                first = False
            else:
                segments.insert(0, int("1" + number[-7:].zfill(7), 2))
            number = number[:-7]
        encoded += list(segments)
    return encoded

def decode(input_bytes):
    """Decodes a list of VLQ encoded non-negative integers.
 
    :param list[int] bytes: The input integer list.
    :raises ValueError: Raised when there's no input.
    :raises TypeError: Raised when the input is not a list.
    :raises TypeError: Raised when a number is not an integer.
    :raises ValueError: Raised when a number is negative.
    :raises ValueError: Raised when the sequence is incomplete.
    :return list[int]: The decoded output list.
    """

    if not input_bytes:
        raise ValueError("No input.")
    if not isinstance(input_bytes, list):
        raise TypeError("Input must be a list.")

    decoded = []
    number = ""
    last = False
    for byte in input_bytes:
        if not isinstance(byte, int):
            raise TypeError("Numbers must be integers.")
        if byte < 0:
            raise ValueError("Numbers must be non-negative integers.")
        byte = bin(byte)[2:].zfill(8)
        if byte[0] == "1":
            number += byte[1:]
        else:
            last = True
            decoded.append(int(number + byte[1:], 2))
            number = ""
    if not last:
        raise ValueError("incomplete sequence")
    return decoded
