import math
import pygame
from sympy import pi, sin

class Physics:

    @staticmethod
    def CalculateSpeedVector(speed, angle, direction):
        vec = pygame.math.Vector2(math.cos(angle * pi / 180) * direction, math.sin(angle * pi /180))
        vec *= speed
        return vec

    @staticmethod
    def CalculateNexPosition(startPos, speed, wind):
        forces = pygame.math.Vector2(0, -9.81) + wind
        x = startPos.x + speed.x
        y = -(-0.5 * (forces.y) ** 2 + (startPos * speed)) + startPos.y
        newPos = pygame.math.Vector2(x, y)
        return newPos
