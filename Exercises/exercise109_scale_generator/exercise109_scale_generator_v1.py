"""Scale Generator exercise"""

class Scale:
    """A chromatic scale of the given tonic."""

    scale_sharp = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G" , "G#"]
    tonic_sharp = ["C", "G" , "D", "A", "E" , "B", "F#", "a", "e", "b" , "f#", "c#", "g#", "d#"]
    scale_flat  = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G" , "Ab"]
    scale_length = 12

    def __init__(self, tonic):

        self.tonic = tonic
        selected_scale = self.scale_sharp\
            if self.tonic in self.tonic_sharp else self.scale_flat
        self.tonic_index = selected_scale.index(self.tonic.capitalize())
        scale_overflow = self.tonic_index + self.scale_length - self.scale_length
        self.chromatic_scale = selected_scale[self.tonic_index:] + selected_scale[:scale_overflow]

    def chromatic(self):
        """Returns the chromatic scale.
 
        :return list[str]: The chromatic scale.
        """

        return self.chromatic_scale

    def interval(self, intervals):
        """The diatonic scale of the given intervals.
 
        :param str intervals: The intervals from which to build the scale.
        :return list[str]: The resulting scale.
        """

        index = 0
        selected_interval = []
        for interval in intervals:
            selected_interval.append(self.chromatic_scale[index%self.scale_length])
            if interval == "m":
                index += 1
            elif interval == "M":
                index += 2
            else:
                index += 3
        return selected_interval + [self.chromatic_scale[index%self.scale_length]]
