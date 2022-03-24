import pygame
from pygame.rect import *
from pygame.locals import * 

GREEN = 0, 255, 0

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.x = 100
        self.y = 100
        self.head = pygame.Rect(self.x, self.y, 50, 50)
        
    def draw(self):
        self.parent_screen.fill((100, 100, 100))
        pygame.draw.rect(self.parent_screen, green, pygame.Rect(self.x, self.y, 50, 50))
        pygame.display.flip()
        
    def move_left(self):
        self.x -= 10
        self.draw()

    def move_right(self):
        self.x += 10
        self.draw()

    def move_up(self):
        self.y -= 10
        self.draw()

    def move_down(self):
        self.y += 10
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

                elif event.type == QUIT:
                    running = False




<<<<<<< HEAD:main.py
if __name__ == '__main__':
    game = Game()
    game.run()
=======
        if rect.bottom > height:
            #print("died")
            speed = [0,0]
            rect = rect_def.copy()
        clock.tick(8)
        screen.fill(bg)
        drawGrid()
        pygame.draw.rect(screen, GREEN, rect)
        pygame.display.flip()
        #print(x,y,speed)
>>>>>>> 8f28a21249f13284ebddc397b0f147f70ba6d2d5:old main.py
