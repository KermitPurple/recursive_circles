import pygame

class RecursiveCircle:

    right = True
    left = False
    up = False
    down = False

    def __init__(self, screen, size, pos, r):
        self.screen = screen
        self.size = size
        self.pos = pos
        self.r = int(r)

    def draw(self):
        if self.r > 0:
            pygame.draw.circle(self.screen, (255,255,255) ,self.pos, int(self.r), 1)
            if RecursiveCircle.right:
                RecursiveCircle(self.screen, self.size, (self.pos[0] + self.r ,self.pos[1]), self.r/2).draw()
            if RecursiveCircle.left:
                RecursiveCircle(self.screen, self.size, (self.pos[0] - self.r ,self.pos[1]), self.r/2).draw()
            if RecursiveCircle.up:
                RecursiveCircle(self.screen, self.size, (self.pos[0], self.pos[1] - self.r), self.r/2).draw()
            if RecursiveCircle.down:
                RecursiveCircle(self.screen, self.size, (self.pos[0], self.pos[1] + self.r), self.r/2).draw()
