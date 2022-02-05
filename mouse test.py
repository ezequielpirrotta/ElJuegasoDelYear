import pygame
import sys
import random

from pygame.constants import K_a
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

pygame.mouse.set_visible(0)
#rect coordinates
axis_x = 10
axis_y = 10

#rect speed
speed_x = 0
speed_y = 0

#main loop

    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        #eventos teclado/mouse
        ######## left and right ########
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                speed_x = -3
            if event.key == pygame.K_d:
                speed_x = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                speed_x = 0
            if event.key == pygame.K_d:
                speed_x = 0
        ######## up and down ##########
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speed_y = -3
            if event.key == pygame.K_s:
                speed_y = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                speed_y = 0
            if event.key == pygame.K_s :
                speed_y = 0
    #Set background
    screen.fill(BLUE)

    #mouse_pos = pygame.mouse.get_pos()
    #x = mouse_pos[0]
    #y = mouse_pos[1]
    
    axis_x += speed_x
    axis_y += speed_y 
    pygame.draw.rect(screen, WHITE, (axis_x, axis_y, 80, 80))

    #refresh window
    pygame.display.flip()
    #clock set on 60 FPS
    clock.tick(60)
        