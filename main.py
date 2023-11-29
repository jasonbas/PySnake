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

        x = WindowWidth / 2
        y = WindowHeight / 2
        self.segments = [pygame.Rect(( x, y, BodySize, BodySize )),
                         pygame.Rect(( x - BodySize, y, BodySize, BodySize )),
                         pygame.Rect(( x - BodySize * 2, y, BodySize, BodySize ))]

        self.direction = Direction.UNDEFINED
        self.requestedDirection = Direction.UNDEFINED
        self.changingDirection = False
        self.GrowthRemaining = 0
        
    def ChangeDirection( self, direction ):
        if self.direction is direction:
            return
        
        if self.direction is Direction.UNDEFINED:
            if direction is Direction.LEFT: #Can't start game moving left
                return
        
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

    def Move( self ):
        if self.direction == Direction.UNDEFINED:
            return

        #Change direction if needed
        head = self.segments[0]
        if self.changingDirection is True:
            remainder = -1
            if self.direction == Direction.RIGHT or self.direction == Direction.LEFT:
                remainder = head.width % BodySize
            else:
                remainder = head.height % BodySize 
            
            if remainder == 0:
                self.direction = self.requestedDirection
                self.changingDirection = False
        
        self.UpdateSegments()
    
    def UpdateSegments( self ):
        self.UpdateHead()

        if self.GrowthRemaining <= 0:
            self.UpdateTail()
        else:
            self.GrowthRemaining = self.GrowthRemaining - MoveRate

    def UpdateHead( self ):
        head = self.segments[0]
        if self.direction == Direction.LEFT:
            if head.width % BodySize == 0:
                self.segments.insert(0,pygame.Rect(head.left - MoveRate, head.top, MoveRate, BodySize))
            else:
                head.update( head.left - MoveRate, head.top, head.width + MoveRate, head.height)
        elif self.direction == Direction.RIGHT:
            if head.width % BodySize == 0:
                self.segments.insert(0,pygame.Rect(head.left + BodySize, head.top, MoveRate, BodySize))
            else:
                head.update( head.left, head.top, head.width + MoveRate, head.height)
        elif self.direction == Direction.UP:
            if head.height % BodySize == 0:
                self.segments.insert(0,pygame.Rect(head.left, head.top - MoveRate, BodySize, MoveRate))
            else:
                head.update( head.left, head.top - MoveRate, head.width, head.height + MoveRate)
        elif self.direction == Direction.DOWN:
            if head.height % BodySize == 0:
                self.segments.insert(0,pygame.Rect(head.left, head.top + BodySize, BodySize, MoveRate))
            else:
                head.update( head.left, head.top, head.width, head.height + MoveRate)


    def UpdateTail( self ):
        tail = self.segments[len(self.segments) - 1]
        segmentBeforeTail = self.segments[len(self.segments) - 2]
        decayDirection = self.DirectionOfNextSegment(tail, segmentBeforeTail)

        if decayDirection is Direction.LEFT:
            if tail.width == MoveRate:
                self.segments.remove(tail)
            else:
                tail.update( tail.left, tail.top, tail.width - MoveRate, tail.height)
        elif decayDirection is Direction.RIGHT:
            if tail.width == MoveRate:
                self.segments.remove(tail)
            else:
                tail.update( tail.left + MoveRate, tail.top, tail.width - MoveRate, tail.height)
        elif decayDirection is Direction.UP:
            if tail.height == MoveRate:
                self.segments.remove(tail)
            else:
                tail.update( tail.left, tail.top, tail.width, tail.height - MoveRate)                
        elif decayDirection is Direction.DOWN:
            if tail.height == MoveRate:
                self.segments.remove(tail)
            else:
                tail.update( tail.left, tail.top + MoveRate, tail.width, tail.height - MoveRate)

    def DirectionOfNextSegment( self, currSegment, nextSegment ):
        if currSegment.left - nextSegment.left == 0 and currSegment.top - nextSegment.top > 0:
            return Direction.UP
        elif currSegment.left - nextSegment.left == 0 and currSegment.top - nextSegment.top < 0:
            return Direction.DOWN
        elif currSegment.left - nextSegment.left > 0 and currSegment.top - nextSegment.top == 0:
            return Direction.LEFT
        elif currSegment.left - nextSegment.left < 0 and currSegment.top - nextSegment.top == 0:
            return Direction.RIGHT
        else:
            return Direction.UNDEFINED

    def StartGrowing( self ):
        self.GrowthRemaining = BodySize

    def IsColliding( self ):
        head = self.segments[0]
        for segment in self.segments[1:]:
            if head.colliderect(segment):
                return True
            
        if self.direction == Direction.LEFT:
            if self.segments[0].left < 0:
                return True
        elif self.direction == Direction.RIGHT:
            if self.segments[0].right > WindowWidth:
                return True
        elif self.direction == Direction.UP:
            if self.segments[0].top < 0:
                return True
        elif self.direction == Direction.DOWN:
            if self.segments[0].bottom > WindowHeight:
                return True
            
        return False

pygame.init()

#Defines
WindowWidth = 640
WindowHeight = 480
BodySize = 20
MoveRate = 2
MiceEaten = 0

screen = pygame.display.set_mode((WindowWidth, WindowHeight))

display = "PySnake ----- Mice Eaten: %d" % MiceEaten
pygame.display.set_caption(display) 

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

    #Move snake
    snake.Move()

    #Check if snake is eating mouse
    snakeHead = snake.segments[0]
    if snakeHead.colliderect( mouse.body ):
        mouse = Mouse()
        snake.StartGrowing()

        #Update window with score
        MiceEaten += 1        
        display = "PySnake ----- Mice Eaten: %d" % MiceEaten
        pygame.display.set_caption(display) 

        #Find a spawn spot for mouse not on snake body
        keepSpawningMouse = True
        while keepSpawningMouse:
            respawned = False
            for segment in snake.segments:
                if segment.colliderect( mouse.body ):
                    mouse = Mouse()
                    respawned = True
                
            if respawned is False:
                keepSpawningMouse = False
    
    screen.fill((0, 0, 0))

    for segment in snake.segments:
        pygame.draw.rect(screen, (0,255,0), segment)

    pygame.draw.rect(screen, (255,255,255), mouse.body)

    pygame.display.update()

    clock.tick(60)
    
    if snake.IsColliding():
        playing = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

pygame.quit()
sys.exit()