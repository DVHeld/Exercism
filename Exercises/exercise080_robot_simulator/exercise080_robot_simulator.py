"""Robot Simulator exercise"""

NORTH      = 0
EAST       = 1
SOUTH      = 2
WEST       = 3
ADVANCE    = "A"
TURN_LEFT  = "L"
TURN_RIGHT = "R"

class Robot:
    """A robot.
    
    The coordinates must be integers.
    The valid directions are:
        NORTH = 0,
        EAST  = 1,
        SOUTH = 2,
        WEST  = 3
    """

    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        """Initializes the robot.
 
        :param int direction: The initial direction, defaults to NORTH
        :param int x_pos: The initial x coordinate, defaults to 0
        :param int y_pos: The initial y coordinate, defaults to 0
        :raises TypeError: Raised if the direction is not an integer.
        :raises ValueError: Raised if the direction is not valid.
        :raises TypeError: Raised if the coordinates are not integers.
        """

        if not isinstance(direction, int):
            raise TypeError("Direction must be an integer.")
        if direction not in (NORTH, EAST, SOUTH, WEST):
            raise ValueError("Invalid direction.")
        if not isinstance(x_pos, int) or not isinstance(y_pos, int):
            raise TypeError("Coordinates must be integers.")

        self.coordinates = (x_pos, y_pos)
        self.direction   =  direction

    def move(self, instructions):
        """Moves the robot according to the instructions provided.
 
        Valid instructions are:
            'L' - Turn left
            'R' - Turn right
            'A' - Advance
 
        :raises TypeError: Raised if the input is not a string.
        :raises ValueError: Raised if there are invalid instructions.
        :param str instructions: The instruction sequence.
        """

        if not isinstance(instructions, str):
            raise TypeError("Input must be a string.")

        for instruction in instructions:
            if instruction not in (TURN_LEFT, TURN_RIGHT, ADVANCE):
                raise ValueError("Invalid instruction.")
            if instruction == ADVANCE:
                if self.direction == NORTH:
                    self.coordinates = self.coordinates[0], self.coordinates[1]+1
                elif self.direction == SOUTH:
                    self.coordinates = self.coordinates[0], self.coordinates[1]-1
                elif self.direction == EAST:
                    self.coordinates = self.coordinates[0]+1, self.coordinates[1]
                elif self.direction == WEST:
                    self.coordinates = self.coordinates[0]-1, self.coordinates[1]
            elif instruction == TURN_LEFT:
                self.direction = (self.direction-1)%4
            elif instruction == TURN_RIGHT:
                self.direction = (self.direction+1)%4
