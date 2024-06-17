import pygame
import random
import os


images_dir = '../images/aminos/'
amino_pics = [
    'ala.png', 'arg.png', 'asn.png', 'asp.png', 'cys.png', 'gln.png', 
    'glu.png', 'gly.png', 'his.png', 'ile.png', 'leu.png', 'lys.png', 
    'met.png', 'phe.png', 'pro.png', 'ser.png', 'thr.png', 'trp.png', 
    'tyr.png', 'val.png'
]

class Aminoacid(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(images_dir, random.choice(amino_pics)))
        random_position = pygame.Rect(random.randint(0, 24) * 32, random.randint(1, 18) * 18, 32, 32)
        self.rect = random_position
