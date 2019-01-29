import pygame

class Rocket(object):
    def __init__(self, x, y, radius, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (255, 0, 0)
        self.facing = facing
        self.vel = 5

    def draw(self, window):
        pygame.draw.circle(window, self.color, (round(self.x), round(self.y)), self.radius)
