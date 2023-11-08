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
        self.body = pygame.Rect((random.randrange( 0, WindowWidth - BodySize, BodySize), 
                                 random.randrange( 0, WindowHeight - BodySize, BodySize), 
                                 BodySize, 
                                 BodySize ))

class Snake:
    def __init__( self ):
        self.body = pygame.Rect(( WindowWidth / 2, WindowHeight / 2, 
                                 BodySize, BodySize ))        
        self.direction = Direction.UNDEFINED
        self.requestedDirection = Direction.UNDEFINED
        self.changingDirection = False
        
    def ChangeDirection( self, direction ):
        if self.direction is direction:
            return
        
        if self.direction is Direction.UNDEFINED:
            self.direction = direction
            return
        
        if self.direction is Direction.DOWN and direction is Direction.UP:
            return
        elif self.direction is Direction.UP and direction is Direction.DOWN:
            return
        elif self.direction is Direction.LEFT and direction is Direction.RIGHT:
            return
        elif self.direction is Direction.RIGHT and direction is Direction.LEFT:
            return
        
        self.requestedDirection = direction
        self.changingDirection = True

    def Move( self, moveRate ):
        if self.direction == Direction.UNDEFINED:
            return

        if self.changingDirection is True:
            if self.direction == Direction.RIGHT or self.direction == Direction.LEFT:
                remainder = self.body.left % BodySize
                if remainder is 0:
                    self.direction = self.requestedDirection
                    self.changingDirection = False          
            if self.direction == Direction.UP or self.direction == Direction.DOWN:
                remainder = self.body.top % BodySize
                if remainder is 0:
                    self.direction = self.requestedDirection
                    self.changingDirection = False                  

        #Move snake body
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
BodySize = 20
MoveRate = 4

screen = pygame.display.set_mode((WindowWidth, WindowHeight))
pygame.display.set_caption('Snake')

snake = Snake()
mouse = Mouse()

clock = pygame.time.Clock()

playing = True
while playing:

    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True or key[pygame.K_LEFT] == True:
        snake.ChangeDirection( Direction.LEFT )
    elif key[pygame.K_d] == True or key[pygame.K_RIGHT] == True:
        snake.ChangeDirection( Direction.RIGHT )
    elif key[pygame.K_w] == True or key[pygame.K_UP] == True:
        snake.ChangeDirection( Direction.UP )
    elif key[pygame.K_s] == True or key[pygame.K_DOWN] == True:
        snake.ChangeDirection( Direction.DOWN )

    snake.Move( MoveRate )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0,255,0), snake.body)
    pygame.draw.rect(screen, (255,255,255), mouse.body)

    pygame.display.update()

    # print('Mouse', mouse.body)
    # print('Snake', snake.body)

    clock.tick(60)

pygame.quit()
sys.exit()