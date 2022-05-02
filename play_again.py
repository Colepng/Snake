import pygame
from pygame.locals import *
import pickle


def play_again(screen, starting_x, starting_y,width,height, apple_count):
    
    WHITE = (255,255,255)

    font = pygame.font.Font(pygame.font.get_default_font(), 36)

    main_rect = pygame.Rect(200,100,width,height)
    main_rect = pygame.Rect(starting_x - width/2, starting_y - height/2, width, height) 

    apple_wrong_size = pygame.image.load("Assests/apple.png").convert_alpha()
    apple = pygame.transform.scale(apple_wrong_size, (50,50))
    apple_rect = apple.get_rect(x=main_rect.left + 100, y=main_rect.top + 50)

    new_high_score = False
    filename = "highscore.pk"
    with open(filename,  "rb") as f:
        unpick = pickle.Unpickler(f)
        old_highscore = unpick.load()

        if old_highscore < apple_count:

            with open(filename,  "wb") as f:
                pickle.dump(apple_count, f)
                new_high_score = True

    with open(filename,  "rb") as f:
        unpick = pickle.Unpickler(f)
        highscore = unpick.load()

    play_again_rect = pygame.Rect(0,0,400 - 5,50)
    play_again_rect = pygame.Rect(main_rect.left,main_rect.bottom + 10, play_again_rect.width, play_again_rect.height)
    play_again_text = font.render('Play again', True,WHITE)

        
    exit_rect = pygame.Rect(0,0,100 - 5,50)
    exit_rect = pygame.Rect(main_rect.right - exit_rect.width, play_again_rect.top,exit_rect.width, exit_rect.height)
    exit_text = font.render("exit", True, WHITE)
    
    
    amount_of_apple = font.render(str(apple_count),True, (0,0,0))
    highscore_text = font.render(f"Your highscore is {highscore}",True,(0,0,0))

    while 1:
        pygame.draw.rect(screen, (0,100,0), main_rect)
        pygame.draw.rect(screen, (0,0,100), play_again_rect)
        screen.blit(play_again_text, ((play_again_rect.width - play_again_text.get_width())/2 + play_again_rect.left, (play_again_rect.height - play_again_text.get_height())/2 + play_again_rect.top))
        pygame.draw.rect(screen, (0,0,100), exit_rect)
        screen.blit(exit_text, ((exit_rect.width - exit_text.get_width())/2 + exit_rect.left, (exit_rect.height - exit_text.get_height())/2 + exit_rect.top))
        screen.blit(apple, apple_rect)
        screen.blit(amount_of_apple, (apple_rect.left - amount_of_apple.get_width() - 10, (apple_rect.height - amount_of_apple.get_height())/2 + apple_rect.y))
        screen.blit(highscore_text, (apple_rect.left - amount_of_apple.get_width() - 10, (apple_rect.height - amount_of_apple.get_height())/2 + apple_rect.y + 100))
        pygame.display.flip()

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            if event.type == MOUSEBUTTONDOWN and play_again_rect.collidepoint(event.pos):
                return True
            
            if event.type == MOUSEBUTTONDOWN and exit_rect.collidepoint(event.pos):
                return False
