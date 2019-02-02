import math

import pygame
from math import cos, sin
from Worms.Crosshair import *


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x  # Position X
        self.y = y  # Position Y
        self.width = width  # Width in pixel
        self.height = height  # Height in pixel
        self.vel = 2  # Movement speed
        self.isJumping = False  # Is the player jumping ?
        self.jumpCount = 10  # Position during a jump: 10 = start, 0 = middle, -10 = end
        self.jumpHeight = 0.1  # Jump power
        self.left = False  # Is player looking left ?
        self.right = False  # Is player looking right ?
        self.walkCount = 0  # Index of the sprite to display when walking
        self.hasShot = False  # Has player already shoot ?
        self.facing = 1  # 1 if player is looking right, -1 if he is looking left
        self.crosshair = Crosshair(self.x + self.width / 2, self.y + self.height / 2)

        # Player Sprites
        self.walkRight = [pygame.image.load('Images\Rwalk1.png'),
                          pygame.image.load('Images\Rwalk2.png'),
                          pygame.image.load('Images\Rwalk3.png'),
                          pygame.image.load('Images\Rwalk4.png'),
                          pygame.image.load('Images\Rwalk5.png'),
                          pygame.image.load('Images\Rwalk6.png'),
                          pygame.image.load('Images\Rwalk7.png'),
                          pygame.image.load('Images\Rwalk8.png'),
                          pygame.image.load('Images\Rwalk9.png'),
                          pygame.image.load('Images\Rwalk10.png'),
                          pygame.image.load('Images\Rwalk11.png'),
                          pygame.image.load('Images\Rwalk12.png'),
                          pygame.image.load('Images\Rwalk13.png'),
                          pygame.image.load('Images\Rwalk14.png'),
                          pygame.image.load('Images\Rwalk15.png')]
        self.walkLeft = [pygame.image.load('Images\Lwalk1.png'),
                         pygame.image.load('Images\Lwalk2.png'),
                         pygame.image.load('Images\Lwalk3.png'),
                         pygame.image.load('Images\Lwalk4.png'),
                         pygame.image.load('Images\Lwalk5.png'),
                         pygame.image.load('Images\Lwalk6.png'),
                         pygame.image.load('Images\Lwalk7.png'),
                         pygame.image.load('Images\Lwalk8.png'),
                         pygame.image.load('Images\Lwalk9.png'),
                         pygame.image.load('Images\Lwalk10.png'),
                         pygame.image.load('Images\Lwalk11.png'),
                         pygame.image.load('Images\Lwalk12.png'),
                         pygame.image.load('Images\Lwalk13.png'),
                         pygame.image.load('Images\Lwalk14.png'),
                         pygame.image.load('Images\Lwalk15.png')]
        self.char = pygame.image.load('Images\Rwalk1.png')

    def draw(self, win):
        if self.walkCount + 1 >= 45:
            self.walkCount = 0

        # Display sprite
        if self.left:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.char, (self.x, self.y))

    def UpdateCrosshairPosition(self):
        self.crosshair.x = (self.x + self.width / 2) + self.crosshair.distanceToPlayer * math.cos(math.radians(self.crosshair.angle))
        self.crosshair.y = (self.y + self.height / 2) + self.crosshair.distanceToPlayer * -math.sin(math.radians(self.crosshair.angle))
