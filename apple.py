import pygame
import random
import json

from fun import calc_in_grid

class Apple:
    def __init__(self, parent_screen, SIZE, win_x, win_y):
        self.SIZE = SIZE
        self.win_x = win_x
        self.win_y = win_y
        self.parent_screen = parent_screen
        self.apple_x = calc_in_grid(random.randint(self.SIZE,self.win_x)-self.SIZE,self.SIZE)
        self.apple_y = calc_in_grid(random.randint(self.SIZE,self.win_y)-self.SIZE,self.SIZE)
        self.orgn_size_apple = pygame.image.load("Assests/apple.png").convert_alpha()
        self.apple = pygame.transform.scale(self.orgn_size_apple,(self.SIZE,self.SIZE))
        self.apple_rect = self.apple.get_rect(x=self.apple_x,y=self.apple_y)
        #print(f"apple size{self.SIZE}")
    def apple_draw(self):
        self.parent_screen.blit(self.apple, self.apple_rect)

    def apple_move(self):
        self.apple_x = calc_in_grid(random.randint(self.SIZE,self.win_x)-self.SIZE,self.SIZE)
        self.apple_y = calc_in_grid(random.randint(self.SIZE,self.win_y)-self.SIZE,self.SIZE)
        self.apple_rect = self.apple.get_rect(x=self.apple_x,y=self.apple_y)