import pygame
import random
import json

def calc_in_grid(num_to_round, grid_size):
    return round(num_to_round/grid_size)*grid_size

setting = open('settings.json',)
setting_json = json.load(setting)
win_x = setting_json['win_x']
win_y = setting_json['win_y']
SIZE = setting_json['size']


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.apple_x = calc_in_grid(random.randint(SIZE,win_x)-SIZE,SIZE)
        self.apple_y = calc_in_grid(random.randint(SIZE,win_y)-SIZE,SIZE)
        self.orgn_size_apple = pygame.image.load("apple.png").convert_alpha()
        self.apple = pygame.transform.scale(self.orgn_size_apple,(SIZE,SIZE))
        self.apple_rect = self.apple.get_rect(x=self.apple_x,y=self.apple_y)
    def apple_draw(self):
        self.parent_screen.blit(self.apple, self.apple_rect)

    def apple_move(self):
        self.apple_x = calc_in_grid(random.randint(SIZE,win_x)-SIZE,SIZE)
        self.apple_y = calc_in_grid(random.randint(SIZE,win_y)-SIZE,SIZE)
        self.apple_rect = self.apple.get_rect(x=self.apple_x,y=self.apple_y)