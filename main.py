import pygame
import sys
from enum import Enum
import random

class Direction(Enum):
    UNDEFINED = 0
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4

class Mouse:
    def __init__( self ):
        print( random.randrange( 0, WindowWidth, 1) )
        self.body = pygame.Rect((random.randrange( 0, WindowWidth - 10, 10), 
                                 random.randrange( 0, WindowHeight - 10, 10), 
                                 BodySize, 
                                 BodySize ))

class Snake:
    def __init__( self ):
        self.direction = Direction.UNDEFINED
        self.body = pygame.Rect(( WindowWidth / 2, WindowHeight / 2, 
                                 BodySize, BodySize ))

    def Move( self, moveRate ):
        if self.direction == Direction.UNDEFINED:
            return
        
        if self.direction == Direction.RIGHT or self.direction == Direction.LEFT:
            remainder = self.body.top % BodySize
            self.body.move_ip( 0, -remainder)
        if self.direction == Direction.UP or self.direction == Direction.DOWN:
            remainder = self.body.left % BodySize
            self.body.move_ip( -remainder, 0)

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

pygame.init()

#Defines
WindowWidth = 640
WindowHeight = 480
BodySize = 10
MoveRate = 2

screen = pygame.display.set_mode((WindowWidth, WindowHeight))
pygame.display.set_caption('Snake')

snake = Snake()
mouse = Mouse()

clock = pygame.time.Clock()

playing = True
while playing:
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0,255,0), snake.body)
    pygame.draw.rect(screen, (255,255,255), mouse.body)

    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True or key[pygame.K_LEFT] == True:
        snake.direction = Direction.LEFT
    elif key[pygame.K_d] == True or key[pygame.K_RIGHT] == True:
        snake.direction = Direction.RIGHT
    elif key[pygame.K_w] == True or key[pygame.K_UP] == True:
        snake.direction = Direction.UP
    elif key[pygame.K_s] == True or key[pygame.K_DOWN] == True:
        snake.direction = Direction.DOWN

    snake.Move( MoveRate )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    pygame.display.update()

    # print('Mouse', mouse.body)
    # print('Snake', snake.body)

    clock.tick(60)

pygame.quit()
sys.exit()