import pygame
import sys
import Models
from Models.Player import Player
pygame.init
from pygame.locals import *
pygame.font.init()

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

## Creating players  ##
player_1 = Player(15,90, WHITE,(50, 300 - (player_height / 2)))
player_2 = Player(15,90, WHITE,(750 - player_width, 300 - (player_height / 2)))


player1_y_speed = 0 
player2_y_speed = 0 

#### Ball coords #####
ball_x = window_width / 2
ball_y = window_height / 2
ball_speed_x = 3
ball_speed_y = 3

## Points system ###
max_points = 7
points_player1 = 0
points_player2 = 0

game_over = False

continue_box = Rect(window_width/2 - 170, window_height/2, 150, 50)
quit_box = Rect(window_width/2 + 20, window_height/2, 150, 50)

font = pygame.font.SysFont("Comic Sans MS", 30)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        ### Movements with keys ###
        # Player 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_y_speed = -3
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
        ### Checking that the players don't pass the borders of the screen ###
        if player_1.pos_y + player_1.height + player1_y_speed > window_height:
            player1_y_speed = 0
            player_1.pos_y = window_height - player_1.height
        if player_1.pos_y + player1_y_speed < 0:
            player1_y_speed = 0
            player_1.pos_y = 0
        if player_2.pos_y + player_2.height + player2_y_speed > window_height:
            player2_y_speed = 0
            player_2.pos_y = window_height - player_2.height
        if player_2.pos_y + player2_y_speed < 0:
            player2_y_speed = 0
            player_2.pos_y = 0
        
    if ball_y > window_height or ball_y < 10:
        ball_speed_y *= -1    
        
    if ball_x > window_width  or ball_x < 0:
        if ball_x > window_width:
            points_player1 += 1
        elif ball_x < 0:
            points_player2 += 1
        ball_x = 400
        ball_y = 300

    ## Move the players ##
    player_1.move(player1_y_speed)
    player_2.move(player2_y_speed)
    ## Move ball ##
    ball_x += ball_speed_x
    ball_y += ball_speed_y


    screen.fill(BLACK)

    ### Drawing zone ###
    text_1 = font.render("Points: "+str(points_player1), True, WHITE)
    text_2 = font.render("Points: "+str(points_player2), True, WHITE)
    screen.blit(text_1, (10, 10))
    screen.blit(text_2, (window_width - 140, 10))

    pygame.draw.rect(screen, WHITE, ((window_width / 2), 0, 1, window_height))
    player_1_box = pygame.draw.rect(screen, WHITE, (player_1.pos_x, player_1.pos_y, player_1.width, player_1.height))
    player_2_box = pygame.draw.rect(screen, WHITE, (player_2.pos_x, player_2.pos_y, player_2.width, player_2.height))
    ball = pygame.draw.circle(screen, WHITE, (ball_x, ball_y), 10)

    # Collisions
    if ball.colliderect(player_1_box) or ball.colliderect(player_2_box):
        ball_speed_x *= -1 
    
    #Lose the game
    if points_player1 < max_points or points_player2 < max_points:
        
        if points_player1 == max_points:
            game_over_text = font.render("Game over! Player 1 wins!!", True, WHITE)
        if points_player2 == max_points:
            game_over_text = font.render("Game over! Player 2 wins!!", True, WHITE)
        
        pygame.draw.rect(screen, BLUE, continue_box, 0)
        pygame.draw.rect(screen, BLUE, quit_box, 0)

        button1_text = font.render("Continue", True, WHITE)
        button2_text = font.render("Quit", True, WHITE)
        screen.blit(button1_text, (window_width/2 - 170 + (continue_box.width - button1_text.get_width())/2, window_height/2))
        screen.blit(button2_text, (window_width/2 + 20 + (quit_box.width - button2_text.get_width())/2, window_height/2))
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.button == 1:
                if continue_box.collidepoint(pygame.mouse.get_pos()):
                    game_over = False
                    points_player1 = 0
                    points_player2 = 0
        
        
        if False :
            game_over = True
    #refresh window
    pygame.display.flip()
    #clock set on 60 FPS
    clock.tick(60)