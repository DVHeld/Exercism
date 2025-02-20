"""House exercise"""

def recite(start_end_verse=None, end_verse=None, /):
    """Recites the poen "The House that Jack Built".
 
    This function takes the numbers of the verse whith wich to begin the poem
    and the verse with which to end the poem. It returns a list of the
    selected verses. 
 
    :param int start_end_verse: The verse from which to start the poem. If only one argument is given
    :param int end_verse: The verse in which to finish the poem. 
    :raises ValueError: Raised if the starting verse is higher than the
                        ending verse.
    :return list[str]: The selected verses.
    """

    ALL_VERSES = 12

    if (start_end_verse is not None) and (not isinstance(start_end_verse, int)) or\
       (end_verse is not None) and (not isinstance(end_verse, int)):
        raise TypeError("The verse numbers have to be positive integers.")
    if start_end_verse is None:
        start_number, end_number = 0, ALL_VERSES
    elif end_verse is None:
        start_number, end_number = 0, start_end_verse
    else:
        start_number, end_number = start_end_verse-1, end_verse
    if start_number < 0 or end_number < 0:
        raise ValueError("The verse numbers have to be positive integers.")
    if end_number <= start_number:
        raise ValueError("The end verse number has to be higher than the start verse number.")
    if start_number > ALL_VERSES or end_number > ALL_VERSES:
        raise ValueError(f"The amount of verses cannot be higher than {ALL_VERSES}.")

    def verse(number):
        """Builds the body of the poem.
 
        This recursive function builds the body of the poem.
 
        :param int number: The number of the verse to be built.
        :return str: The built verse.
        """

        COMPONENTS = [
            " the house that Jack built",
            " the malt that lay in",
            " the rat that ate",
            " the cat that killed",
            " the dog that worried",
            " the cow with the crumpled horn that tossed",
            " the maiden all forlorn that milked",
            " the man all tattered and torn that kissed",
            " the priest all shaven and shorn that married",
            " the rooster that crowed in the morn that woke",
            " the farmer sowing his corn that kept",
            " the horse and the hound and the horn that belonged to"
        ]

        line = COMPONENTS[number]
        return f"{line}{verse(number-1)}" if number > 0 else line

    return [
        f"This is{verse(number)}."
        for number in range(start_number, end_number)
    ]
