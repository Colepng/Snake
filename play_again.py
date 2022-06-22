import pygame
from pygame.locals import *
import pickle
import json

from fun import calc_mid_of_rect_for_text, calc_offset_of_outside_text
import snake


def play_again(screen, starting_x, starting_y,width,height, apple_count):
    
    logged = json.load(open('logged.json',))
    
    WHITE = (255,255,255)

    font = pygame.font.Font(pygame.font.get_default_font(), 36)

    main_rect = pygame.Rect(200,100,width,height)
    main_rect.center = screen.get_rect().center

    apple_wrong_size = pygame.image.load("Assests/apple.png").convert_alpha()
    apple = pygame.transform.scale(apple_wrong_size, (50,50))
    apple_rect = apple.get_rect(x=main_rect.left + 100, y=main_rect.top + 50)

    new_high_score = False
    filename = "highscore.pk" if not logged else "highscore_account.pk"
    print(logged)
    print(filename)
    with open(filename,  "rb") as f:
        unpick = pickle.Unpickler(f)
        old_highscore = unpick.load()
        print(old_highscore)

        if old_highscore < apple_count:

            with open(filename,  "wb") as f:
                pickle.dump(apple_count, f)
                new_high_score = True

    with open(filename,  "rb") as f:
        unpick = pickle.Unpickler(f)
        highscore = unpick.load()
        print(highscore)

    #play again rect and text
    play_again_rect = pygame.Rect(0, 0, 400 - 5, 50)
    play_again_rect = pygame.Rect(main_rect.left,main_rect.bottom + 10, play_again_rect.width, play_again_rect.height)
    play_again_text = font.render('Play again', True,WHITE)

    #exit rect and text
    exit_rect = pygame.Rect(0, 0, 100 - 5, 50)
    exit_rect = pygame.Rect(main_rect.right - exit_rect.width, play_again_rect.top,exit_rect.width, exit_rect.height)
    exit_text = font.render("Exit", True, WHITE)
    
    #Main menu rect and text
    main_menu_rect = pygame.Rect(0, 0, 500, 50)
    main_menu_rect.centerx = screen.get_rect().centerx
    main_menu_rect.top = play_again_rect.bottom + 20
    main_menu_text = font.render("Main Menu", True, WHITE)
    
    amount_of_apple = font.render(str(apple_count),True, (0, 0, 0))
    highscore_text = font.render(f"Your highscore is {highscore}",True,(0, 0, 0))

    while 1:
        pygame.draw.rect(screen, (0, 100, 0), main_rect)
        pygame.draw.rect(screen, (0, 0, 100), play_again_rect)
        #screen.blit(play_again_text, ((play_again_rect.width - play_again_text.get_width())/2 + play_again_rect.left, (play_again_rect.height - play_again_text.get_height())/2 + play_again_rect.top))
        screen.blit(play_again_text, calc_mid_of_rect_for_text(play_again_rect, play_again_text))


        pygame.draw.rect(screen, (0, 0, 100), exit_rect)
        #screen.blit(exit_text, ((exit_rect.width - exit_text.get_width())/2 + exit_rect.left, (exit_rect.height - exit_text.get_height())/2 + exit_rect.top))
        screen.blit(exit_text, calc_mid_of_rect_for_text(exit_rect, exit_text))

        #Main menu drawing
        pygame.draw.rect(screen, (0, 0, 100), main_menu_rect)
        screen.blit(main_menu_text, calc_mid_of_rect_for_text(main_menu_rect, main_menu_text))


        screen.blit(apple, apple_rect)
        screen.blit(amount_of_apple, (apple_rect.left - amount_of_apple.get_width() - 10, (apple_rect.height - amount_of_apple.get_height())/2 + apple_rect.y))
        #screen.blit(amount_of_apple, calc_offset_of_outside_text(apple_rect, amount_of_apple))
        screen.blit(highscore_text, (apple_rect.left - amount_of_apple.get_width() - 10, (apple_rect.height - amount_of_apple.get_height())/2 + apple_rect.y + 100))
        pygame.display.flip()

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            if event.type == MOUSEBUTTONDOWN and play_again_rect.collidepoint(event.pos):
                return True
            
            elif event.type == MOUSEBUTTONDOWN and exit_rect.collidepoint(event.pos):
                return False

            elif event.type == MOUSEBUTTONDOWN and main_menu_rect.collidepoint(event.pos):
                print("test")
                snake.running = False
                return "Main Menu"
