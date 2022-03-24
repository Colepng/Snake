import sys
import pygame
from pygame.rect import *
from pygame.locals import *
pygame.init()

clock=pygame.time.Clock()

grid_size = 35

SIZE = width, height = 800, 800
GREEN = (0,100,0)
WHITE = (255,255,255)
bg = 0,0,0
screen = pygame.display.set_mode(SIZE)

x = 400
y = 400

loop = 0
rect_def = pygame.Rect(350, 350, grid_size, grid_size)
rect = rect_def.copy()
speed = [0, 0]

dir = { K_w: (0, -grid_size), K_s: (0, grid_size), K_d: (grid_size, 0), K_a: (-grid_size,0)}

pygame.draw.rect(screen, GREEN, rect)
pygame.display.flip()


def drawGrid():
    blockSize = grid_size #Set the size of the grid block
    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)


while 1:
        drawGrid()
        for event in pygame.event.get():
                if event.type == QUIT: sys.exit()

                if event.type == KEYDOWN:
                    speed = dir[event.key]
    
        rect.move_ip(speed)
        if rect.left < 0:
            #print("died")
            speed = [0,0]
            rect = rect_def.copy()

        if rect.right > width:
            #print("died")
            speed = [0,0]
            rect = rect_def.copy()

        if rect.top < 0:
            #print("died")
            speed = [0,0]
            rect = rect_def.copy()

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
