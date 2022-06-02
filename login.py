import pygame
from pygame.locals import *
from pygame.rect import *

from fun import draw_surfaces,calc_mid_of_rect_for_text
from serve_fun import main


def login(screen):
    username_input = ""
    password_input = ""

    BLACK = (0, 0, 0)

    rect_width = 140

    rect_height  = 32

    user_text = [username_input,password_input]

    username_rect = pygame.Rect(200, 200, rect_width, rect_height)
    passowrd_rect = pygame.Rect(200, 250, rect_width, rect_height)

    input_rects = [username_rect,passowrd_rect]

    login_rect = pygame.Rect(200, 300, rect_width, rect_height)

    back_rect = pygame.Rect(0, 0, rect_width, rect_height)

    pygame.font.init()
    base_font = pygame.font.Font(None,32)

    clock = pygame.time.Clock()

    hit_rect = ""

    while 1:

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:
                print(event.pos)
                for i in range(len(input_rects)):
                    if input_rects[i].collidepoint(event.pos):
                        hit_rect = i
                        break       

                    elif not input_rects[i].collidepoint(event.pos):
                        hit_rect = "outside"




                if login_rect.collidepoint(event.pos):
                    print("login")              
                    if main("login",user_text[0],user_text[1]):
                        print("Login Successful")
                    else:
                        print("Login Failed")

                elif back_rect.collidepoint(event.pos):
                    return

            elif event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN and hit_rect != "outside":
                text = event.unicode

                if event.key == K_BACKSPACE:
                    user_text[hit_rect] = user_text[hit_rect][:-1]

                else:
                    user_text[hit_rect] += text

        screen.fill((255,255,255))

        for i in range(len(input_rects)):
            pygame.draw.rect(screen,(0, 0, 0),input_rects[i],5)
        
        

        username_surface = base_font.render("Username",True,(0, 0, 0))

        password_surface = base_font.render("Password",True,(0, 0, 0))

        login_surface = base_font.render("Login",True,(0, 0, 0))

        back_surface = base_font.render("Back",True,(0, 0, 0))

        username_input_surface = base_font.render(user_text[0], True, BLACK)

        password_input_surface = base_font.render(user_text[1], True, BLACK)    

        draw_surfaces(screen, username_input_surface, username_surface, username_rect)

        draw_surfaces(screen, password_input_surface, password_surface, passowrd_rect)


        screen.blit(login_surface, calc_mid_of_rect_for_text(login_rect, login_surface))
        pygame.draw.rect(screen, BLACK, login_rect, 5)
        pygame.draw.rect(screen, BLACK, back_rect, 5)
        screen.blit(back_surface, calc_mid_of_rect_for_text(back_rect, back_surface))
        
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    login()