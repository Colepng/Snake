import pygame 
from pygame.locals import *
from pygame.rect import *

from fun import calc_mid_of_rect_for_text, list_into_str, draw_surfaces

import json

import settings

    #make setting menu to look better

def run():
    clock = pygame.time.Clock()
    logged = json.load(open('logged.json',))
    setting = open('settings.json',) if logged == False else open('account_settings.json',)
    setting_json = json.load(setting)
    win_x = setting_json['win_x']
    win_y = setting_json['win_y']
    starting_x = setting_json['starting_x']
    starting_y = setting_json['starting_y'] - 200
    length = setting_json['length']
    size = setting_json['size']
    speed = setting_json['speed']
    if_hex = setting_json['if_hex']

    if if_hex == False:
        head_colour = list_into_str(setting_json['head_colour_rgb'])
        print(head_colour,"test 1 ")
        snake_colour_1 = list_into_str(setting_json['snake_colour_1_rgb'])
        print(snake_colour_1,'test 2')
        snake_colour_2 = list_into_str(setting_json['snake_colour_2_rgb'])
        print(snake_colour_2,'test 3')
    elif if_hex == True:
        head_colour = setting_json['head_colour_hex']
        print(head_colour)
        snake_colour_1 = setting_json['snake_colour_1_hex']
        print(snake_colour_1)
        snake_colour_2 = setting_json['snake_colour_2_hex']
        print(snake_colour_2)
    
    rect_width = 140
    rect_hight = 32
    BLACK = (0,0,0)


    pygame.font.init()

    screen = pygame.display.set_mode((win_x, win_y))

    base_font = pygame.font.Font(None, 32)
    

    length_input_text = str(length)
    size_input_text = str(size)

    speed_input_text = str(speed)

    head_colour_input_text = head_colour
    snake_colour_1_input_text = snake_colour_1
    snake_colour_2_input_text = snake_colour_2


    user_text = [size_input_text,length_input_text,head_colour_input_text,snake_colour_1_input_text,snake_colour_2_input_text,speed_input_text]

    size_input_rect = pygame.Rect(starting_x, starting_y, rect_width, rect_hight)
    length_input_rect = pygame.Rect(starting_x, size_input_rect.bottom + 10, rect_width, rect_hight)

    if_hex_rect = pygame.Rect(starting_x-rect_width/2, length_input_rect.bottom + 10,rect_width*2,rect_hight)

    head_colour_input_rect = pygame.Rect(starting_x, if_hex_rect.bottom + 10,rect_width, rect_hight)
    snake_colour_1_input_rect = pygame.Rect(starting_x, head_colour_input_rect.bottom + 10, rect_width, rect_hight)
    snake_colour_2_input_rect = pygame.Rect(starting_x, snake_colour_1_input_rect.bottom + 10, rect_width, rect_hight)

    speed_input_rect = pygame.Rect(starting_x, snake_colour_2_input_rect.bottom + 10, rect_width, rect_hight)


    apply_rect = pygame.Rect(500,700,140,32)
    

    input_rects = [size_input_rect,length_input_rect, head_colour_input_rect, snake_colour_1_input_rect, snake_colour_2_input_rect, speed_input_rect]

    color_active = pygame.Color('lightskyblue3')

    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    active = False

    while True:

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:
                for i in input_rects:
                    if i.collidepoint(event.pos):
                        print(i.collidepoint(event.pos))
                        active = True
                        hit_rect = input_rects.index(i)
                        break
                    

                    if not i.collidepoint(event.pos):
                        active = False

                if if_hex_rect.collidepoint(event.pos):

                    if if_hex == True: if_hex = False
                    elif if_hex == False: if_hex = True
                
                    if if_hex == False:
                        user_text[2] = list_into_str(setting_json['head_colour_rgb'])
                        print(user_text[2])
                        user_text[3] = list_into_str(setting_json['snake_colour_1_rgb'])
                        print(user_text[3])
                        user_text[4] = list_into_str(setting_json['snake_colour_2_rgb'])
                        print(user_text[4])
                    elif if_hex == True:
                        user_text[2] = setting_json['head_colour_hex']
                        print(user_text[2])
                        user_text[3] = setting_json['snake_colour_1_hex']
                        print(user_text[3])
                        user_text[4] = setting_json['snake_colour_2_hex']
                        print(user_text[4])


                        

                if apply_rect.collidepoint(event.pos):

                    if if_hex == False:
                        snake_colour_2_input_text = user_text[4].split(',')
                        snake_colour_2_output = [int(x) for x in snake_colour_2_input_text]

                        snake_colour_1_input_text = user_text[3].split(',')
                        snake_colour_1_output = [int(x) for x in snake_colour_1_input_text]

                        head_colour_input_text_list_str = user_text[2].split(',')
                        head_colour_output = [int(x) for x in head_colour_input_text_list_str]
                    elif if_hex == True:
                        snake_colour_2_output = user_text[4]        

                        snake_colour_1_output = user_text[3]

                        head_colour_output = user_text[2]
                    if if_hex == True:
                        settings.write(size=int(user_text[0]), length=int(user_text[1]), speed=int(user_text[5]),
                            head_colour=head_colour_output, snake_colour_1=snake_colour_1_output, snake_colour_2=snake_colour_2_output,
                            head_colour_hex=head_colour_output, snake_colour_1_hex=snake_colour_1_output, snake_colour_2_hex=snake_colour_2_output, if_hex=if_hex
                            )
                    elif if_hex == False:
                        settings.write(size=int(user_text[0]), length=int(user_text[1]), speed=int(user_text[5]),
                            head_colour=head_colour_output, snake_colour_1=snake_colour_1_output, snake_colour_2=snake_colour_2_output,
                            head_colour_rgb=head_colour_output, snake_colour_1_rgb=snake_colour_1_output, snake_colour_2_rgb=snake_colour_2_output, if_hex=if_hex
                            )
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
        pygame.draw.rect(screen,color, if_hex_rect, width=5)
        #pygame.draw.line(screen, (255,0,0), (100,0), (100,win_y), width=5)
        size_surface = base_font.render('size', True, BLACK)
        length_surface = base_font.render('length', True, BLACK)
        if if_hex == True:
            if_hex_surface = base_font.render('Change to RGB colours', True, BLACK)
        elif if_hex == False:
            if_hex_surface = base_font.render('Change to HEX colours', True, BLACK)
        head_colour_surface = base_font.render('head colour', True, BLACK)
        snake_colour_1_surface = base_font.render('Colour 1', True, BLACK)
        snake_colour_2_surface = base_font.render('Colour 2', True, BLACK)

        speed_surface = base_font.render('speed', True, BLACK)

        apply_surface = base_font.render('apply', True, BLACK)
        #print(user_text[0])


        size_input_surface = base_font.render(user_text[0], True, BLACK)
        length_input_surface = base_font.render(user_text[1], True, BLACK)
        head_colour_input_surface = base_font.render(user_text[2], True,BLACK )
        snake_colour_1_input_surface = base_font.render(user_text[3], True,BLACK )
        snake_colour_2_input_surface = base_font.render(user_text[4], True,BLACK )
        speed_input_surface = base_font.render(user_text[5], True, BLACK)
    

        draw_surfaces(screen, size_input_surface, size_surface, size_input_rect)

        draw_surfaces(screen, length_input_surface, length_surface, length_input_rect)

        draw_surfaces(screen, head_colour_input_surface, head_colour_surface, head_colour_input_rect)

        draw_surfaces(screen, snake_colour_1_input_surface, snake_colour_1_surface, snake_colour_1_input_rect)

        draw_surfaces(screen, snake_colour_2_input_surface, snake_colour_2_surface, snake_colour_2_input_rect)

        draw_surfaces(screen, speed_input_surface, speed_surface, speed_input_rect)

        screen.blit(if_hex_surface, calc_mid_of_rect_for_text(if_hex_rect, if_hex_surface))

        screen.blit(apply_surface, (apply_rect.topleft))


        #input_rect.w = max(100, text_surface.get_width()+10)
        pygame.display.flip()
    
        clock.tick(60)
# run()