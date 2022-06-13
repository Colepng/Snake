import pygame
from pygame.locals import *
from pygame.rect import *

import json
import sys

from game import game as game
import setting_menu
from account__screen import login_create_account_screen

def run_game():
    pygame.init()

    BLACK = 0, 0, 0

    # window_sizes = pygame.display.list_modes()
    # screen = pygame.display.set_mode(window_sizes[int(input())], FULLSCREEN)
    logged = json.load(open('logged.json',))
    print(logged)
    setting_file = open('settings.json',) if logged == False else open('account_settings.json',)    
    setting_file_loaded = json.load(setting_file)
    win_x = setting_file_loaded['win_x']
    win_y = setting_file_loaded['win_y']

    screen = pygame.display.set_mode((win_x, win_y))  # sets the windoes size

    play_rect = pygame.Rect(win_x/2 - 200, win_y/2 - 50, 400, 100,)


    font = pygame.font.Font(pygame.font.get_default_font(), 75)
    text = font.render('PLAY', True, BLACK)
    text_rect = text.get_rect()
    text_rect = (play_rect.left + ((play_rect.width - text.get_width())/2), play_rect.centery - text.get_height()/2)


    # Loads the setting icon, sets its size and gets a rect for its
    setting_icon_no_size_change = pygame.image.load(
        "Assests/setting_icon.png").convert_alpha()
    setting_icon = pygame.transform.scale(setting_icon_no_size_change, (50, 50))
    setting_icon_rect = setting_icon.get_rect(x=10, y=10)

    # account screen
    account_screen_rect = pygame.Rect(win_x - 50, 0, 50, 50,)



    while 1:
        screen.fill((0, 255, 0))
        pygame.draw.rect(screen, BLACK, play_rect, width=5)
        pygame.draw.rect(screen, BLACK, account_screen_rect)
        screen.blit(text, text_rect)
        screen.blit(setting_icon, setting_icon_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            logged = json.load(open('logged.json',))
            temp_setting_file = setting_file
            setting_file = open('settings.json',) if logged == False else open('account_settings.json',)
            if temp_setting_file != setting_file:
                setting_file_loaded = json.load(setting_file)
            length = setting_file_loaded['length']
            size = setting_file_loaded['size']
            win_x = setting_file_loaded['win_x']
            win_y = setting_file_loaded['win_y']
            starting_x = setting_file_loaded['starting_x']
            starting_y = setting_file_loaded['starting_y']
            head_colour = setting_file_loaded['head_colour']
            snake_colour_1 = setting_file_loaded['snake_colour_1']
            snake_colour_2 = setting_file_loaded['snake_colour_2']
            if_hex = setting_file_loaded['if_hex']
            speed = setting_file_loaded['speed']
            
            screen = pygame.display.set_mode((win_x, win_y))
            #print(pygame.display.get_window_size(), win_x, win_y)

            if event.type == MOUSEBUTTONDOWN and setting_icon_rect.collidepoint(event.pos):
                setting_menu.run()
                setting_file.close()
                setting_file = open('settings.json',) if logged == False else open('account_settings.json',)
                setting_file_loaded = json.load(setting_file)

                #print(pygame.display.list_modes())

            elif event.type == MOUSEBUTTONDOWN and play_rect.collidepoint(event.pos):
                print(setting_file_loaded,setting_file,logged)
                game().run(screen, length, size, win_x, win_y,starting_x, starting_y,head_colour,snake_colour_1,snake_colour_2,if_hex, speed)  # Runs the run fuctions
                
            elif event.type == MOUSEBUTTONDOWN and account_screen_rect.collidepoint(event.pos):
                login_create_account_screen(screen)
                

            elif event.type == QUIT:
                sys.exit()

# run_game()
