import pygame 
from pygame.locals import *
from pygame.rect import *
import json

import settings

    #make setting menu to look better

def run():
    clock = pygame.time.Clock()

    setting = open('settings.json',)
    setting_json = json.load(setting)
    win_x = setting_json['win_x']
    win_y = setting_json['win_y']

    pygame.font.init()

    screen = pygame.display.set_mode((win_x, win_y))


    base_font = pygame.font.Font(None, 32)
    length_input_text = str(setting_json['length'])
    size_input_text = str(setting_json['size'])
    user_text = [size_input_text,length_input_text]

    size_input_rect = pygame.Rect(setting_json['starting_x'], setting_json['starting_y'], 140, 32)
    length_input_rect = pygame.Rect(setting_json['starting_x'], setting_json['starting_y']+size_input_rect.height + 10, 140, 32)

    apply_rect = pygame.Rect(500,700,140,32)

    input_rects = [size_input_rect,length_input_rect]

    color_active = pygame.Color('lightskyblue3')

    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    active = False

    while True:
        #if loop == False:break
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(input_rects)):
                    if input_rects[i].collidepoint(event.pos):
                        print(input_rects[i].collidepoint(event.pos), i)
                        active = True
                        hit_rect = i
                        break
                    #else:
                        #print(input_rects[i].collidepoint(event.pos), i)

                    if not input_rects[i].collidepoint(event.pos):
                        active = False

                if apply_rect.collidepoint(event.pos):
                    settings.write(size=int(user_text[0]), length=int(user_text[1]))
                    return print('exit')
    
            if event.type == KEYDOWN and active == True:
                text = event.unicode
                #print(text)
                # Check for backspace
                if event.key == K_BACKSPACE:
    
                    # get text input from 0 to -1 i.e. end.
                    user_text[hit_rect] = user_text[hit_rect][:-1]
                
                elif text.isdigit() == True:
                    user_text[hit_rect] += text
                    #print(user_text[hit_rect])
        screen.fill((255, 255, 255, 100))
    
        if active:
            color = color_active
        else:
            color = color_passive

        for i in range(len(input_rects)):
            pygame.draw.rect(screen, color, input_rects[i], width=5)
        
        pygame.draw.rect(screen,color, apply_rect, width=5)
        pygame.draw.line(screen, (255,0,0), (100,0), (100,win_y), width=5)
        size_surface = base_font.render('size', True, (0,0,0))
        length_surface = base_font.render('length', True, (0,0,0))
        apply_surface = base_font.render('apply', True, (0,0,0))
        #print(user_text[0])
        size_input_surface = base_font.render(user_text[0], True, (0, 0, 0))
        #print(user_text[1])
        length_input_surface = base_font.render(user_text[1], True, (0, 0, 0))
        screen.blit(size_input_surface, (size_input_rect.x+5, size_input_rect.y+5))
        screen.blit(size_surface, (size_input_rect.x - size_surface.get_width(), size_input_rect.y))
        screen.blit(length_input_surface, (length_input_rect.x+5, length_input_rect.y+5))
        screen.blit(length_surface, (length_input_rect.x - length_surface.get_width(), length_input_rect.y))
        screen.blit(apply_surface,(apply_rect.topleft))
        #input_rect.w = max(100, text_surface.get_width()+10)
        pygame.display.flip()
    
        clock.tick(60)