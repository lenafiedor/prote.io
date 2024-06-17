from enum import Enum


class Direction(Enum):

    '''
    An enumeration to represent the possible directions in which the snake can move.

    Attributes:
        UP (int): Represents the upward direction with a value of 0.
        RIGHT (int): Represents the rightward direction with a value of 1.
        DOWN (int): Represents the downward direction with a value of 2.
        LEFT (int): Represents the leftward direction with a value of 3.
    '''

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
