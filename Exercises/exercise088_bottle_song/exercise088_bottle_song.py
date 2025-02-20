"""Bottle Song exercise"""

def recite(start, take=1):
    """Recites the song 'Ten Green Bottles.
 
    :param int start: The initial verse.
    :param int take: The amount of verses to recite, defaults to 1.
    :raises TypeError: Raised if the inputs are not integers.
    :raises ValueError: Raised if the inputs are greater than the maximum amount of verses.
    :raises ValueError: Raised if the inputs are less than 1.
    :return list[str]: The song. 
    """

    verses_max = 10

    if not isinstance(start, int) or not isinstance(take, int):
        raise TypeError("Inputs must be integer.")
    if start > verses_max or take > verses_max:
        raise ValueError(f"Maximum number of verses is {verses_max}")
    if start < 1 or take < 1:
        raise ValueError("Inputs cannot be lower than 1.")

    song = [[" green bottle" ," hanging on the wall,"],
            "And if one green bottle should accidentally fall,",
            ["There'll be ", " green bottle", " hanging on the wall."]]
    numbers = ["No", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
    verses = []

    for verse_number in range(take):
        verses.append((numbers[start-verse_number] + song[0][0] +
                       "s"*bool(start-verse_number-1) + song[0][1]))
        verses.append((numbers[start-verse_number] + song[0][0] +
                       "s"*bool(start-verse_number-1) + song[0][1]))
        verses.append(song[1])
        verses.append(song[2][0] + numbers[start-1-verse_number].lower() +
                      song[2][1] + "s"*bool(start-2-verse_number) + song[2][2])
        if take-verse_number-1:
            verses.append("")
    return verses
