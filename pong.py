import pygame
import sys
pygame.init



#Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

window_height = 600
window_width = 800

player_width = 15
player_height = 90

screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

## Coords and speed of players  ##
player1_x = 50
player1_y = 300 - (player_height / 2)
player1_y_speed = 0 

player2_x = 750 - player_width
player2_y = 300 - (player_height / 2)
player2_y_speed = 0 

#### Ball coords #####
ball_x = window_width / 2
ball_y = window_height / 2
ball_speed_x = 3
ball_speed_y = 3

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        ### Movements with keys ###
        # Player 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_y_speed = -3
            if player1_y + player_height < window_height:
                if event.key == pygame.K_s:
                    player1_y_speed = 3
                
        # Player 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3
        # Player 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
        # Player 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

    if ball_y > window_width or ball_y < 10:
        ball_speed_y *= -1    
        
    if ball_x >= window_height-10  or ball_x <= 10:
        ball_x = 400
        ball_y = 300

    ## Modify the coords to move the players ##
    player1_y += player1_y_speed
    player2_y += player2_y_speed
    ## Move ball ##
    ball_x += ball_speed_x
    ball_y += ball_speed_y


    screen.fill(BLACK)

    ### Drawing zone ###
    player_1 = pygame.draw.rect(screen, WHITE, (player1_x, player1_y, player_width, player_height))
    player_2 = pygame.draw.rect(screen, WHITE, (player2_x, player2_y, player_width, player_height))
    ball = pygame.draw.circle(screen, WHITE, (ball_x, ball_y), 10)

    # Collisions
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1 
    #refresh window
    pygame.display.flip()
    #clock set on 60 FPS
    clock.tick(60)