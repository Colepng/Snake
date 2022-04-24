import pygame 
from pygame.locals import *
from pygame.rect import *

import game
import json

pygame.init()
count = 1

COLOR = 0,0,0
rect_color = 0,0,0

setting = open('settings.json',)
setting_json = json.load(setting)
win_x = setting_json['win_x']
win_y = setting_json['win_y']
 
screen = pygame.display.set_mode((win_x, win_y))#sets the windoes size

rect = pygame.Rect(win_x/2 - 200, win_y/2 - 50, 400, 100,)
font = pygame.font.Font(pygame.font.get_default_font(), 75)
text = font.render('PLAY', True, COLOR)
text_rect = text.get_rect()

text_rect = (rect.left + ((rect.width - text.get_width())/2), rect.centery - text.get_height()/2)
#print(rect.top, rect.centery - text.get_height()/2)

while 1:
    screen.fill((0,255,0))
    pygame.draw.rect(screen, rect_color, rect, width=5)
    screen.blit(text, text_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos[0],mouse_pos[1] , rect.x, rect.y, rect.x + rect.width, rect.y + rect.height)
        if count == 1 and event.type == MOUSEBUTTONDOWN and mouse_pos[0] > rect.x and mouse_pos[1] > rect.y and mouse_pos[0] < rect.x + rect.width and mouse_pos[1] < rect.y + rect.height:
            game = game.game()
            game.run()#Runs the run fuctions
            count = 2