import pygame


class ShootPowerBar(object):
    def __init__(self, x, y):
        self.x = x  # X Position
        self.y = y  # Y Position
        self.width = 0  # Width

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, 10))
