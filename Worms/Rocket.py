import pygame
from Worms.Vector2 import Vector2

class Rocket(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 5

    def draw(self, window):
        pygame.draw.circle(window, self.color, (round(self.x), round(self.y)), self.radius)
