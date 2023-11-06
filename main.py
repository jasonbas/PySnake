import pygame
import sys

pygame.init()

WindowWidth = 640
WindowHeight = 480

screen = pygame.display.set_mode((WindowWidth, WindowHeight))

player = pygame.Rect((300,250,50,50))

clock = pygame.time.Clock()

moveRate = 10

playing = True
while playing:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255,0,0), player)

    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True or key[pygame.K_LEFT] == True:
        if player.left >= moveRate:
            player.move_ip(-moveRate, 0)
    elif key[pygame.K_d] == True or key[pygame.K_RIGHT] == True:
        if player.right <= WindowWidth - moveRate:
            player.move_ip( moveRate, 0)
    elif key[pygame.K_w] == True or key[pygame.K_UP] == True:
        if player.top >= moveRate:
            player.move_ip( 0, -moveRate)
    elif key[pygame.K_s] == True or key[pygame.K_DOWN] == True:
        if player.bottom <= WindowHeight - moveRate:
            player.move_ip( 0, moveRate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    pygame.display.update()

    clock.tick(30)
    fps = clock.get_fps()

pygame.quit()
sys.exit()