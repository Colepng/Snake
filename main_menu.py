import pygame
from pygame.locals import *
from pygame.rect import *

import json
import sys
import sqlite3 as sql

from game import game as game
import setting_menu
from account__screen import login_create_account_screen
from fun import calc_mid_of_rect_for_text


def write_leaderboard(screen, names, scores, leaderboard_rect):
    font_small = pygame.font.Font(pygame.font.get_default_font(), 36)
    texts = []
    pos = leaderboard_rect.top + 10
    #print(leaderboard_rect.topleft)
    for i in range(len(names)):
    #     font_small.render(names[i], scores[i], (255, 255, 255))
        #print(names[i], scores[i])
        texts.append(font_small.render(names[i] + " " + str(scores[i]), True, (0, 0, 0)))
    for i in texts:
        screen.blit(i, (leaderboard_rect.left + 10, pos))
        pos += 50
    
def get_users_and_scores():
    con = sql.connect("Snake.sqlite3")
    cur = con.cursor()
    get_users= "SELECT username FROM Snake ORDER BY highscore DESC LIMIT 10"
    cur.execute(get_users)
    users_sql = cur.fetchall()
    users = []
    for i in users_sql:
        users.append(i[0])
    #print(users)
    get_highscore= "SELECT highscore FROM Snake ORDER BY highscore DESC LIMIT 10"
    cur.execute(get_highscore)
    highscores_sql = cur.fetchall()
    highscores = []
    for i in highscores_sql:
        highscores.append(i[0])
    #print(highscores)
    return users, highscores



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
    font_small = pygame.font.Font(pygame.font.get_default_font(), 36)
    text = font.render('PLAY', True, BLACK)
    text_rect = text.get_rect()
    text_rect = (play_rect.left + ((play_rect.width - text.get_width())/2), play_rect.centery - text.get_height()/2)


    # Loads the setting icon, sets its size and gets a rect for its
    # setting_icon_no_size_change = pygame.image.load(
    #     "Assests/setting_icon.png").convert_alpha()
    # setting_icon = pygame.transform.scale(setting_icon_no_size_change, (50, 50))
    # setting_icon_rect = setting_icon.get_rect(x=10, y=10)
    setting_rect = pygame.Rect(0, 0, 200, 50)
    setting_surface = font_small.render("Settings", True, BLACK)

    # account screen
    account_screen_rect = pygame.Rect(win_x - 200, 0, 200, 50)
    account_surface = font_small.render("Account", True, BLACK)

    # leaderboard
    leaderboard_rect = pygame.Rect(win_x - 250, 200, 200, 600)
    leaderboard_rect = pygame.Rect(win_x - 250, (win_y-leaderboard_rect.height)/2, 200, 600)
    leadboard_text = font_small.render('Leaderboard', True, BLACK)
    leadboard_text_rect = leadboard_text.get_rect()
    top_10_text = font_small.render('Top 10', True, BLACK)
    top_10_text_rect = top_10_text.get_rect()

    pygame.display.set_caption('Snake')
    while 1:
        screen.fill((0, 255, 0))
        users, scores = get_users_and_scores()
        write_leaderboard(screen, users, scores, leaderboard_rect)
        pygame.draw.rect(screen, BLACK, play_rect, width=5)
        pygame.draw.rect(screen, BLACK, account_screen_rect, 5, 5)
        pygame.draw.rect(screen, BLACK, leaderboard_rect, width=5)
        screen.blit(text, text_rect)
        pygame.draw.rect(screen, BLACK, setting_rect, 5, 5)
        screen.blit(setting_surface, calc_mid_of_rect_for_text(setting_rect, setting_surface))
        screen.blit(account_surface, calc_mid_of_rect_for_text(account_screen_rect, account_surface))
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

            if event.type == MOUSEBUTTONDOWN and setting_rect.collidepoint(event.pos):
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
