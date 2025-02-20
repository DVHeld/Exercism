"""Scale Generator exercise"""

class Scale:
    """A chromatic scale of the given tonic. The C scale is used if no tonic is passed."""

    scale_length = 12

    def __init__(self, tonic="C") -> None:

        scale_sharp = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
        scale_flat  = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
        tonic_sharp = ["C", "G", "D", "A", "E", "B", "F#", "a", "e", "b", "f#", "c#", "g#", "d#"]
        tonic_flat  = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]
        if not isinstance(tonic, str):
            raise TypeError("The tonic must be a string.")
        if tonic not in tonic_sharp + tonic_flat:
            raise ValueError("Invalid tonic.")
        selected_scale = scale_sharp if tonic in tonic_sharp else scale_flat
        tonic_index = selected_scale.index(tonic.capitalize())
        self.chromatic_scale = selected_scale[tonic_index:] + selected_scale[:tonic_index]

    def chromatic(self) -> list[str]:
        """Returns the chromatic scale.
 
        :return list[str]: The chromatic scale.
        """

        return self.chromatic_scale

    def interval(self, intervals="") -> list[str]:
        """The diatonic scale of the given intervals.
 
        :param str intervals: The intervals from which to build the scale. Defaults to no intervals.
        :return list[str]: The resulting scale.
        """

        if not isinstance(intervals, str):
            raise TypeError("Intervals must be a string")
        intervals_dict = {"m": 1, "M": 2, "A": 3}
        index = 0
        selected_interval = []
        for _interval in intervals:
            if _interval not in intervals_dict:
                raise ValueError(f"Invalid interval: {_interval}")
            selected_interval.append(self.chromatic_scale[index%self.scale_length])
            index += intervals_dict[_interval]
        return selected_interval + [self.chromatic_scale[index%self.scale_length]]
