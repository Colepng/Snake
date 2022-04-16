import pygame               #importing everything from pygame that I need
from pygame.rect import *
from pygame.locals import * 
import random
GREEN = 0, 255, 0 #setting the first colout of the snake
LIGHT_GREEN = 0,150,0 #setting the second colout of the snake
clock=pygame.time.Clock()

SIZE = 35
length = 3

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.apple_x = round(random.randint(0,1000)/35)*35
        self.apple_y = round(random.randint(0,800)/35)*35
        self.apple =  pygame.image.load("apple.png").convert_alpha()

    def apple_draw(self):
        self.parent_screen.blit(self.apple, (self.apple_x,self.apple_y))
class Snake:
    def __init__(self, parent_screen, length):
        self.length = length #A local varibel for the length of the snake
        self.parent_screen = parent_screen #A local varibel for the surface
        self.x = [SIZE]*length 
        self.y = [SIZE]*length
        self.rect = pygame.Rect(SIZE, SIZE, 50, 50) #A local varibel for the head of the snake
        self.parent_screen.fill((100, 100, 100))#fills the screen with green so the snake old postion gets drawened over
        pygame.draw.rect(self.parent_screen, GREEN, pygame.Rect(SIZE, SIZE, 50, 50)) #Draws the first instence of the snake
        pygame.display.flip()   #Updates the user screen
        self.direction = "down" #sets starting direction to down
        self.move_size = 20 #sets how much you move by
        self.count = 1 # used to switch betwwen colours when drawing the snake
        self.apple = Apple(self.parent_screen)
        
    def draw(self):
        self.parent_screen.fill((100, 100, 100))
        for i in range(self.length): #A for loop that draws a new segment of the snake
            if self.count == 1:
                pygame.draw.rect(self.parent_screen, GREEN, pygame.Rect(self.x[i], self.y[i], SIZE, SIZE))
                self.count = 2
            elif self.count == 2:
                pygame.draw.rect(self.parent_screen, LIGHT_GREEN, pygame.Rect(self.x[i], self.y[i], SIZE, SIZE))
                self.count = 1
        self.apple.apple_draw()
        pygame.display.flip()
    #4 functions that set your direction based on what key you pressed
    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"
    #A function that is automaticly moving
    def auto_move(self):

        for i in range(self.length-1,0,-1):
            self.x[i] =  self.x[i - 1]
            print(self.x[i])
            self.y[i] =  self.y[i - 1]
            print(self.y[i])

        if self.direction == "left":
            self.x[0] -= SIZE + 5
           #  print(self.x[0])
        if self.direction == "right":
            self.x[0] += SIZE + 5
           # print(self.x[0])
        if self.direction == "up":
            self.y[0] -= SIZE + 5
           # print(self.y[0])
        if self.direction == "down":
            self.y[0] += SIZE + 5
           # print(self.y[0])
        self.apple_x_pos = SIZE + self.apple.apple_x
        self.apple_x_neg = SIZE - self.apple.apple_x
        self.apple_y_pos = SIZE + self.apple.apple_y
        self.apple_y_neg = SIZE - self.apple.apple_y
        if self.x[0] <  self.apple_x_pos and self.x[0] > self.apple_x_neg and self.y[0] <  self.apple_y_pos and self.y[0] > self.apple_y_neg:
            self.apple.apple_x = round(random.randint(0,1000)/35)*35
            self.apple.apple_y = round(random.randint(0,1000)/35)*35
            #self.length += 1
        self.draw()

class Game: #Crates a class for the actual game
    def __init__(self):
        pygame.init()#starts pygame
        self.surface = pygame.display.set_mode((1000, 800))#sets the windoes size
        self.snake = Snake(self.surface,2)#gives the snake class its function and macking it a local varible, first argument is the surface and the second one is the legnth
        self.snake.draw()
    
    def run(self):# The games loop
        running = True

        while running:
            for event in pygame.event.get():#gets all events that are happening
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:#if the esc key is press it stop the loop from running
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                if event.type == QUIT:#if the user press the x at the top of the screen it will close the program
                    running = False

            self.snake.auto_move()#calls the auto move function
            clock.tick(8)#sets the in game tick speed
            


game = Game()#makes the game class a varible 
game.run()#Runs the run fuctions