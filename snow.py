import pygame
import sys
import random
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

#main loop
circles = []
for i in range(60):
    x = random.randint(0, 800)
    y = random.randint(0, 500)
    circles.append([x, y])
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Set background
    screen.fill(BLUE)

    ######### Drawing zone ##########
    for coord in circles:
        pygame.draw.circle(screen, WHITE, coord, 2)
        coord[1] += 1
        reach_top = coord[1] > 500
        if(reach_top):
            coord[1] = 0
        
    
    ######### Drawing zone ##########
    #refresh window
    pygame.display.flip()
    #clock set on 60 FPS
    clock.tick(60)
        

#if(axis_x > 720 or axis_x < 0):
#    speed_x *= -1
#if(axis_y > 320 or axis_y < 0):
#    speed_y *= -1
#    
#axis_x += speed_x 
#axis_y += speed_y