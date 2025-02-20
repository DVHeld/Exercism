"""High Scores exercise"""

class HighScores:
    """Stores the high scores for Frogger."""

    def __init__(self, scores):

        if scores is None:
            raise ValueError("No input given.")
        if not isinstance(scores, list):
            raise TypeError("Scores must be in a list.")
        for score in scores:
            if not isinstance(score, int):
                raise TypeError("Scpres must be integers.")

        self.scores = scores

    def latest(self):
        """The most recent high score.
 
        :return int: The score.
        """

        return self.scores[-1]

    def personal_best(self):
        """The highest score.
 
        :return int: The score.
        """

        return max(self.scores)

    def personal_top_three(self):
        """The top three scores in descending order.
 
        :return list[int]: The top three list.
        """

        return sorted(sorted(self.scores)[-3:], reverse=True)
