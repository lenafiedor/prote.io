import pygame
import random
import time
import os
from amino import Aminoacid
from direction import Direction
from snake import Snake


# set the working directory to the current script directory
MAIN_DIR = os.path.dirname(os.path.realpath(__file__))

# define screen dimensions and initialize points to 0
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 608
points = 0

# create the background surface and set the game title
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Prote.io')

# fill the background with slightly modified tiles to create a pattern
for i in range(25):
    for j in range(19):
        img = pygame.image.load(os.path.join(MAIN_DIR, '/../images/background.png'))
        mask = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))
        
        img.fill(mask, special_flags=pygame.BLEND_ADD)
        background.blit(img, (i*32, j*32))

# initialize the game and the default font
pygame.init()
pygame.font.init()

# set up the display screen, clock for FPS counting, and the font for rendering text
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('geneva', 24)

# initialize the snake and set a timer event for moving the snake
snake = Snake()
SNAKE_MOVE = pygame.USEREVENT + 1
pygame.time.set_timer(SNAKE_MOVE, 200)

# initialize the first aminoacid sprite and add it to a sprite group of all aminoacids
amino = Aminoacid()
aminos = pygame.sprite.Group()
aminos.add(amino)

# main game loop
game_status = True
while game_status:
    # event handling loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_status = False
            if event.key == pygame.K_w:
                snake.change_direction(Direction.UP)
            if event.key == pygame.K_d:
                snake.change_direction(Direction.RIGHT)
            if event.key == pygame.K_s:
                snake.change_direction(Direction.DOWN)
            if event.key == pygame.K_a:
                snake.change_direction(Direction.LEFT)
        
        elif event.type == SNAKE_MOVE:
            snake.update()
        elif event.type == pygame.QUIT:
            game_status = False

    # check for collision with aminoacids
    collision = pygame.sprite.spritecollideany(snake, aminos)
    if collision != None:
        collision.kill()
        snake.add_amino()
        amino = Aminoacid()
        aminos.add(amino)
        points += 1

    # draw the background, snake, and amino acids on the screen
    screen.blit(background, (0, 0))
    snake.draw_segments(screen)
    screen.blit(snake.image, snake.rect)
    for amino in aminos:
        screen.blit(amino.image, amino.rect)

    # render and display the current score
    score_text = my_font.render(f'Score: {points}', False, (0, 0, 0))
    screen.blit(score_text, (16, 16))

    # check for collision with the snake's body or the screen borders
    if snake.check_collision():
        lost_text = my_font.render('You\'ve lost!', False, (0, 0, 0))
        screen.blit(lost_text, (SCREEN_WIDTH/2-50, SCREEN_HEIGHT/2))
        game_status = False
    
    # update the display and regulate the frame rate to 30 FPS (delays the program if a loop runs faster)
    pygame.display.flip()
    clock.tick(30)

# wait a few seconds before closing the game window
time.sleep(3)
pygame.quit()
