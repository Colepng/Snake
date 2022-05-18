import pygame
from pygame.rect import *
from pygame.locals import *
import sys
import apple as apple
from fun import calc_in_grid, drawGrid
from play_again import play_again
import json

import pickle

from tkinter import *
from tkinter import messagebox

WHITE = 255, 255, 255

running = True


class Snake():

    def __init__(self, parent_screen, length, size, win_x, win_y, starting_x, starting_y, head_colour, snake_colour_1, snake_colour_2, if_hex):
        if if_hex == True:
            self.head_colour = pygame.Color(head_colour)
            self.snake_colour_1 = pygame.Color(snake_colour_1)
            self.snake_colour_2 = pygame.Color(snake_colour_2)
        elif if_hex == False:
            self.head_colour = head_colour
            self.snake_colour_1 = snake_colour_1
            self.snake_colour_2 = snake_colour_2
        self.win_x = win_x
        self.win_y = win_y
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.staring_length = length
        self.SIZE = size
        self.length = length
        self.apple_count = 0
        self.parent_screen = parent_screen  # A local varibel for the surface
        self.x = [self.starting_x]*self.length
        self.y = [self.starting_y]*self.length
        self.x[0] = self.starting_x
        self.y[0] = self.starting_y
        self.direction = 'right'
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[0] - self.SIZE*i
            self.y[i] = self.y[0]
        # A local varibel for the head of the snakee
        self.head = pygame.Rect(self.x[0], self.y[0], self.SIZE, self.SIZE)
        self.apple = apple.Apple(self.parent_screen, self.SIZE, self.win_x, self.win_y)
        self.move = False

    def ins_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
        self.apple_count += 1

    def draw(self):
        self.draw_length = self.length - 1
        self.parent_screen.fill((100, 100, 100))
        self.count = 1
        for i in range(self.draw_length):  # A for loop that draws a new segment of the snake
           # print(self.x[i],self.y[i],i)
            if self.count == 1:
                pygame.draw.rect(self.parent_screen, self.head_colour, pygame.Rect(
                    self.x[i], self.y[i], self.SIZE, self.SIZE))
                self.count = 2
            elif self.count == 2:
                pygame.draw.rect(self.parent_screen, self.snake_colour_1, pygame.Rect(
                    self.x[i], self.y[i], self.SIZE, self.SIZE))
                self.count = 3
            elif self.count == 3:
                pygame.draw.rect(self.parent_screen, self.snake_colour_2, pygame.Rect(
                    self.x[i], self.y[i], self.SIZE, self.SIZE))
                self.count = 2
        self.apple.apple_draw()
        #drawGrid(self.parent_screen,WHITE, size=self.SIZE)
        pygame.display.flip()

    # 4 functions that set your direction based on what key you pressed
    def move_left(self):
        if self.direction != "right" and self.move == True:
            self.direction = "left"
            self.move = False

    def move_right(self):
        if self.direction != "left" and self.move == True:
            self.direction = "right"
            self.move = False

    def move_up(self):
        if self.direction != "down" and self.move == True:
            self.direction = "up"
            self.move = False

    def move_down(self):
        if self.direction != "up" and self.move == True:
            self.direction = "down"
            self.move = False

    def reset(self):
        self.length = self.staring_length
        self.apple_count = 0
        self.x[0] = self.starting_x
        self.y[0] = self.starting_y
        self.direction = "right"
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[0] - self.SIZE*i
            self.y[i] = self.y[0]
        self.apple.apple_move()
        self.draw()

    def auto_move(self):
        for i in range(self.length-1, 0, -1):
            # if self.x[i] == 0
            self.x[i] = self.x[i - 1]
            # print(self.x[i])
            self.y[i] = self.y[i - 1]
            # print(self.y[i])

        if self.direction == "left":
            self.x[0] -= self.SIZE
            self.move = True
           #  print(self.x[0])
        if self.direction == "right":
            self.x[0] += self.SIZE
            self.move = True
           # print(self.x[0])
        if self.direction == "up":
            self.y[0] -= self.SIZE
            self.move = True
           # print(self.y[0])
        if self.direction == "down":
            self.y[0] += self.SIZE
            self.move = True

        if self.x[0] > self.win_x - self.SIZE or self.x[0] < 0 or self.y[0] > self.win_y - self.SIZE or self.y[0] < 0:
            if play_again(self.parent_screen, self.starting_x, self.starting_y, 500, 400, self.apple_count) == True:
                self.reset()
            else:
                sys.exit()
            print('border')

        for i in range(2, self.length):
            if self.head.topleft == (self.x[i], self.y[i]):
                if play_again(self.parent_screen, self.starting_x, self.starting_y, 500, 400, self.apple_count) == True:
                    self.reset()
                else:
                    sys.exit()
                print('body')

        self.head = pygame.Rect(self.x[0], self.y[0], self.SIZE, self.SIZE)

        if self.head.topleft == self.apple.apple_rect.topleft:
            self.apple.apple_move()
            for i in range(self.length-1):
                if self.x[i] == self.apple.apple_x and self.y[i] == self.apple.apple_y:
                    self.apple.apple_move()
            self.ins_length()
        self.draw()
