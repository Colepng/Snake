import pygame
from pygame.rect import *
from pygame.locals import *
import sys
import apple
from fun import calc_in_grid, drawGrid
import json

import pickle

from tkinter import *
from tkinter import messagebox

GREEN = 0, 255, 0 #setting the first colout of the snake
LIGHT_GREEN = 0,150,0 #setting the second colout of the snake
BLUE = 0,0,255
WHITE = 255,255,255

running = True
class Snake():

    def __init__(self, parent_screen, length, size, win_x, win_y, starting_x, starting_y):
        self.win_x = win_x
        self.win_y = win_y
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.SIZE = size
        self.length = length
        self.apple_count = 0
        self.parent_screen = parent_screen #A local varibel for the surface
        self.x = [self.starting_x]*self.length 
        self.y = [self.starting_y]*self.length
        self.x[0] = self.starting_x
        self.y[0] = self.starting_y
        self.direction = "right"
        for i in range(self.length-1,0,-1):
            self.x[i] =  self.x[0] - self.SIZE*i
            self.y[i] = self.y[0]
        self.head = pygame.Rect(self.x[0], self.y[0], self.SIZE, self.SIZE) #A local varibel for the head of the snakee
        self.apple = apple.Apple(self.parent_screen, self.SIZE, self.win_x, self.win_y)
        self.move = False
    




    def ins_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
        self.apple_count += 1

    def draw(self):
        self.draw_length = self.length -1
        self.parent_screen.fill((100, 100, 100))
        self.count = 1
        for i in range(self.draw_length): #A for loop that draws a new segment of the snake
           # print(self.x[i],self.y[i],i)
            if self.count == 1:
                pygame.draw.rect(self.parent_screen, BLUE, pygame.Rect(self.x[i], self.y[i], self.SIZE, self.SIZE))
                self.count = 2
            elif self.count == 2:
                pygame.draw.rect(self.parent_screen, GREEN, pygame.Rect(self.x[i], self.y[i], self.SIZE, self.SIZE))
                self.count = 3
            elif self.count == 3:
                pygame.draw.rect(self.parent_screen, LIGHT_GREEN, pygame.Rect(self.x[i], self.y[i], self.SIZE, self.SIZE))
                self.count = 2
        self.apple.apple_draw()
        drawGrid(self.parent_screen,WHITE, size=self.SIZE)
        pygame.display.flip()

    #4 functions that set your direction based on what key you pressed
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
    #A function that is automaticly moving
    
    def play_again(self):
        #length = 5
        self.new_high_score = False
        filename = "highscore.pk"
        with open(filename,  "rb") as f:
            unpick = pickle.Unpickler(f)
            old_highscore = unpick.load()
            #print(old_highscore)
            if old_highscore < self.apple_count:
                #print("trues")
                with open(filename,  "wb") as f:
                    pickle.dump(self.apple_count, f)
                    self.new_high_score = True
                    #print("tuerer")
        with open(filename,  "rb") as f:
            unpick = pickle.Unpickler(f)
            self.highscore = unpick.load()

        self.length = 5 + 1
        if self.new_high_score == True:
            yesno_message = f"You eat {self.apple_count} apples, You set a new highscore it is {self.highscore}, Do you want to Play again?"
            #print("you set a new highscore")
        else:
            yesno_message = f"You eat {self.apple_count} apples, Your highscore is {self.highscore} Do you want to Play again?"
            #print("you did not set a new highscore")
        if messagebox.askyesno("",yesno_message) == True:
            self.apple_count = 0
            self.x[0] = self.starting_x
            self.y[0] = self.starting_y
            self.direction = "right"
            for i in range(self.length-1,0,-1):
                self.x[i] =  self.x[0] - self.SIZE*i
                self.y[i] = self.y[0]
            self.apple.apple_move()
            self.draw()   

        else:
            global running
            sys.exit()
            print("exit")


    def auto_move(self):
        for i in range(self.length-1,0,-1):
            #if self.x[i] == 0
                self.x[i] =  self.x[i - 1]
                #print(self.x[i])
                self.y[i] =  self.y[i - 1]
                #print(self.y[i])

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
            
        #print(self.x[0], win_x)
        #print(self.y[0], win_y)
        if self.x[0] > self.win_x - self.SIZE or self.x[0] < 0 or self.y[0] > self.win_y - self.SIZE or self.y[0] < 0:
            self.play_again()
            print('border')

        for i in range(2,self.length):
            if self.head.topleft == (self.x[i], self.y[i]):
                self.play_again()
                print('body')
       
        self.head = pygame.Rect(self.x[0], self.y[0], self.SIZE, self.SIZE)
        #print(self.head.topleft, self.apple.apple_rect.topleft)

        if self.head.topleft == self.apple.apple_rect.topleft:
            self.apple.apple_move()
            for i in range(self.length-1):
                if self.x[i] == self.apple.apple_x and self.y[i] == self.apple.apple_y:
                    self.apple.apple_move()
            self.ins_length()        
        self.draw()
        print(self.starting_x, self.starting_y)