import pygame
from pygame.locals import *
from create_user import create_user
from login import login
from fun import calc_mid_of_rect_for_text, get_logged
from settings import write_logged


def login_create_account_screen(screen):

    logged = get_logged()

    BLACK = (0, 0, 0)

    rect_width = 140

    rect_height  = 32

    create_user_rect = pygame.Rect(screen.get_width()/2 - 140/2, screen.get_height()/2 - 32/2 - 100, rect_width, rect_height,)

    login_rect = pygame.Rect(create_user_rect.left, create_user_rect.bottom + 50, rect_width, rect_height,)

    logout_rect = pygame.Rect(login_rect.left, login_rect.bottom + 50, rect_width, rect_height,)

    back_rect = pygame.Rect(0, 0, rect_width, rect_height)

    pygame.font.init()

    base_font = pygame.font.Font(None, 32)

    while True:
        logged = get_logged()

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:

                if create_user_rect.collidepoint(event.pos):
                    print("create user")
                    create_user(screen)
                    

                elif login_rect.collidepoint(event.pos):
                    print("login")
                    login(screen)

                elif back_rect.collidepoint(event.pos):
                    return

                elif logout_rect.collidepoint(event.pos) and logged:
                    write_logged(False)

        login_surface = base_font.render("Login", True, BLACK)
        create_user_surface = base_font.render("Create User", True, BLACK)
        back_surface = base_font.render("Back", True, BLACK)

        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, BLACK, create_user_rect, 5)
        pygame.draw.rect(screen, BLACK, login_rect, 5)
        pygame.draw.rect(screen, BLACK, back_rect, 5)
        if logged:
            pygame.draw.rect(screen, BLACK, logout_rect, 5)

        screen.blit(login_surface, calc_mid_of_rect_for_text(login_rect, login_surface))

        screen.blit(create_user_surface, calc_mid_of_rect_for_text(create_user_rect, create_user_surface))

        screen.blit(back_surface, calc_mid_of_rect_for_text(back_rect, back_surface))

        pygame.display.flip()

