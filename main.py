import pygame               #importing everything from pygame that I need
from pygame.rect import *
from pygame.locals import * 

from tkinter import *
from tkinter import messagebox

import random
import pickle

import apple

import snake
GREEN = 0, 255, 0 #setting the first colout of the snake
LIGHT_GREEN = 0,150,0 #setting the second colout of the snake
BLUE = 0,0,255
WHITE = 255,255,255
clock=pygame.time.Clock()

##fix border wired values

##Clean up code, make it easier to understand and more readable

SIZE = 35
length = 5 + 1

def calc_in_grid(num_to_round, grid_size):
    return round(num_to_round/grid_size)*grid_size

windoes_x = calc_in_grid(1000,SIZE)
windoes_y = calc_in_grid(800,SIZE)
running = True
def set_up_highscore():
    filename = "highscore.pk"
    with open(filename,  "wb") as f:
        highscore = 0
        pickle.dump(highscore, f)
    with open(filename,  "rb") as f:
        unpick = pickle.Unpickler(f)
        print(unpick.load())

surface = pygame.display.set_mode((windoes_x, windoes_y))#sets the windoes size
starting_x = calc_in_grid(windoes_x/2,SIZE)
starting_y = calc_in_grid(windoes_y/2,SIZE)

def drawGrid():
    blockSize = 35 #Set the size of the grid block
    for x in range(0, 1000, blockSize):
        for y in range(0, 800, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(surface, WHITE, rect, 1)



class Game: #Crates a class for the actual game
    def __init__(self):
        pygame.init()#starts pygame
        self.snake = snake.Snake(surface)#gives the snake class its function and macking it a local varible, first argument is the surface and the second one is the legnth
        self.snake.draw()
    
    def run(self):# The games loop
        #set_up_highscore()
        while snake.running:
            for event in pygame.event.get():#gets all events that are happening
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:#if the esc key is press it stop the loop from running
                        snake.running = False
                    if event.key == K_LEFT or event.key == K_a:
                        self.snake.move_left()

                    if event.key == K_RIGHT or event.key == K_d:
                        self.snake.move_right()

                    if event.key == K_UP or event.key == K_w:
                        self.snake.move_up()

                    if event.key == K_DOWN or event.key == K_s:
                        self.snake.move_down()

                if event.type == QUIT:#if the user press the x at the top of the screen it will close the program
                    snake.running = False

            self.snake.auto_move()#calls the auto move function
            clock.tick(8)#sets the in game tick speed

game = Game()#makes the game class a varible 
game.run()#Runs the run fuctions