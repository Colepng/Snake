import pygame
import json


import snake
from pygame.locals import *

pygame.init()

def pause_menu(surface,win_x,win_y,starting_x, starting_y):
        black = (0,0,0)
        run = True
        gap = 75

        font = pygame.font.Font(pygame.font.get_default_font(), 50)

        resume_rect = pygame.Rect(starting_x, starting_y, 275,100)
        resume_rect = pygame.Rect(starting_x - resume_rect.width/2, starting_y - gap, resume_rect.width, resume_rect.height)
        resume_text = font.render('Resume', True, black)
        

        main_menu_rect = pygame.Rect(starting_x, starting_y, 275,100)
        main_menu_rect = pygame.Rect(resume_rect.x, starting_y + gap, main_menu_rect.width,main_menu_rect.height)
        main_menu_text = font.render('Main Menu', True, black)


        while run:
            pygame.draw.rect(surface, black, resume_rect, width=5)
            pygame.draw.rect(surface, black, main_menu_rect, width=5)
            surface.blit(resume_text, (resume_rect.left + resume_rect.width/2 - resume_text.get_width()/2,(resume_rect.y + resume_rect.height/2)  - resume_text.get_height()/2))
            surface.blit(main_menu_text, (main_menu_rect.x,(main_menu_rect.y + main_menu_rect.height/2)  - main_menu_text.get_height()/2))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and resume_rect.collidepoint(event.pos):
                    print("TEST")
                    run = False

                if event.type == MOUSEBUTTONDOWN and main_menu_rect.collidepoint(event.pos):
                    print('main menu')
                    snake.running = False
                    return 
