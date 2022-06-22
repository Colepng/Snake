#
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
    #Makes a list of the different rendered texts
    for i in range(len(names)):
        texts.append(font_small.render(names[i] + " " + str(scores[i]), True, (0, 0, 0)))
    #Draws all the text
    for i in texts:
        screen.blit(i, (leaderboard_rect.left + 10, pos))
        pos += 50

def get_users_and_scores():
    #Connects to the database
    con = sql.connect("Snake.sqlite3")
    cur = con.cursor()

    get_users = "SELECT username FROM Snake ORDER BY highscore DESC LIMIT 10"
    cur.execute(get_users)#Execute sql code
    users_sql = cur.fetchall()#Gets what the sql code returend
    users = []
    #Make a list of the users
    for i in users_sql:
        users.append(i[0])
    get_highscore= "SELECT highscore FROM Snake ORDER BY highscore DESC LIMIT 10"
    cur.execute(get_highscore)#Execute sql code
    highscores_sql = cur.fetchall()#Gets what the sql code returend
    highscores = []
    #Makes a list of the highscores
    for i in highscores_sql:
        highscores.append(i[0])
    #print(highscores)
    return users, highscores


#Main menu
def run_game():
    #Starts pygame
    pygame.init()
    
    BLACK = (0, 0, 0)

    #Gets if a user is logged in or not
    logged = json.load(open('logged.json',))
    print(logged)

    #Open either the account settings file or local settings file depending if a user is logged in
    setting_file = open('settings.json',) if logged == False else open('account_settings.json',)    
    setting_file_loaded = json.load(setting_file)
    win_x = setting_file_loaded['win_x']
    win_y = setting_file_loaded['win_y']

    #Sets the sreen varible to the pygame window and sets the window's caption
    screen = pygame.display.set_mode((win_x, win_y))
    pygame.display.set_caption('Snake')

    #Two constents one for smaller text and one for larger text
    font = pygame.font.Font(pygame.font.get_default_font(), 75)
    font_small = pygame.font.Font(pygame.font.get_default_font(), 36)\
    
    #Play again rect and renders the text 
    play_rect = pygame.Rect(0, 0, 400, 100)
    play_rect.center = screen.get_rect().center
    play_surface = font.render('PLAY', True, BLACK)

    #Settings rect and renders the text    
    setting_rect = pygame.Rect(0, 0, 200, 50)
    setting_surface = font_small.render("Settings", True, BLACK)

    # account screen
    account_screen_rect = pygame.Rect(win_x - 200, 0, 200, 50)
    account_surface = font_small.render("Account", True, BLACK)

    # leaderboard
    leaderboard_rect = pygame.Rect(win_x - 250, 200, 200, 600)
    leaderboard_rect = pygame.Rect(win_x - 250, (win_y-leaderboard_rect.height)/2, 200, 600)
    top_10_text = font_small.render('Top 10', True, BLACK)
    top_10_text_rect = top_10_text.get_rect()
    top_10_text_rect.centerx, top_10_text_rect.centery = leaderboard_rect.centerx, leaderboard_rect.top - top_10_text.get_height() + 10



    while 1:
        #Fills the screen
        screen.fill((0, 255, 0))

        #Gets the top 10 users and there highscores and draws it 
        users, scores = get_users_and_scores()
        write_leaderboard(screen, users, scores, leaderboard_rect)

        #Draws the rectangles
        pygame.draw.rect(screen, BLACK, play_rect, width=5)
        pygame.draw.rect(screen, BLACK, account_screen_rect, 5, 5)
        pygame.draw.rect(screen, BLACK, leaderboard_rect, width=5)
        pygame.draw.rect(screen, BLACK, setting_rect, 5, 5)

        #Draws the text
        screen.blit(play_surface, calc_mid_of_rect_for_text(play_rect, play_surface))
        screen.blit(setting_surface, calc_mid_of_rect_for_text(setting_rect, setting_surface))
        screen.blit(account_surface, calc_mid_of_rect_for_text(account_screen_rect, account_surface))
        screen.blit(top_10_text, top_10_text_rect)

        #Updates the display
        pygame.display.flip()

        #Setting the varibales to the data from the json file
        logged = json.load(open('logged.json'))
        setting_file = open('settings.json') if logged == False else open('account_settings.json')
        setting_file_loaded = json.load(setting_file)
        setting_file.close()
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
        
        for event in pygame.event.get():

            #Checks if the event is a click and what rectangles was clicked on
            if event.type == MOUSEBUTTONDOWN and setting_rect.collidepoint(event.pos):
                #Setting menu
                setting_menu.run()

            elif event.type == MOUSEBUTTONDOWN and play_rect.collidepoint(event.pos):
                #Starts the game
                game().run(screen, length, size, win_x, win_y,starting_x, starting_y,head_colour,snake_colour_1,snake_colour_2,if_hex, speed)
                
            elif event.type == MOUSEBUTTONDOWN and account_screen_rect.collidepoint(event.pos):
                login_create_account_screen(screen)
                
            #Checks if the event is a quit event
            elif event.type == QUIT:
                #Exits the program
                sys.exit()
