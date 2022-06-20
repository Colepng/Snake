import pygame
from pygame.locals import *
from create_user import create_user
from login import login
from fun import calc_mid_of_rect_for_text, get_highscore, get_logged, get_username
from serve_fun import main
from settings import write_logged
import json

def login_create_account_screen(screen):
    logged = get_logged()

    BLACK = (0, 0, 0)

    rect_width = 140

    rect_height  = 32

    spacing = 20

    create_user_rect = pygame.Rect(screen.get_width()/2 - 140/2, screen.get_height()/2 - 32/2 - 100, rect_width, rect_height,)

    login_rect = pygame.Rect(create_user_rect.left, create_user_rect.bottom + spacing, rect_width, rect_height,)

    back_rect = pygame.Rect(0, 0, rect_width, rect_height)

    load_rect = pygame.Rect(0, 0, rect_width, rect_height)
    load_rect.center = screen.get_rect().center

    save_rect = pygame.Rect(0, 0, rect_width, rect_height)
    save_rect.center = load_rect.centerx, 0
    save_rect.bottom = load_rect.top - spacing

    logout_rect = pygame.Rect(0, 0, rect_width, rect_height)
    logout_rect.center = load_rect.centerx, 0
    logout_rect.top = load_rect.bottom + spacing
    #server rects
    #load_cloud = pygame.Rect()

    pygame.font.init()

    base_font = pygame.font.Font(None, 32)

    while True:
        logged = get_logged()

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:

                if create_user_rect.collidepoint(event.pos) and not logged:
                    print("create user")
                    create_user(screen)
                    
                    

                elif login_rect.collidepoint(event.pos) and not logged:
                    print("login")
                    login(screen)

                elif back_rect.collidepoint(event.pos):
                    return

                elif logout_rect.collidepoint(event.pos) and logged:
                    write_logged(False)

                elif save_rect.collidepoint(event.pos) and logged:
                    print("sync")
                    highscore = get_highscore()
                    print(get_username(), highscore)
                    main("sync", get_username(), highscore = highscore)
                    main("update_settings", get_username(), settings = json.load(open("account_settings.json",)))
                    print("sync done")

                elif load_rect.collidepoint(event.pos) and logged:
                    print("Need to add load")
                    
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return


        screen.fill((255, 255, 255))

        if logged:
            #Draws the rectangles if a user is logged in
            pygame.draw.rect(screen, BLACK, load_rect, 5, 5)
            pygame.draw.rect(screen, BLACK, save_rect, 5, 5)
            pygame.draw.rect(screen, BLACK, logout_rect, 5, 5)
            #Render the text if a user is logged in
            save_surface = base_font.render("Save", True, BLACK)
            load_surface = base_font.render("Load", True, BLACK)
            logout_surface = base_font.render("Logout", True, BLACK)
            #Draws the text if a user is logged in
            screen.blit(logout_surface, calc_mid_of_rect_for_text(logout_rect, logout_surface))
            screen.blit(load_surface, calc_mid_of_rect_for_text(load_rect, load_surface))
            screen.blit(save_surface, calc_mid_of_rect_for_text(save_rect, save_surface))

        else:
            #Draws the rectangles
            pygame.draw.rect(screen, BLACK, create_user_rect, 5, 5)
            pygame.draw.rect(screen, BLACK, login_rect, 5, 5)
            #Renders the text
            login_surface = base_font.render("Login", True, BLACK)
            create_user_surface = base_font.render("Create User", True, BLACK)
            #Draws the text
            screen.blit(create_user_surface, calc_mid_of_rect_for_text(create_user_rect, create_user_surface))
            screen.blit(login_surface, calc_mid_of_rect_for_text(login_rect, login_surface))

        back_surface = base_font.render("Back", True, BLACK)
        screen.blit(back_surface, calc_mid_of_rect_for_text(back_rect, back_surface))
        pygame.draw.rect(screen, BLACK, back_rect, 5, 5)
        
        pygame.display.flip()

        #     pygame.draw.rect(screen, BLACK, sync_rect, 5, 10)
        #     screen.blit(sync_surface, calc_mid_of_rect_for_text(sync_rect, sync_surface))

        # screen.blit(login_surface, calc_mid_of_rect_for_text(login_rect, login_surface))

        # screen.blit(create_user_surface, calc_mid_of_rect_for_text(create_user_rect, create_user_surface))

        # screen.blit(back_surface, calc_mid_of_rect_for_text(back_rect, back_surface))

        
        #pygame.draw.rect(screen, BLACK, create_user_rect, 5)
        #pygame.draw.rect(screen, BLACK, login_rect, 5)
        #pygame.draw.rect(screen, BLACK, back_rect, 5)