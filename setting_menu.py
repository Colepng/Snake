import pygame 
from pygame.locals import *
from pygame.rect import *

import json

import settings

    #make setting menu to look better

def calc_mid_of_rect_for_text(outside_rect, text):
    return ((outside_rect.width - text.get_width())/2 + outside_rect.x, (outside_rect.height - text.get_height())/2 + outside_rect.y)
            

def calc_offset_of_outside_text(rect, text):
    return (rect.x - text.get_width(),(rect.height - text.get_height())/2 + rect.y)
    #(head_colour_input_rect.x - head_colour_surface.get_width(),head_colour_input_rect.height - head_colour_surface.get_height()/2 + head_colour_input_rect.y))

def list_into_str(head_colour):
    first_run = True
    testing = ''
    for i in range(len(head_colour)):
        if first_run ==  True:
            testing = testing + str(head_colour[i])
            first_run = False
        else:
            testing = testing + ',' + str(head_colour[i])
    return testing


def run():
    clock = pygame.time.Clock()

    setting = open('settings.json',)
    setting_json = json.load(setting)
    win_x = setting_json['win_x']
    win_y = setting_json['win_y']
    starting_x = setting_json['starting_x']
    starting_y = setting_json['starting_y']
    length = setting_json['length']
    size = setting_json['size']
    if_hex = setting_json['if_hex']
    head_colour = setting_json['head_colour']
    snake_colour_1 = setting_json['snake_colour_1']
    snake_colour_2 = setting_json['snake_colour_2']
    
    rect_width = 140
    rect_hight = 32
    BLACK = (0,0,0)


    pygame.font.init()

    screen = pygame.display.set_mode((win_x, win_y))

    base_font = pygame.font.Font(None, 32)
    

    length_input_text = str(length)
    size_input_text = str(size)

    head_colour_input_text = list_into_str(head_colour)
    snake_colour_1_input_text = list_into_str(snake_colour_1)
    snake_colour_2_input_text = list_into_str(snake_colour_2)


    user_text = [size_input_text,length_input_text,head_colour_input_text,snake_colour_1_input_text,snake_colour_2_input_text]

    size_input_rect = pygame.Rect(starting_x, starting_y, rect_width, rect_hight)
    length_input_rect = pygame.Rect(starting_x, size_input_rect.bottom + 10, rect_width, rect_hight)

    head_colour_input_rect = pygame.Rect(starting_x, length_input_rect.bottom + 10,rect_width, rect_hight)
    snake_colour_1_input_rect = pygame.Rect(starting_x, head_colour_input_rect.bottom + 10, rect_width, rect_hight)
    snake_colour_2_input_rect = pygame.Rect(starting_x, snake_colour_1_input_rect.bottom + 10, rect_width, rect_hight)


    apply_rect = pygame.Rect(500,700,140,32)

    input_rects = [size_input_rect,length_input_rect, head_colour_input_rect, snake_colour_1_input_rect, snake_colour_2_input_rect]

    color_active = pygame.Color('lightskyblue3')

    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    active = False

    while True:

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(input_rects)):
                    if input_rects[i].collidepoint(event.pos):
                        print(input_rects[i].collidepoint(event.pos), i)
                        active = True
                        hit_rect = i
                        break
                    

                    if not input_rects[i].collidepoint(event.pos):
                        active = False

                if apply_rect.collidepoint(event.pos):

                    snake_colour_1_input_text = user_text[3].split(',')
                    snake_color_1_list_int = [int(x) for x in snake_colour_1_input_text]

                    head_colour_input_text_list_str = user_text[2].split(',')
                    head_color_list_int = [int(x) for x in head_colour_input_text_list_str]

                    settings.write(size=int(user_text[0]), length=int(user_text[1]), head_colour = head_color_list_int, snake_colour_1=snake_color_1_list_int)
                    return print('exit')
    
            if event.type == KEYDOWN and active == True:
                text = event.unicode


                if event.key == K_BACKSPACE:
    

                    user_text[hit_rect] = user_text[hit_rect][:-1]
                
                else:
                    user_text[hit_rect] += text

        screen.fill((255, 255, 255, 100))
    
        if active:
            color = color_active
        else:
            color = color_passive

        for i in range(len(input_rects)):
            pygame.draw.rect(screen, color, input_rects[i], width=5)
        
        pygame.draw.rect(screen,color, apply_rect, width=5)
        #pygame.draw.line(screen, (255,0,0), (100,0), (100,win_y), width=5)
        size_surface = base_font.render('size', True, BLACK)
        length_surface = base_font.render('length', True, BLACK)
        apply_surface = base_font.render('apply', True, BLACK)
        head_colour_surface = base_font.render('head colour', True, BLACK)
        snake_colour_1_surface = base_font.render('Colour 1', True, BLACK)
        snake_colour_2_surface = base_font.render('Colour 2', True, BLACK)
        #print(user_text[0])


        size_input_surface = base_font.render(user_text[0], True, BLACK)
        length_input_surface = base_font.render(user_text[1], True, BLACK)
        head_colour_input_surface = base_font.render(user_text[2], True,BLACK )
        snake_colour_1_input_surface = base_font.render(user_text[3], True,BLACK )
        snake_colour_2_input_surface = base_font.render(user_text[4], True,BLACK )
    
        screen.blit(size_input_surface, calc_mid_of_rect_for_text(size_input_rect, size_input_surface))
        screen.blit(size_surface, (size_input_rect.x - size_surface.get_width(), size_input_rect.y))

        screen.blit(length_input_surface, calc_mid_of_rect_for_text(length_input_rect, length_input_surface))
        screen.blit(length_surface, (length_input_rect.x - length_surface.get_width(), length_input_rect.y))

        screen.blit(head_colour_input_surface, calc_mid_of_rect_for_text(head_colour_input_rect, head_colour_input_surface))
        screen.blit(head_colour_surface,calc_offset_of_outside_text(head_colour_input_rect,head_colour_surface))

        screen.blit(snake_colour_1_input_surface, calc_mid_of_rect_for_text(snake_colour_1_input_rect, snake_colour_1_input_surface))
        screen.blit(snake_colour_1_surface, calc_offset_of_outside_text(snake_colour_1_input_rect,snake_colour_1_surface))

        screen.blit(snake_colour_2_input_surface, calc_mid_of_rect_for_text(snake_colour_2_input_rect, snake_colour_2_input_surface))
        screen.blit(snake_colour_2_surface, calc_offset_of_outside_text(snake_colour_2_input_rect,snake_colour_2_surface))

        screen.blit(apply_surface,(apply_rect.topleft))


        #input_rect.w = max(100, text_surface.get_width()+10)
        pygame.display.flip()
    
        clock.tick(60)