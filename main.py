import pygame
import sys
from enum import Enum

pygame.init()

class Direction(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4

class Snake:
    def __init__( self, windowWidth, windowHeight ):
        self.direction = Direction.RIGHT
        self.body = pygame.Rect(( windowWidth / 2, windowHeight / 2, 10, 10 ))
    
    def Move( self, moveRate ):
        if self.direction == Direction.LEFT:
            if self.body.left >= moveRate:
                self.body.move_ip(-moveRate, 0)
        if self.direction == Direction.RIGHT:
            if self.body.right <= WindowWidth - moveRate:
                self.body.move_ip( moveRate, 0)
        if self.direction == Direction.UP:
            if self.body.top >= moveRate:
                self.body.move_ip( 0, -moveRate)
        if self.direction == Direction.DOWN:
            if self.body.bottom <= WindowHeight - moveRate:
                self.body.move_ip( 0, moveRate)

WindowWidth = 640
WindowHeight = 480

screen = pygame.display.set_mode((WindowWidth, WindowHeight))

snake = pygame.Rect((300,250,10,10))

direction = Direction.RIGHT

clock = pygame.time.Clock()

moveRate = 5

playing = True
while playing:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0,255,0), snake)

    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True or key[pygame.K_LEFT] == True:
        if snake.left >= moveRate:
            snake.move_ip(-moveRate, 0)
    elif key[pygame.K_d] == True or key[pygame.K_RIGHT] == True:
        if snake.right <= WindowWidth - moveRate:
            snake.move_ip( moveRate, 0)
    elif key[pygame.K_w] == True or key[pygame.K_UP] == True:
        if snake.top >= moveRate:
            snake.move_ip( 0, -moveRate)
    elif key[pygame.K_s] == True or key[pygame.K_DOWN] == True:
        if snake.bottom <= WindowHeight - moveRate:
            snake.move_ip( 0, moveRate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    pygame.display.update()

    clock.tick(30)
    fps = clock.get_fps()

pygame.quit()
sys.exit()