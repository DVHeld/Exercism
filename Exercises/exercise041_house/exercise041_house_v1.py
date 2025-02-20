"""House exercise"""

COMPONENTS = {
    1:  ("house"                           , "Jack built"),
    2:  ("malt"                            , "lay in"),
    3:  ("rat"                             , "ate"),
    4:  ("cat"                             , "killed"),
    5:  ("dog"                             , "worried"),
    6:  ("cow with the crumpled horn"      , "tossed"),
    7:  ("maiden all forlorn"              , "milked"),
    8:  ("man all tattered and torn"       , "kissed"),
    9:  ("priest all shaven and shorn"     , "married"),
    10: ("rooster that crowed in the morn" , "woke"),
    11: ("farmer sowing his corn"          , "kept"),
    12: ("horse and the hound and the horn", "belonged to")
}

BEGINNING = "This is"
ENDING = "."

def poem(verse):
    """Builds the body of the poem.
 
    This recursive function builds the body of the poem.
 
    :param int verse: The verse to be built.
    :return str: The built verse.
    """
    line = f" the {COMPONENTS[verse][0]} that {COMPONENTS[verse][1]}"
    if verse > 1:
        return f"{line}{poem(verse-1)}"
    return f"{line}"

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
    if start_verse > end_verse:
        raise ValueError("start_verse has to be lower than end_verse")
    verses = []
    for verse in range(start_verse, end_verse+1):
        verses.append(f"{BEGINNING}{poem(verse)}{ENDING}")
    return verses
