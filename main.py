import pygame
import sys
from enum import Enum
import random

pygame.init()

WindowWidth = 640
WindowHeight = 480

class Direction(Enum):
    UNDEFINED = 0
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4

class Mouse:
    def __init__( self ):
        print( random.randrange( 0, WindowWidth, 1) )
        self.body = pygame.Rect((random.randrange( 0, WindowWidth - 10, 10), random.randrange( 0, WindowHeight - 10, 10), 10, 10 ))

class Snake:
    def __init__( self ):
        self.direction = Direction.UNDEFINED
        self.body = pygame.Rect(( WindowWidth / 2, WindowHeight / 2, 10, 10 ))

    def Move( self, moveRate ):
        if self.direction == Direction.UNDEFINED:
            return
                
        if self.direction == Direction.LEFT:
            if self.body.left >= moveRate:
                self.body.move_ip(-moveRate, 0)
        elif self.direction == Direction.RIGHT:
            if self.body.right <= WindowWidth - moveRate:
                self.body.move_ip( moveRate, 0)
        elif self.direction == Direction.UP:
            if self.body.top >= moveRate:
                self.body.move_ip( 0, -moveRate)
        elif self.direction == Direction.DOWN:
            if self.body.bottom <= WindowHeight - moveRate:
                self.body.move_ip( 0, moveRate)

screen = pygame.display.set_mode((WindowWidth, WindowHeight))

snake = Snake()
mouse = Mouse()

clock = pygame.time.Clock()

moveRate = 5

playing = True
while playing:
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0,255,0), snake.body)
    pygame.draw.rect( screen, (255,255,255), mouse.body)

    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True or key[pygame.K_LEFT] == True:
        snake.direction = Direction.LEFT
    elif key[pygame.K_d] == True or key[pygame.K_RIGHT] == True:
        snake.direction = Direction.RIGHT
    elif key[pygame.K_w] == True or key[pygame.K_UP] == True:
        snake.direction = Direction.UP
    elif key[pygame.K_s] == True or key[pygame.K_DOWN] == True:
        snake.direction = Direction.DOWN

    snake.Move( moveRate )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    pygame.display.update()

    clock.tick(30)
    fps = clock.get_fps()

pygame.quit()
sys.exit()