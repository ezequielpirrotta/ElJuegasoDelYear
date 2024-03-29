import pygame
import sys
pygame.init()

#Define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

wSize = (800, 500)

#crate window
screen = pygame.display.set_mode(wSize)

#control FPS
clock = pygame.time.Clock()

#rect coordinates
axis_x = 400
axis_y = 200

#rect speed
speed_x = 3
speed_y = 3

#main loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if(axis_x > 720 or axis_x < 0):
        speed_x *= -1
    if(axis_y > 320 or axis_y < 0):
        speed_y *= -1
        
    axis_x += speed_x 
    axis_y += speed_y   

    #Set background
    screen.fill(WHITE)

    ######### Drawing zone ##########
    pygame.draw.rect(screen, RED, (axis_x, axis_y, 80, 80))
    
    ######### Drawing zone ##########

    #refresh window
    pygame.display.flip()
    #clock set on 60 FPS
    clock.tick(60)
        