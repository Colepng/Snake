import pygame
from pygame.rect import *
from pygame.locals import *

rect0 = Rect(50, 60, 200, 80)
rect = rect0.copy()

SIZE = 500, 200
RED = (255, 0, 0)
GRAY = (150, 150, 150)
BLUE = (0,0,255)

screen = pygame.display.set_mode(SIZE)

running = True

dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rect.move_ip(v)

    screen.fill(GRAY)
    pygame.draw.rect(screen, BLUE, rect0, 1)
    pygame.draw.rect(screen, RED, rect, 4)
    pygame.display.flip()

pygame.quit()