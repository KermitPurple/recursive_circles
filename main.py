import pygame
import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = 600,600
screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
            elif event.key == pygame.K_RIGHT:
                print("right")
            elif event.key == pygame.K_UP:
                print("up")
            elif event.key == pygame.K_DOWN:
                print("down")
    screen.fill((0,0,0))
    pygame.display.update()
