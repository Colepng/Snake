import pygame
import random

SIZE = 35


def calc_in_grid(num_to_round, grid_size):
    return round(num_to_round/grid_size)*grid_size

windoes_x = calc_in_grid(1000, SIZE)
windoes_y = calc_in_grid(800, SIZE)

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.apple_x = calc_in_grid(random.randint(SIZE,windoes_x)-SIZE,SIZE)
        self.apple_y = calc_in_grid(random.randint(SIZE,windoes_y)-SIZE,SIZE)
        self.orgn_size_apple = pygame.image.load("apple.png").convert_alpha()
        self.apple = pygame.transform.scale(self.orgn_size_apple,(SIZE,SIZE))
        self.apple_rect = self.apple.get_rect(x=self.apple_x,y=self.apple_y)
    def apple_draw(self):
        self.parent_screen.blit(self.apple, self.apple_rect)

    def apple_move(self):
        self.apple_x = calc_in_grid(random.randint(SIZE,windoes_x)-SIZE,SIZE)
        self.apple_y = calc_in_grid(random.randint(SIZE,windoes_y)-SIZE,SIZE)
        self.apple_rect = self.apple.get_rect(x=self.apple_x,y=self.apple_y)