from time import sleep
import pygame 
from pygame.locals import *
from pygame.rect import *
import json

from game import game
import setting_menu
import snake

pygame.init()
count = 1

COLOR = 0,0,0
rect_color = 0,0,0

# window_sizes = pygame.display.list_modes()
# screen = pygame.display.set_mode(window_sizes[int(input())], FULLSCREEN)

setting = open('settings.json',)
setting_json = json.load(setting)
win_x = setting_json['win_x']
win_y = setting_json['win_y']

screen = pygame.display.set_mode((win_x,win_y))#sets the windoes size

rect = pygame.Rect(win_x/2 - 200, win_y/2 - 50, 400, 100,)
font = pygame.font.Font(pygame.font.get_default_font(), 75)
text = font.render('PLAY', True, COLOR)
text_rect = text.get_rect()

text_rect = (rect.left + ((rect.width - text.get_width())/2), rect.centery - text.get_height()/2)
#print(rect.top, rect.centery - text.get_height()/2)

setting_icon_no_size_change = pygame.image.load("Assests/setting_icon.png").convert_alpha()
setting_icon = pygame.transform.scale(setting_icon_no_size_change,(50,50))
setting_icon_rect = setting_icon.get_rect(x=10,y=10)
# while 1:
#     print(snake.Snake.SIZE)
#     print()
while 1:
    screen.fill((0,255,0))
    pygame.draw.rect(screen, rect_color, rect, width=5)
    screen.blit(text, text_rect)
    screen.blit(setting_icon,setting_icon_rect)
    pygame.display.flip()


    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        length = setting_json['length']
        size = setting_json['size']
        win_x = setting_json['win_x']
        win_y = setting_json['win_y']
        starting_x = setting_json['starting_x']
        starting_y = setting_json['starting_y']
        screen = pygame.display.set_mode((win_x, win_y))
        print(pygame.display.get_window_size(), win_x, win_y)
        #print(size,length)

        if event.type == MOUSEBUTTONDOWN and setting_icon_rect.collidepoint(event.pos):
            setting_menu.run()
            setting.close()
            setting = open('settings.json',)
            setting_json = json.load(setting)
            
            print(pygame.display.list_modes())


        if event.type == MOUSEBUTTONDOWN and rect.collidepoint(event.pos):
                
                game().run(screen, length,size, win_x, win_y, starting_x, starting_y)#Runs the run fuctions
                count = 2