import pygame               #importing everything from pygame that I need
from pygame.rect import *
from pygame.locals import * 

import sys

from pause_menu import pause_menu
import snake
import fun


clock=pygame.time.Clock()

##Clean up code, make it easier to understand and more readable

running = True

class game: #Crates a class for the actual game     
    
    def run(self, surface, length, size, win_x, win_y, starting_x, starting_y, head_colour, snake_colour_1, snake_colour_2,if_hex, speed):# The games loop
        if False:
            fun.set_up_highscore()

        self.snake = snake.Snake(surface, length, size, win_x, win_y, starting_x, starting_y, head_colour, snake_colour_1, snake_colour_2,if_hex)
        self.snake.draw()

        snake.running = True
        while snake.running:
            for event in pygame.event.get():#gets all events that are happening
 
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:#if the esc key is press it stop the loop from running
                        pause_menu(surface, win_x, win_y, starting_x, starting_y)               

                    #Sets the snake direction to left          
                    if event.key == K_LEFT or event.key == K_a:
                        self.snake.move_left()

                    #Sets the snake direction to right
                    if event.key == K_RIGHT or event.key == K_d:
                        self.snake.move_right()

                    #Sets the snake direction to up
                    if event.key == K_UP or event.key == K_w:
                        self.snake.move_up()

                    #Sets the snake direction to down
                    if event.key == K_DOWN or event.key == K_s:
                        self.snake.move_down()
            

                if event.type == QUIT:#if the user press the x at the top of the screen it will close the program
                    sys.exit()

            if self.snake.auto_move(): #calls the auto move function
                return

            clock.tick(speed)#sets the frame rate

