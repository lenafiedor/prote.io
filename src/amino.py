import pygame
import random
import os


MAIN_DIR = os.path.dirname(os.path.realpath(__file__))


# define the directory containing aminoacid images and the list of image files with their corresponding names
images_dir = f'{MAIN_DIR}/../images/aminos/'
amino_pics = {
    'Ala': 'ala.png', 'Arg': 'arg.png', 'Asn': 'asn.png', 'Asp': 'asp.png', 
    'Cys': 'cys.png', 'Gln': 'gln.png', 'Glu': 'glu.png', 'Gly': 'gly.png', 
    'His': 'his.png', 'Ile': 'ile.png', 'Leu': 'leu.png', 'Lys': 'lys.png', 
    'Met': 'met.png', 'Phe': 'phe.png', 'Pro': 'pro.png', 'Ser': 'ser.png', 
    'Thr': 'thr.png', 'Trp': 'trp.png', 'Tyr': 'tyr.png', 'Val': 'val.png'
}

class Aminoacid(pygame.sprite.Sprite):

    '''
    Represents aminoacid in the game.

    Attributes:
        name (str): Short name of the randomly chosen aminoacid.
        image (pygame.Surface): The image representing the aminoacid.
        rect (pygame.Rect): The position of the aminoacid on the game screen.
    '''

    def __init__(self):

        '''
        Initializes a new Aminoacid instance by selecting a random name, its image and position.
        '''

        super().__init__()
        self.name = random.choice(list(amino_pics.keys()))
        self.image = pygame.image.load(os.path.join(images_dir, amino_pics.get(self.name)))
        random_position = pygame.Rect(random.randint(0, 24)*32, random.randint(1, 18)*18, 32, 32)
        self.rect = random_position
