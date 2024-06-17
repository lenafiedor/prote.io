import pygame
import random
import os
from main import MAIN_DIR


# define the directory containing aminoacid images and the list of image files
images_dir = os.path.join(MAIN_DIR, '../images/aminos/')
amino_pics = [
    'ala.png', 'arg.png', 'asn.png', 'asp.png', 'cys.png', 'gln.png', 
    'glu.png', 'gly.png', 'his.png', 'ile.png', 'leu.png', 'lys.png', 
    'met.png', 'phe.png', 'pro.png', 'ser.png', 'thr.png', 'trp.png', 
    'tyr.png', 'val.png'
]

class Aminoacid(pygame.sprite.Sprite):

    '''
    Represents aminoacid in the game.

    Attributes:
        image (pygame.Surface): The image representing the aminoacid.
        rect (pygame.Rect): The position of the aminoacid on the game screen.
    '''

    def __init__(self):

        '''
        Initializes a new Aminoacid instance by selecting a random image and position.
        '''

        super().__init__()
        self.image = pygame.image.load(os.path.join(images_dir, random.choice(amino_pics)))
        random_position = pygame.Rect(random.randint(0, 24)*32, random.randint(1, 18)*18, 32, 32)
        self.rect = random_position
