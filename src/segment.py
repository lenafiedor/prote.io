import pygame
import copy
import os


MAIN_DIR = os.path.dirname(os.path.realpath(__file__))


class Segment(pygame.sprite.Sprite):

    '''
    Represents a segment of the snake in the game.
    
    Attributes:
        image (pygame.Surface): The image representing the segment.
        position (pygame.Rect): The current position of the segment.
        last_position (pygame.Rect or None): The last position of the segment before it moved.
    '''

    def __init__(self):

        '''
        Initializes a new Segment instance with a default position and loads its image.
        '''
        
        super().__init__()
        self.image = pygame.image.load(f'{MAIN_DIR}/../images/segment.png')
        self.position = pygame.Rect(-32, -32, 32, 32) # default off-screen position
        self.last_position = None

    def move(self, new_position: pygame.Rect):

        '''
        Moves the segment to a new position.
        
        Args:
            new_position (pygame.Rect): The new position to move the segment to.
        '''

        self.last_position = copy.deepcopy(self.position)
        self.position = copy.deepcopy(new_position)
