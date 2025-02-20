"""Twelve Days exercise"""

def recite(start_verse=1, end_verse=12, /):
    """Recites the song "The Twelve Days of Christmas", starting from start_verse and ending on
    end_verse. If no input is given, the function recites the whole song.
 
    :param int start_verse: The verse from which to start the song, defaults to 1
    :param int end_verse: The verse on which to end the song, defaults to 12
    :raises TypeError: Raised if a input is not an integer.
    :raises ValueError: Raised if the starting verse is lower than 1.
    :raises ValueError: Raised if the end verse is lower than the starting verse.
    :raises ValueError: Raised if the end verse is higher than the maximum amount of verses.
    :return list[str]: The selected verses.
    """

    all_verses = 12

    if not isinstance(start_verse, int) or not isinstance(end_verse, int):
        raise TypeError("Inputs must be positive integers.")
    if start_verse < 1:
        raise ValueError("The starting verse must be greater than zero.")
    if start_verse > end_verse:
        raise ValueError("The end verse must be greater than the starting verse.")
    if end_verse > all_verses:
        raise ValueError(f"Maximum verse number is {all_verses}")

    components = [
        ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth",
         "tenth", "eleventh", "twelfth"],
        ["and a Partridge in a Pear Tree.",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"]
    ]

    verses = []
    for verse in range(start_verse-1, end_verse):
        print(f"verse: {verse} - {components[0][verse]} - {components[1][verse]}")
        line = f"On the {components[0][verse]} day of Christmas my true love gave to me: "
        if verse == 0:
            line += components[1][verse][4:]
        else:
            line += ", ".join(reversed(components[1][:verse+1]))
        verses.append(line)
    return verses
