import pygame               #importing everything from pygame that I need
from pygame.rect import *
from pygame.locals import * 

from tkinter import *
from tkinter import messagebox

import random
import pickle

GREEN = 0, 255, 0 #setting the first colout of the snake
LIGHT_GREEN = 0,150,0 #setting the second colout of the snake
BLUE = 0,0,255
WHITE = 255,255,255
clock=pygame.time.Clock()

SIZE = 35
length = 2

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
        #print(unpick.load())
    
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

surface = pygame.display.set_mode((windoes_x, windoes_y))#sets the windoes size
starting_x = calc_in_grid(500,SIZE)
starting_y = calc_in_grid(400,SIZE)

def drawGrid():
    blockSize = 35 #Set the size of the grid block
    for x in range(0, 1000, blockSize):
        for y in range(0, 800, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(surface, WHITE, rect, 1)


class Snake:
    def __init__(self, parent_screen):
        global length
        self.apple_count = 0
        self.parent_screen = parent_screen #A local varibel for the surface
        self.x = [starting_x]*length 
        self.y = [starting_y]*length
        self.head = pygame.Rect(self.x[0], self.y[0], SIZE, SIZE) #A local varibel for the head of the snake
        self.direction = "" #sets starting direction to down
        self.count = 1 # used to switch betwwen colours when drawing the snake
        self.apple = Apple(self.parent_screen)

    def ins_length(self):
        global length
        length += 1
        self.x.append(-1)
        self.y.append(-1)
        self.apple_count += 1

    def draw(self):
        global length
        self.parent_screen.fill((100, 100, 100))
        self.count = 1
        for i in range(length): #A for loop that draws a new segment of the snake
            if self.count == 1:
                pygame.draw.rect(self.parent_screen, BLUE, pygame.Rect(self.x[i], self.y[i], SIZE, SIZE))
                self.count = 2
            elif self.count == 2:
                pygame.draw.rect(self.parent_screen, GREEN, pygame.Rect(self.x[i], self.y[i], SIZE, SIZE))
                self.count = 3
            elif self.count == 3:
                pygame.draw.rect(self.parent_screen, LIGHT_GREEN, pygame.Rect(self.x[i], self.y[i], SIZE, SIZE))
                self.count = 2
        self.apple.apple_draw()
        #drawGrid()
        pygame.display.flip()

    #4 functions that set your direction based on what key you pressed
    def move_left(self):
        if self.direction != "right":
            self.direction = "left"

    def move_right(self):
        if self.direction != "left":
            self.direction = "right"

    def move_up(self):
        if self.direction != "down":
            self.direction = "up"

    def move_down(self):
        if self.direction != "up":
            self.direction = "down"
    #A function that is automaticly moving
    def auto_move(self):
        global length
        for i in range(length-1,0,-1):
            #if self.x[i] == 0
                self.x[i] =  self.x[i - 1]
                #print(self.x[i])
                self.y[i] =  self.y[i - 1]
                #print(self.y[i])

        if self.direction == "left":
            self.x[0] -= SIZE
           #  print(self.x[0])
        if self.direction == "right":
            self.x[0] += SIZE
           # print(self.x[0])
        if self.direction == "up":
            self.y[0] -= SIZE
           # print(self.y[0])
        if self.direction == "down":
            self.y[0] += SIZE
        
        if self.x[0] > windoes_x or self.x[0] < 0 or self.y[0] > windoes_y or self.y[0] < 0:
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

            length = 2
            Tk().wm_withdraw() #to hide the main window
            if self.new_high_score == True:
                yesno_message = f"You eat {self.apple_count} apples, You set a new highscore it is {self.highscore}, Do you want to Play again?"
            else:
                yesno_message = f"You eat {self.apple_count} apples, Your highscore is {self.highscore} Do you want to Play again?"
            if messagebox.askyesno("",yesno_message) == True:
                self.apple_count = 0
                self.parent_screen.fill((100, 100, 100))
                self.count = 1
                for i in range(length):
                    self.x[i] = 0
                    self.y[i] = 0
                    if self.count == 1:
                        pygame.draw.rect(self.parent_screen, BLUE, pygame.Rect(self.x[i], self.y[i], SIZE, SIZE))
                        self.count = 2
                        #print(1)
                    elif self.count == 2:
                        pygame.draw.rect(self.parent_screen, GREEN, pygame.Rect(self.x[i], self.y[i], SIZE, SIZE))
                        self.count = 3
                        #print(2)
                    elif self.count == 3:
                        pygame.draw.rect(self.parent_screen, LIGHT_GREEN, pygame.Rect(self.x[i], self.y[i], SIZE, SIZE))
                        self.count = 2
                        #print(3)                
            else:
                global running
                running = False
                #print("exit")

        self.head = pygame.Rect(self.x[0], self.y[0], SIZE, SIZE)
        #print(self.head.topleft, self.apple.apple_rect.topleft)
        if self.head.topleft == self.apple.apple_rect.topleft:
            self.apple.apple_move()
            self.ins_length()        
        self.draw()


        
class Game: #Crates a class for the actual game
    def __init__(self):
        pygame.init()#starts pygame
        self.snake = Snake(surface)#gives the snake class its function and macking it a local varible, first argument is the surface and the second one is the legnth
        self.snake.draw()
    
    def run(self):# The games loop
        #set_up_highscore()
        global running
        while running:
            for event in pygame.event.get():#gets all events that are happening
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:#if the esc key is press it stop the loop from running
                        running = False
                    if event.key == K_LEFT or event.key == K_a:
                        self.snake.move_left()

                    if event.key == K_RIGHT or event.key == K_d:
                        self.snake.move_right()

                    if event.key == K_UP or event.key == K_w:
                        self.snake.move_up()

                    if event.key == K_DOWN or event.key == K_s:
                        self.snake.move_down()

                if event.type == QUIT:#if the user press the x at the top of the screen it will close the program
                    running = False

            self.snake.auto_move()#calls the auto move function
            clock.tick(8)#sets the in game tick speed





game = Game()#makes the game class a varible 
game.run()#Runs the run fuctions