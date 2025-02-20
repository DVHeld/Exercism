"""Bowling exercise"""

STRIKE = 2
SPARE = 1
OPEN = 0
ONGOING = -1

class BowlingGame:
    """A bowling game. Stores all frames and throws and calculates the final score."""

    def __init__(self):

        self._match = []

    def roll(self, dropped_pins):
        """Stores a roll where the given amount of pins have been dropped.
 
        :param int dropped_pins: The amount of pins dropped in the roll.
        :raises ValueError: Raised when there's no input.
        :raises TypeError: Raised when the input is not an integer.
        :raises ValueError: Raised when the input is out of range. Valid range is 0 to 10.
        :raises IndexError: Raised when a roll is attempted when the game has been already
                            completed.
        :raises ValueError: Raised when the amount of pins dropped in both throws exceeds 10.
        """

        if dropped_pins is None:
            raise ValueError("No input.")
        if not isinstance(dropped_pins, int):
            raise TypeError("Input must be an integer.")
        if 10 < dropped_pins or dropped_pins < 0:
            raise ValueError("Input must be from 0 to 10.")
        if len(self._match) >= 10 and self._match[9]["bonus"] != ONGOING:
            throws = 0
            for frame in self._match[10:]:
                throws += len(frame["throws"])
            if throws == self._match[9]["bonus"]:
                raise IndexError("Cannot roll with a completed game.")
        if len(self._match) == 0 or\
           len(self._match[-1]["throws"]) == 2 or\
           self._match[-1]["bonus"] == STRIKE:
            self._match.append({
                "throws": [dropped_pins],
                "bonus": STRIKE if dropped_pins == 10 else ONGOING
                })
        elif len(self._match[-1]["throws"]) == 1:
            if len(self._match) != 10 and self._match[-1]["throws"][0] + dropped_pins > 10:
                raise ValueError("Two rolls in a frame cannot score more than 10 points.")
            self._match[-1]["throws"].append(dropped_pins)
            self._match[-1]["bonus"] = SPARE if sum(self._match[-1]["throws"]) == 10 else OPEN

    def score(self):
        """Calculates the final score.
 
        :raises IndexError: Raised when the score is requested on an incomplete game.
        :return int: The final score.
        """

        if len(self._match) < 10:
            raise IndexError("Incomplete games cannot be scored.")
        throws = 0
        for frame in self._match[10:]:
            throws += len(frame["throws"])
        if throws < self._match[9]["bonus"]:
            raise IndexError("Incomplete games cannot be scored.")
        score = 0
        for frame_no, frame in enumerate(self._match[:10]):
            if frame_no > 9:
                break
            score += sum(frame["throws"])
            counter = frame["bonus"]
            for next_frame in self._match[frame_no+1:]:
                if not counter:
                    break
                for throw in next_frame["throws"]:
                    if not counter:
                        break
                    score += throw
                    counter -= 1
        return score
