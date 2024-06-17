import pygame
import random
import time
from amino import Aminoacid
from direction import Direction
from snake import Snake


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 608
points = 0

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Prote.io')

for i in range(25):
    for j in range(19):
        img = pygame.image.load('../images/background.png')
        mask = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))
        
        img.fill(mask, special_flags=pygame.BLEND_ADD)
        background.blit(img, (i*32, j*32))

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

my_font = pygame.font.SysFont('Comic Sans MS', 24)

snake = Snake()
SNAKE_MOVE = pygame.USEREVENT + 1
pygame.time.set_timer(SNAKE_MOVE, 200)

amino = Aminoacid()
aminos = pygame.sprite.Group()
aminos.add(amino)

game_status = True

while game_status:
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

    collision = pygame.sprite.spritecollideany(snake, aminos)
    if collision != None:
        collision.kill()
        snake.add_amino()
        amino = Aminoacid()
        aminos.add(amino)
        points += 1


    screen.blit(background, (0, 0))
    snake.draw_segments(screen)
    screen.blit(snake.image, snake.rect)
    for amino in aminos:
        screen.blit(amino.image, amino.rect)

    score_text = my_font.render(f'Score: {points}', False, (0, 0, 0))
    screen.blit(score_text, (16, 16))

    if snake.check_collision():
        lost_text = my_font.render('You\'ve lost!', False, (0, 0, 0))
        screen.blit(lost_text, (SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2))
        game_status = False
    
    pygame.display.flip()
    clock.tick(30)

time.sleep(3)
pygame.quit()
