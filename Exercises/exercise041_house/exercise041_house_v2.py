"""House exercise"""

COMPONENTS = [
    ("the house"                           , "that Jack built"),
    ("the malt"                            , "that lay in"),
    ("the rat"                             , "that ate"),
    ("the cat"                             , "that killed"),
    ("the dog"                             , "that worried"),
    ("the cow with the crumpled horn"      , "that tossed"),
    ("the maiden all forlorn"              , "that milked"),
    ("the man all tattered and torn"       , "that kissed"),
    ("the priest all shaven and shorn"     , "that married"),
    ("the rooster that crowed in the morn" , "that woke"),
    ("the farmer sowing his corn"          , "that kept"),
    ("the horse and the hound and the horn", "that belonged to")
]

def recite(start_verse, end_verse):
    """Recites the poen "The House that Jack Built".
 
    This function takes the numbers of the verse whith wich to begin the poem
    and the verse with which to end the poem. It returns a list of the
    selected verses. 
 
    :param int start_verse: The verse from which to start the poem.
    :param int end_verse: The verse in which to finish the poem. 
    :raises ValueError: Raised if the starting verse is higher than the
                        ending verse.
    :return list[str]: The selected verses.
    """

    def poem(verse):
        """Builds the body of the poem.
 
        This recursive function builds the body of the poem.
 
        :param int verse: The verse to be built.
        :return str: The built verse.
        """
        line = f" {COMPONENTS[verse-1][0]} {COMPONENTS[verse-1][1]}"
        if verse > 1:
            return f"{line}{poem(verse-1)}"
        return f"{line}"

    if start_verse > end_verse:
        raise ValueError("start_verse has to be lower than end_verse")
    verses = []
    for verse in range(start_verse, end_verse+1):
        verses.append(f"This is{poem(verse)}.")
    return verses
