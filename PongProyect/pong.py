import pygame
import sys
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
#start_bg_img = pygame.image.load('images/star_night_resize_800x600.gif')
#start_bg_img = pygame.transform.scale(start_bg_img,(window_width,window_height))

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
max_points = 3

continue_box = Rect(window_width/2 - 170, window_height/2, 150, 50)
quit_box = Rect(window_width/2 + 20, window_height/2, 150, 50)
font_1 = pygame.font.SysFont("Comic Sans MS", 30)
game_over_box = Rect(window_width/2 - 237/2, window_height/2 + 20 - 150, 237, 50)
font_2 = pygame.font.SysFont("Comic Sans MS", 20)
#game_menu_box = Rect(window_width/2 , window_height/2 , 237, 30)
font_3 = pygame.font.SysFont("Comic Sans MS", 50)

### Functions ###
##def draw_text(screen, font, text, text_colour, pos):


def show_start_menu():
    
    global ball_speed_x
    global ball_speed_y
    global running
    #screen.fill()
    title_text = font_3.render("Pong", True, WHITE)
    button1_text = font_1.render("Play", True, WHITE)
    button2_text = font_1.render("Quit", True, WHITE)
    
    pygame.draw.rect(screen, BLUE, continue_box, 0)
    pygame.draw.rect(screen, BLUE, quit_box, 0)
    screen.blit(title_text, ((window_width/2 - title_text.get_width()/2) , 60))
    screen.blit(button1_text, (window_width/2 - 170  + (continue_box.width - button1_text.get_width())/2, window_height/2))
    screen.blit(button2_text, (window_width/2 + 20 + (quit_box.width - button2_text.get_width())/2, window_height/2))
    pygame.display.flip()
    
    waiting = True

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.BUTTON_LEFT:
                if continue_box.collidepoint(pygame.mouse.get_pos()):
                    print("llegué")
                    player_1.set_default()
                    player_2.set_default()
                    ball_speed_x = 3
                    ball_speed_y = 3
                    waiting = False
                    running = True
                elif quit_box.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()


def show_game_over():
    

    global player_1
    global player_2
    global ball_speed_x
    global ball_speed_y
    global running
    
    if player_1.points == max_points:
        game_over_text = font_2.render("Game over! Player 1 wins!!", True, WHITE)
    if player_2.points == max_points:
        game_over_text = font_2.render("Game over! Player 2 wins!!", True, WHITE)
    #print(game_over_text.get_width())
    pygame.draw.rect(screen, BLUE, game_over_box, 0)
    screen.blit(game_over_text, ((window_width/2 -237/2) + (game_over_box.width - game_over_text.get_width())/2, window_height/2 - 130))
    
    pygame.draw.rect(screen, BLUE, continue_box, 0)
    pygame.draw.rect(screen, BLUE, quit_box, 0)
    button1_text = font_1.render("Continue", True, WHITE)
    button2_text = font_1.render("Quit", True, WHITE)
    screen.blit(button1_text, (window_width/2 - 170 + (continue_box.width - button1_text.get_width())/2, window_height/2))
    screen.blit(button2_text, (window_width/2 + 20 + (quit_box.width - button2_text.get_width())/2, window_height/2))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.BUTTON_LEFT:
                if continue_box.collidepoint(pygame.mouse.get_pos()):
                    player_1.set_default()
                    player_2.set_default()
                    ball_speed_x = 3
                    ball_speed_y = 3
                    waiting = False
                elif quit_box.collidepoint(pygame.mouse.get_pos()):
                    running = False
                    waiting = False



game_over = False
running = False

if(not running):
    show_start_menu()
    screen.fill((BLACK))
    pygame.display.flip()
print(running)
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
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
    
    #last_to_hit = 0   
    if ball_x > window_width  or ball_x < 0:
        if ball_x > window_width:
            player_1.point()
            #last_to_hit = 1   
        elif ball_x < 0:
            player_2.point()
            #last_to_hit = 2   
        ball_x = 400
        ball_y = 300
        #ball = pygame.draw.circle(screen, WHITE, (ball_x, ball_y), 10)
        #pygame.display.flip()

        #waiting = True
        #while waiting:
        #    for event in pygame.event.get():
        #        if event.type == pygame.KEYDOWN:
        #            
        #            waiting = False
                        

    ## Move the players ##
    player_1.move(player1_y_speed)
    player_2.move(player2_y_speed)
    ## Move ball ##
    ball_x += ball_speed_x
    ball_y += ball_speed_y


    screen.fill(BLACK)

    ### Drawing zone ###
    text_1 = font_1.render("Points: "+str(player_1.points), True, WHITE)
    text_2 = font_1.render("Points: "+str(player_2.points), True, WHITE)
    screen.blit(text_1, (10, 10))
    screen.blit(text_2, (window_width - 140, 10))

    pygame.draw.rect(screen, WHITE, ((window_width / 2), 0, 1, window_height))
    player_1_box = pygame.draw.rect(screen, WHITE, (player_1.pos_x, player_1.pos_y, player_1.width, player_1.height))
    player_2_box = pygame.draw.rect(screen, WHITE, (player_2.pos_x, player_2.pos_y, player_2.width, player_2.height))
    ball = pygame.draw.circle(screen, WHITE, (ball_x, ball_y), 10)

    # Collisions
    if ball.colliderect(player_1_box) or ball.colliderect(player_2_box):
        ball_speed_x *= -1 
    
    #refresh window
    pygame.display.flip()
    
    #Lose the game
    if player_1.points == max_points or player_2.points == max_points:
        game_over = True
        ball_speed_x = 0
        ball_speed_y = 0
        ball_x = window_width / 2
        ball_y = window_height / 2
        
        show_game_over()
        
    #refresh window
    pygame.display.flip()
    #clock set on 60 FPS
    clock.tick(60)

    if(not running):
        screen.fill((BLACK))
        pygame.display.flip()
        show_start_menu()
        screen.fill((BLACK))
        pygame.display.flip()
        
