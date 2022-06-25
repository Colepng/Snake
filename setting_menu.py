import pygame 
from pygame.locals import *
from pygame.rect import *

from fun import calc_mid_of_rect_for_text, list_into_str, draw_surfaces
import json
import settings
import sys
def run(screen):
    clock = pygame.time.Clock()

    logged = json.load(open('logged.json',))
    setting = open('settings.json',) if logged == False else open('account_settings.json',)
    setting_json = json.load(setting)
    # win_x = setting_json['win_x']
    # win_y = setting_json['win_y']
    starting_x = setting_json['starting_x']
    #starting_y = setting_json['starting_y'] - 200
    length = setting_json['length']
    size = setting_json['size']
    speed = setting_json['speed']
    if_hex = setting_json['if_hex']

    #If the user is using rgb for colours display the rgb colours else display the hex colours
    if not if_hex:
        head_colour = list_into_str(setting_json['head_colour_rgb'])
        print(head_colour,"test 1 ")
        snake_colour_1 = list_into_str(setting_json['snake_colour_1_rgb'])
        print(snake_colour_1,'test 2')
        snake_colour_2 = list_into_str(setting_json['snake_colour_2_rgb'])
        print(snake_colour_2,'test 3')
    elif if_hex:
        head_colour = setting_json['head_colour_hex']
        print(head_colour)
        snake_colour_1 = setting_json['snake_colour_1_hex']
        print(snake_colour_1)
        snake_colour_2 = setting_json['snake_colour_2_hex']
        print(snake_colour_2)

    font = pygame.font.Font(None, 32)
    
    #Initialize input texts
    length_input_text = str(length)
    size_input_text = str(size)
    speed_input_text = str(speed)
    head_colour_input_text = head_colour
    snake_colour_1_input_text = snake_colour_1
    snake_colour_2_input_text = snake_colour_2


    #Constent
    RECT_WIDTH = 140
    RECT_HEIGHT = 32
    BLACK = (0, 0, 0)
    SPACING = 20

    #create rects
    center = screen.get_rect().center
    centerx = screen.get_rect().centerx

    #A list of the input texts
    user_text = [size_input_text,length_input_text,head_colour_input_text,snake_colour_1_input_text,snake_colour_2_input_text,speed_input_text]

    #The rectangle in the middle of the screen
    head_colour_input_rect = pygame.Rect(0, 0,RECT_WIDTH, RECT_HEIGHT)
    head_colour_input_rect.center = center

    #The top 3 rectangles 
    if_hex_rect = pygame.Rect(0, 0, RECT_WIDTH*2, RECT_HEIGHT)
    if_hex_rect.centerx = centerx
    if_hex_rect.bottom = head_colour_input_rect.top - SPACING

    size_input_rect = pygame.Rect(0, 0, RECT_WIDTH, RECT_HEIGHT)
    size_input_rect.centerx = centerx
    size_input_rect.bottom = if_hex_rect.top - SPACING

    length_input_rect = pygame.Rect(0, 0, RECT_WIDTH, RECT_HEIGHT)
    length_input_rect.centerx = centerx
    length_input_rect.bottom = size_input_rect.top - SPACING

    #Bottom 3 rectangles
    snake_colour_1_input_rect = pygame.Rect(0, 0, RECT_WIDTH, RECT_HEIGHT)
    snake_colour_1_input_rect.centerx = centerx
    snake_colour_1_input_rect.top = head_colour_input_rect.bottom + SPACING

    snake_colour_2_input_rect = pygame.Rect(starting_x, snake_colour_1_input_rect.bottom + 10, RECT_WIDTH, RECT_HEIGHT)
    snake_colour_2_input_rect.centerx = centerx
    snake_colour_2_input_rect.top = snake_colour_1_input_rect.bottom + SPACING

    speed_input_rect = pygame.Rect(starting_x, snake_colour_2_input_rect.bottom + 10, RECT_WIDTH, RECT_HEIGHT)
    speed_input_rect.centerx = centerx
    speed_input_rect.top = snake_colour_2_input_rect.bottom + SPACING

    #Buttons
    apply_rect = pygame.Rect(0, 700, 140, 32)
    apply_rect.x = centerx + SPACING

    back_rect = pygame.Rect(0, 700, 140, 32)
    back_rect.right = centerx - SPACING
    
    #Text
    input_rects = [size_input_rect, length_input_rect, head_colour_input_rect, snake_colour_1_input_rect, snake_colour_2_input_rect, speed_input_rect]
    colour_state = [False, False, False, False, False, False]#Which box is seleced for colours

    #Colours
    not_selected_colour = (0, 0, 0)
    selected_colour = pygame.Color("#E5446D")

    #stores if a user is editing a input
    active = False

    #Main loop
    while True:

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:
                #Sets all the boxes colours to use the non selected colour
                colour_state = [False, False, False, False, False, False]

                #Checks if any of the rectangles collide with where the mouse was clicked
                for i in input_rects:
                    if i.collidepoint(event.pos):
                        hit_rect = input_rects.index(i)
                        colour_state[hit_rect] = True
                        active = True
                        break

                if not i.collidepoint(event.pos):
                        active = False
                        
            
                if if_hex_rect.collidepoint(event.pos):
                    #swiches the values of if_hex
                    if if_hex: if_hex = False
                    elif not if_hex: if_hex = True

                    #Depending if the user is editing hex colours or rgb colours sets the input to the other colour
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

                #If the user hit the apply rectangle
                elif apply_rect.collidepoint(event.pos):

                    #if the user was editing rgb colours
                    if not if_hex:
                        #Takes the input text and changes it into a list of the rgb values
                        snake_colour_2_input_text = user_text[4].split(',')
                        snake_colour_2_output = [int(x) for x in snake_colour_2_input_text]

                        snake_colour_1_input_text = user_text[3].split(',')
                        snake_colour_1_output = [int(x) for x in snake_colour_1_input_text]

                        head_colour_input_text_list_str = user_text[2].split(',')
                        head_colour_output = [int(x) for x in head_colour_input_text_list_str]

                    elif if_hex == True:
                        #Takes the input text to the colour
                        snake_colour_2_output = user_text[4]        

                        snake_colour_1_output = user_text[3]

                        head_colour_output = user_text[2]

                    if if_hex == True:
                        #Writes the input texts to the settings json
                        settings.write(size=int(user_text[0]), length=int(user_text[1]), speed=int(user_text[5]),
                            head_colour=head_colour_output, snake_colour_1=snake_colour_1_output, snake_colour_2=snake_colour_2_output,
                            head_colour_hex=head_colour_output, snake_colour_1_hex=snake_colour_1_output, snake_colour_2_hex=snake_colour_2_output, if_hex=if_hex
                            )
                    elif if_hex == False:
                        #Writes the input texts to the settings json
                        settings.write(size=int(user_text[0]), length=int(user_text[1]), speed=int(user_text[5]),
                            head_colour=head_colour_output, snake_colour_1=snake_colour_1_output, snake_colour_2=snake_colour_2_output,
                            head_colour_rgb=head_colour_output, snake_colour_1_rgb=snake_colour_1_output, snake_colour_2_rgb=snake_colour_2_output, if_hex=if_hex
                            )
                    return print('exit')
                #If the back button was pressed exit back to the main menu
                elif back_rect.collidepoint(event.pos):
                    return
            #If the event is a keydown event
            if event.type == KEYDOWN and active == True:
                text = event.unicode

                #If the user press backspace delete the last characters
                if event.key == K_BACKSPACE:
                    user_text[hit_rect] = user_text[hit_rect][:-1]

                #else whatever other key was press adds it
                else:
                    user_text[hit_rect] += text
            #If the user press the esc key returns back to the main menu
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

            #If the event is quit exit the program
            elif event.type == QUIT:
                sys.exit()
        #Fills the screen
        screen.fill((255, 255, 255, 100))

        #Draws all the input rectangles
        for i in input_rects:
            pygame.draw.rect(screen, selected_colour if colour_state[input_rects.index(i)] else not_selected_colour, i, width=5, border_radius=5)
        
        #Draws the other rectangles
        pygame.draw.rect(screen, not_selected_colour, apply_rect, width=5, border_radius = 5)
        pygame.draw.rect(screen, not_selected_colour, if_hex_rect, width=5, border_radius = 5)
        pygame.draw.rect(screen, not_selected_colour, back_rect, width=5, border_radius =5)

        #Renders size length and rgb hex text
        size_surface = font.render('size', True, BLACK)
        length_surface = font.render('length', True, BLACK)
        if if_hex == True:
            if_hex_surface = font.render('Change to RGB colours', True, BLACK)
        elif if_hex == False:
            if_hex_surface = font.render('Change to HEX colours', True, BLACK)
        #Renders the colour text
        head_colour_surface = font.render('head colour', True, BLACK)
        snake_colour_1_surface = font.render('Colour 1', True, BLACK)
        snake_colour_2_surface = font.render('Colour 2', True, BLACK)
        #Renders the button text
        speed_surface = font.render('speed', True, BLACK)
        apply_surface = font.render('apply', True, BLACK)
        #Renders all the input text
        size_input_surface = font.render(user_text[0], True, BLACK)
        length_input_surface = font.render(user_text[1], True, BLACK)
        head_colour_input_surface = font.render(user_text[2], True,BLACK )
        snake_colour_1_input_surface = font.render(user_text[3], True,BLACK )
        snake_colour_2_input_surface = font.render(user_text[4], True,BLACK )
        speed_input_surface = font.render(user_text[5], True, BLACK)
        back_surface = font.render('back', True, BLACK)
    
        #Draws the input boxs text and labels
        draw_surfaces(screen, size_input_surface, size_surface, size_input_rect)
        draw_surfaces(screen, length_input_surface, length_surface, length_input_rect)
        draw_surfaces(screen, head_colour_input_surface, head_colour_surface, head_colour_input_rect)
        draw_surfaces(screen, snake_colour_1_input_surface, snake_colour_1_surface, snake_colour_1_input_rect)
        draw_surfaces(screen, snake_colour_2_input_surface, snake_colour_2_surface, snake_colour_2_input_rect)
        draw_surfaces(screen, speed_input_surface, speed_surface, speed_input_rect)

        #Draws the button text
        screen.blit(if_hex_surface, calc_mid_of_rect_for_text(if_hex_rect, if_hex_surface))
        screen.blit(apply_surface, calc_mid_of_rect_for_text(apply_rect, apply_surface))
        screen.blit(back_surface, calc_mid_of_rect_for_text(back_rect, back_surface))

        #Updates the display
        pygame.display.flip()
    
        clock.tick(60)#Caps the frame right