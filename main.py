import pygame
import os
from RecursiveCircle import RecursiveCircle
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = 650,650
screen = pygame.display.set_mode(size)
circle = RecursiveCircle(screen, size,(int(size[0]/2),int(size[1]/2)), 160)
circle.printcontrols()
running = True
pygame.key.set_repeat(60)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                RecursiveCircle.left = not RecursiveCircle.left
            elif event.key == pygame.K_RIGHT:
                RecursiveCircle.right = not RecursiveCircle.right
            elif event.key == pygame.K_UP:
                RecursiveCircle.up = not RecursiveCircle.up
            elif event.key == pygame.K_DOWN:
                RecursiveCircle.down = not RecursiveCircle.down
            elif event.unicode == 'q':
                running = False
            elif event.unicode == '=':
                circle.r = 160
            elif event.unicode == '+':
                    circle.r += 5
            elif event.unicode == '-':
                if circle.r > 5:
                    circle.r -= 5
    screen.fill((0,0,0))
    circle.draw()
    pygame.display.update()
