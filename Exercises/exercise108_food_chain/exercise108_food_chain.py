"""Food Chain exercise"""

def recite(start_verse=None, end_verse=None):
    """Recites the given verses of the song 'I Know an Old Lady Who Swallowed a Fly'. If only one
    value is provided, only the corresponding verse is returned.
 
    :param int start_verse: The verse from which to start, defaults to 1.
    :param int end_verse: The last verse to be recited, defaults to 8.
    :raises TypeError: Raised when the inputs are not integers.
    :raises ValueError: Raised when the starting verse is greater than the ending verse.
    :raises ValueError: Raised when the inputs are less than 1.
    :return list[str]: The requested verses.
    """

    if start_verse is not None and end_verse is None:
        end_verse = start_verse
    if start_verse is None:
        start_verse = 1
    if end_verse is None:
        end_verse = 8
    if not isinstance(start_verse, int) or not isinstance(end_verse, int):
        raise TypeError("Inputs must be integers.")
    if start_verse > end_verse:
        raise ValueError("Starting verse cannot be greater than ending verse.")
    if start_verse < 1 or end_verse < 1:
        raise ValueError("Inputs must be greater than zero.")

    max_verses = 8
    start_verse -= 1
    song = []
    first = "I know an old lady who swallowed a {}."
    second = "She swallowed the {} to catch the {}"
    spider_special = " that wriggled and jiggled and tickled inside her"
    action_list = (
        "I don't know why she swallowed the fly. Perhaps she'll die.",
        "It wriggled and jiggled and tickled inside her.",
        "How absurd to swallow a bird!",
        "Imagine that, to swallow a cat!",
        "What a hog, to swallow a dog!",
        "Just opened her throat and swallowed a goat!",
        "I don't know how she swallowed a cow!",
        "She's dead, of course!"
    )
    animal_list = ("fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse")
    for i in range(start_verse, end_verse if end_verse != max_verses else end_verse-1):
        song.append(first.format(animal_list[i]))
        song.append(action_list[i])
        for j in range(i, 0, -1):
            line = second.format(animal_list[j], animal_list[j-1])
            if j == 2:
                line += spider_special
            line += "."
            song.append(line)
        if i != 0:
            song.append(action_list[0])
        if i != end_verse-1:
            song.append("")
    if end_verse == max_verses:
        song.append(first.format(animal_list[-1]))
        song.append(action_list[-1])
    return song
