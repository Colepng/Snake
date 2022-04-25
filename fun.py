import pickle
import pygame
import json

setting = open('settings.json',)
setting_json = json.load(setting)
size = setting_json['size']
setting.close()

def calc_in_grid(num_to_round, grid_size):
    return round(num_to_round/grid_size)*grid_size

def set_up_highscore():
    filename = "highscore.pk"
    with open(filename,  "wb") as f:
        highscore = 0
        pickle.dump(highscore, f)
    with open(filename,  "rb") as f:
        unpick = pickle.Unpickler(f)
        print(unpick.load())

def drawGrid(surface,colour):
    blockSize = size#Set the size of the grid block
    for x in range(0, 1000, blockSize):
        for y in range(0, 800, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(surface, colour, rect, 1)