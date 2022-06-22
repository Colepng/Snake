import pygame
from pygame.locals import *
from pygame.rect import *

from fun import draw_surfaces,calc_mid_of_rect_for_text
from serve_fun import main


def login(screen):
    #Initialize the inputs
    username_input = ""
    password_input = ""

    user_text = [username_input,password_input]#List of all the inputs
    #Initialize the constants
    BLACK = (0, 0, 0)

    RECT_WIDTH = 140

    RECT_HEIGHT  = 32

    BASE_FONT = pygame.font.Font(None,32)

    CLOCK = pygame.time.Clock()

    #Initialize the rectangles
    username_rect = pygame.Rect(200, 200, RECT_WIDTH, RECT_HEIGHT)
    passowrd_rect = pygame.Rect(200, 250, RECT_WIDTH, RECT_HEIGHT)

    input_rects = [username_rect,passowrd_rect]#List of all the inputs rectangles

    login_rect = pygame.Rect(200, 300, RECT_WIDTH, RECT_HEIGHT)

    back_rect = pygame.Rect(0, 0, RECT_WIDTH, RECT_HEIGHT)

    #Initialize variables
    hit_rect = "outside"

    while 1:

        for event in pygame.event.get():#Get what event is happening

            if event.type == MOUSEBUTTONDOWN:#Checks if the event is a mouse click
                print(event.pos)
                for i in range(len(input_rects)):
                    if input_rects[i].collidepoint(event.pos):#Checks to see if the event position is in the input rectangle
                        hit_rect = i
                        break       

                    elif not input_rects[i].collidepoint(event.pos):#IF non of the input rectangles are hit then the user selced no rectang;es
                        hit_rect = "outside"




                if login_rect.collidepoint(event.pos):
                    print("login")              
                    if main("login", user_text[0], user_text[1]):
                        print("Login Successful")
                        return True
                    else:
                        print("Login Failed")

                elif back_rect.collidepoint(event.pos):
                    return

            elif event.type == QUIT:#Checks if the event is a quit event
                pygame.quit()
                exit()


            if event.type == KEYDOWN and hit_rect != "outside":#Checks if the event is a key press and if a input is being edited
                text = event.unicode
                

                if event.key == K_BACKSPACE:
                    user_text[hit_rect] = user_text[hit_rect][:-1]#Removes the last character from the input
                    

                else:
                    user_text[hit_rect] += text

            if event.type == KEYDOWN:#Checks if the event is a key press
                if event.key == K_ESCAPE:
                    return

            

        screen.fill((255,255,255))

        for i in range(len(input_rects)):
            pygame.draw.rect(screen,(0, 0, 0),input_rects[i],5, 5)
        
        

        username_surface = BASE_FONT.render("Username",True,(0, 0, 0))

        password_surface = BASE_FONT.render("Password",True,(0, 0, 0))

        login_surface = BASE_FONT.render("Login",True,(0, 0, 0))

        back_surface = BASE_FONT.render("Back",True,(0, 0, 0))

        username_input_surface = BASE_FONT.render(user_text[0], True, BLACK)

        password_input_surface = BASE_FONT.render(user_text[1], True, BLACK)    

        draw_surfaces(screen, username_input_surface, username_surface, username_rect)

        draw_surfaces(screen, password_input_surface, password_surface, passowrd_rect)


        screen.blit(login_surface, calc_mid_of_rect_for_text(login_rect, login_surface))
        pygame.draw.rect(screen, BLACK, login_rect, 5, 5)
        pygame.draw.rect(screen, BLACK, back_rect, 5, 5)
        screen.blit(back_surface, calc_mid_of_rect_for_text(back_rect, back_surface))
        
        pygame.display.flip()

        CLOCK.tick(60)

if __name__ == "__main__":
    login()