"""Ellen's Alien Game exercise

Solution to Ellen's Alien Game exercise."""

class Alien:
    """
    Attributes
    ----------
    (class)total_aliens_created: int - The amount of instances of this
    class that have been created.
    x_coordinate: int - X-Axis position.
    y_coordinate: int - Y-Axis position.
    health: int - Number of health points.
 
    Methods
    -------
    hit(): Reduces health by one point.
    is_alive(): Checks if the alien is alive.
    teleport(x_coordinate, y_coordinate): Teleports the alien to the
    given coordinates.
    collision_detection(other_object): Detects if there is a collision
    with the provided object. TODO
    """

    x_coordinate, y_coordinate = 0, 0
    health = 3
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        """Initializes the instance.
 
        :param x_coordinate: int - X-Axis position.
        :param y_coordinate: int - Y_axis position.
 
        This method initializes the instance, setting the alien's position
        to the given coordinates and incrementing the class's
        total_aliens_created attribute by 1.
        """

        self.x_coordinate, self.y_coordinate = x_coordinate, y_coordinate
        Alien.total_aliens_created += 1

    def hit(self):
        """Reduces health by one point.
 
        This method substracts 1 from the instance's health attribute.
        """

        self.health -= 1

    def is_alive(self):
        """Checks if the alien is alive.
 
        :return: bool - True if the alien is alive.
 
        This method checks if the amount of health points is greater than
        1 and returns True of it is, False otherwise.
        """

        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        """Teleports the alien to the given coordinates.
 
        :param x_coordinate: int - X-Axis position.
        :param y_coordinate: int - Y-Axis position.
 
        This method changes the alien's x and y coordinates to the
        provided ones.
        """

        self.x_coordinate, self.y_coordinate = x_coordinate, y_coordinate

    def collision_detection(self, other_object):
        """ TODO - Detects if there is a collision with the provided object.
 
        :param other_object: object - The object to check collision against.
 
        TODO
        """

        pass

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(alien_start_positions):
    """Creates a list of alien instances in the given coordinates.
 
    :param alien_start_positions: list - A list of iterables with the
    new aliens' coordinates.
 
    :return: list - A list of instances of the Alien class.
 
    This function takes a list of iterables containing x and y coordinates
    and returns a list of Alien class objects with their coordinates set
    accordingly.
    """

    aliens = []
    for new_alien in alien_start_positions:
        aliens.append(Alien(*new_alien))
    return aliens
