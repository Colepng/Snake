import pygame 
from pygame.locals import *
from pygame.rect import *

import game

pygame.init()
count = 1

COLOR = 0,0,0
rect_color = 255,255,255

def calc_in_grid(num_to_round, grid_size):
    return round(num_to_round/grid_size)*grid_size

win_x = calc_in_grid(1000,35)
win_y = calc_in_grid(800,35)

screen = pygame.display.set_mode((win_x, win_y))#sets the windoes size

rect = pygame.Rect(win_x/2 - 100, win_y/2 - 50, 200, 100)
font = pygame.font.Font(pygame.font.get_default_font(), 75)
text = font.render('PLAY', True, COLOR)
text_rect = text.get_rect()

text_rect = (rect.left , rect.centery - text.get_height()/2)
print(rect.top, rect.centery - text.get_height()/2)

while 1:
    screen.fill((100,100,100))
    pygame.draw.rect(screen, rect_color, rect)
    screen.blit(text, text_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos, rect.topleft,rect.bottomright)
        if event.type == MOUSEBUTTONDOWN and count == 1 and rect.topleft < mouse_pos and rect.bottomright > mouse_pos:
            game = game.game()
            game.run()#Runs the run fuctions
            count = 2