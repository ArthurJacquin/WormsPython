import pygame


class Rocket(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 0
        self.color = (255, 0, 0)
        self.facing = 1
        self.vel = 10
        self.mass = 5
        # self.sprite = pygame.image.load('Images\Rocket.jpg')

    def draw(self, window):
        pygame.draw.circle(window, self.color, (round(self.x), round(self.y)), self.radius)

    # Setup the rocket object for a shoot
    def setupForShoot(self, player, facing):
        self.x = round(player.x + player.width // 2)
        self.y = round(player.y + player.height // 2)
        self.radius = 6
        self.facing = facing
