import pygame
import copy


class Segment(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../images/segment.png')
        self.position = pygame.Rect(-32, -32, 32, 32)
        self.last_position = None

    def move(self, new_position):
        self.last_position = copy.deepcopy(self.position)
        self.position = copy.deepcopy(new_position)
