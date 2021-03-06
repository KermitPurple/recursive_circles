import pygame

class RecursiveCircle:

    right = True
    left = False
    up = False
    down = False
    scale = 0.5
    translation_scale = 1

    def __init__(self, screen, size, pos, r, color = 100):
        self.screen = screen
        self.size = size
        self.pos = pos
        self.color = color
        self.r = int(r)

    def draw(self):
        if self.r > 0:
            if self.pos[0] + self.r > 0 and self.pos[0] - self.r < self.size[0] and self.pos[1] + self.r > 0 and self.pos[1] - self.r < self.size[1]:
                pygame.draw.circle(self.screen, self.getcolor(), self.pos, int(self.r), 1)
            if RecursiveCircle.right:
                RecursiveCircle(self.screen, self.size, (self.pos[0] + int(self.r * RecursiveCircle.translation_scale) ,self.pos[1]), self.r * RecursiveCircle.scale, (self.color + 10) % 360).draw()
            if RecursiveCircle.left:
                RecursiveCircle(self.screen, self.size, (self.pos[0] - int(self.r * RecursiveCircle.translation_scale) ,self.pos[1]), self.r * RecursiveCircle.scale, (self.color + 10) % 360).draw()
            if RecursiveCircle.up:
                RecursiveCircle(self.screen, self.size, (self.pos[0], self.pos[1] - int(self.r * RecursiveCircle.translation_scale)), self.r * RecursiveCircle.scale, (self.color + 10) % 360).draw()
            if RecursiveCircle.down:
                RecursiveCircle(self.screen, self.size, (self.pos[0], self.pos[1] + int(self.r * RecursiveCircle.translation_scale)), self.r * RecursiveCircle.scale, (self.color + 10) % 360).draw()

    def getcolor(self):
        color = pygame.Color(255,255,255)
        color.hsva = (self.color, 100, 100)
        return color

    def printcontrols(self):
        print("=" * 75)
        print("<ARROWKEYS> = Toggle directional recursion")
        print("+ = Increase radius of initial triangle")
        print("- = Decrease radius of initial triangle")
        print("< = Decrease radius scale")
        print("> = Incrase radius scale")
        print("k = Decrease translation scale")
        print("l = Increase translation scale")
        print("q = Quit")
        print("=" * 75)
