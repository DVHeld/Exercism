"""Say exercise"""

WORDS = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
    1000000: "million",
    1000000000: "billion", #short scale
    1000000000000: "trillion" #short scale
#   1000000000000: "billion", #long scale
#   1000000000000000000000000: "trillion" #long scale
}

def say(number,/):
    """Spells out the given number.
 
    :param int number: The number. Must be a positive integer lower than a short trillion.
    :raises TypeError: Raised when the input is not an integer.
    :raises ValueError: Raised when the number is not between -1 and 1000000000000.
    :return str: The spelled-out number.
    """

    def _decompose(number):
        """Decomposes the number into a list of 3-digit groups
 
        :param int number: The number to be decomposed.
        "return list[int]: The decomposed number.
        """

        return [] if not number else [*_decompose(number // 1000), number % 1000]

    if not isinstance(number, int):
        raise TypeError("input must be a positive integer")
    if not 0 <= number < 1000000000000:
        raise ValueError("input out of range")
    if not number:
        return WORDS[number]
    parts = _decompose(number)
    parts_amount = len(parts)
    spoken_number = ""
    for index, num in enumerate(parts):
        if num//100:
            spoken_number += f"{WORDS[num//100]} {WORDS[100]} "
            num = num % 100
        elif 0 < num < 20:
            spoken_number += f"{WORDS[num]} "
        if num//10 and num >= 20:
            spoken_number += f"{WORDS[num//10*10]}" + bool (num%10) * f"-{WORDS[num%10]} "
        if num:
            spoken_number += bool(parts_amount-index-1) * f"{WORDS[1000**(parts_amount-index-1)]} "
    return spoken_number.strip()
