import pygame
from pygame.rect import *
from pygame.locals import * 

GREEN = 0, 255, 0
clock=pygame.time.Clock()

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.speed = [0, 0]
        self.x = 100
        self.y = 100
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.parent_screen.fill((100, 100, 100))
        pygame.draw.rect(self.parent_screen, GREEN, pygame.Rect(self.x, self.y, 50, 50))
        pygame.display.flip()
        self.direction = "down"
        
    def draw(self):
        self.parent_screen.fill((100, 100, 100))

        pygame.draw.rect(self.parent_screen, GREEN, pygame.Rect(self.x, self.y, 50, 50))
        pygame.display.flip()

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def auto_move(self):
        if self.direction == "left":
            self.x -= 7

        if self.direction == "right":
            self.x += 7

        if self.direction == "up":
            self.y -= 7

        if self.direction == "down":
            self.y += 7
        print("test")
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.snake = Snake(self.surface)
        self.snake.draw()
    
    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                if event.type == QUIT:
                    running = False

            self.snake.auto_move()
            clock.tick(40)
            


game = Game()
game.run()