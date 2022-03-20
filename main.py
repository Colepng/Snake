import sys
import pygame
from pygame.rect import *
from pygame.locals import *
pygame.init()

clock=pygame.time.Clock()

SIZE = width, height = 800, 800
red = (255,0,0)
blue = (0, 0, 255)
bg = 0,0,0
screen = pygame.display.set_mode(SIZE)

x = 350
y = 350

rect_def = pygame.Rect(x, y, 50, 50)
rect = rect_def.copy()
speed = [0, 0]

dir = { K_w: (0, -5), K_s: (0, 5), K_d: (5, 0), K_a: (-5,0)}

pygame.draw.rect(screen, red, rect)
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
    
        if event.type == KEYDOWN:
            speed = dir[event.key]
            
    rect.move_ip(speed)

    if rect.left < 0:
            print("died")
            speed = [0,0]
            rect = rect_def.copy()

    if rect.right > width:
            print("died")
            speed = [0,0]
            rect = rect_def.copy()

    if rect.top < 0:
            print("died")
            speed = [0,0]
            rect = rect_def.copy()

    if rect.bottom > height:
            print("died")
            speed = [0,0]
            rect = rect_def.copy()
    clock.tick(60)
    screen.fill(bg)
    pygame.draw.rect(screen, blue, rect)
    pygame.display.flip()