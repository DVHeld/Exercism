"""Space Age exercise"""

class SpaceAge:
    """The SpaceAge class.
 
    This class has methods to calculate the person's age in each planet.
    """

    planets_seconds = {
        "Mercury": 7600543.81992,
        "Venus"  : 19414149.052176,
        "Earth"  : 31557600.0,
        "Mars"   : 59354032.690079994,
        "Jupiter": 374355659.124,
        "Saturn" : 929292362.8848,
        "Uranus" : 2651370019.3296,
        "Neptune": 5200418560.032001
        }

    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        """Returns the age on Mercury.
 
        :param float seconds: The age in seconds.
        :return float: The age in Mercury years.
        """

        return round(self.seconds / self.planets_seconds["Mercury"], 2)

    def on_venus(self):
        """Returns the age on Venus.
 
        :param float seconds: The age in seconds.
        :return float: The age in Venus years.
        """

        return round(self.seconds / self.planets_seconds["Venus"], 2)

    def on_earth(self):
        """Returns the age on Earth.
 
        :param float seconds: The age in seconds.
        :return float: The age in Earth years.
        """

        return round(self.seconds / self.planets_seconds["Earth"], 2)

    def on_mars(self):
        """Returns the age on Mars.
 
        :param float seconds: The age in seconds.
        :return float: The age in Mars years.
        """

        return round(self.seconds / self.planets_seconds["Mars"], 2)

    def on_jupiter(self):
        """Returns the age on Jupiter.
 
        :param float seconds: The age in seconds.
        :return float: The age in Jupiter years.
        """

        return round(self.seconds / self.planets_seconds["Jupiter"], 2)

    def on_saturn(self):
        """Returns the age on Saturn.
 
        :param float seconds: The age in seconds.
        :return float: The age in Saturn years.
        """

        return round(self.seconds / self.planets_seconds["Saturn"], 2)

    def on_uranus(self):
        """Returns the age on Uranus.
 
        :param float seconds: The age in seconds.
        :return float: The age in Uranus years.
        """

        return round(self.seconds / self.planets_seconds["Uranus"], 2)

    def on_neptune(self):
        """Returns the age on Neptune.
 
        :param float seconds: The age in seconds.
        :return float: The age in Neptune years.
        """

        return round(self.seconds / self.planets_seconds["Neptune"], 2)
