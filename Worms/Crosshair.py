import pygame


class Crosshair(object):
    def __init__(self, rotationCenterX, rotationCenterY):
        self.rotationCenterX = rotationCenterX  # Center of the player X
        self.rotationCenterY = rotationCenterY  # Center of the player Y
        self.distanceToPlayer = 50  # Radius of the circle between the player and the crosshair
        self.x = self.rotationCenterX + self.distanceToPlayer  # position X of the crosshair
        self.y = self.rotationCenterY  # position Y of the crosshair
        self.radius = 7  # Radius of the crosshair
        self.angle = 0  # angle between horizontal axis and the crosshair

    def draw(self, win):
        pygame.draw.circle(win, (255, 0, 0), (round(self.x), round(self.y)), self.radius)

    def move(self, direction):
        self.angle += 1.5 * direction
