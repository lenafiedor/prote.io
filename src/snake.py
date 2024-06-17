import pygame
import copy
import os
from direction import Direction
from segment import Segment
from main import MAIN_DIR


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 608


class Snake(pygame.sprite.Sprite):

    """
    Represents the snake in the game.

    Attributes:
        original_image (pygame.Surface): The original image of the snake's head.
        image (pygame.Surface): The current image of the snake's head.
        rect (pygame.Rect): The position of the snake's head.
        direction (Direction): The current direction of the snake.
        new_direction (Direction): The new direction to change to.
        last_position (pygame.Rect): The last position of the snake's head.
        add_segment (bool): Flag indicating whether to add a new segment.
        segments (list): List of segments representing the snake's body.
    """

    def __init__(self):

        """
        Initializes the Snake instance with the head image and initial position.
        """

        self.original_image = pygame.image.load(os.path.join(MAIN_DIR, '../images/head.png'))
        self.image = pygame.transform.rotate(self.original_image, 0)
        self.rect = self.image.get_rect(center=(12*32+16, 9*32+16))
        self.direction = Direction.UP
        self.new_direction = Direction.UP
        self.last_position = self.rect
        self.add_segment = False
        self.segments = []

    def change_direction(self, direction: Direction):
        
        """
        Changes the direction of the snake if the new direction is not directly opposite.

        Args:
            direction (Direction): The new direction to change to.
        """

        if abs(direction.value - self.direction.value != 2):
            self.new_direction = direction

    def update(self):

        """
        Updates the snake's position and handles the movement of its segments.
        """

        self.direction = self.new_direction
        self.image = pygame.transform.rotate(self.original_image, (self.direction.value * -90))
        self.last_position = copy.deepcopy(self.rect)

        if self.direction == Direction.UP:
            self.rect.move_ip(0, -32)
        if self.direction == Direction.RIGHT:
            self.rect.move_ip(32, 0)
        if self.direction == Direction.DOWN:
            self.rect.move_ip(0, 32)
        if self.direction == Direction.LEFT:
            self.rect.move_ip(-32, 0)

        for i in range(len(self.segments)):
            if i == 0:
                self.segments[i].move(self.last_position)
            else:
                self.segments[i].move(self.segments[i-1].last_position)

        if self.add_segment:
            new_segment = Segment()
            new_position = None
            if len(self.segments) > 0:
                new_position = copy.deepcopy(self.segments[-1].position)
            else:
                new_position = copy.deepcopy(self.last_position)
            new_segment.position = new_position
            self.segments.append(new_segment)
            self.add_segment = False

    def add_amino(self):

        """
        Sets the flag to add a new segment to the snake.
        """

        self.add_segment = True

    def draw_segments(self, screen: pygame.Surface):

        """
        Draws the segments of the snake on the screen.

        Args:
            screen (pygame.Surface): The screen to draw the segments on.
        """

        for segment in self.segments:
            screen.blit(segment.image, segment.position)

    def check_collision(self) -> bool:

        """
        Checks if the snake has collided with its tail or the screen boundaries.

        Returns:
            bool: True if a collision occurred, False otherwise.
        """

        for segment in self.segments:
            if self.rect.colliderect(segment.position):
                return True

        if self.rect.top < 0 or self.rect.top >= SCREEN_HEIGHT:
            return True
        if self.rect.left < 0 or self.rect.left >= SCREEN_WIDTH:
            return True
        
        return False
