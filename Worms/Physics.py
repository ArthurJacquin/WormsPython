import math
import pygame


class Physics:

    @staticmethod
    def CalculateSpeedVector(speed, angle, direction):
        vec = pygame.math.Vector2(math.cos(angle * math.pi / 180) * direction, math.sin(angle * math.pi / 180))
        vec *= speed
        return vec

    # Calculate coordinates of the projectile for the next frame
    @staticmethod
    def CalculateNexPosition(startPos, speed, wind, angle, time):
        forces = pygame.math.Vector2(0, -9.81) + wind
        speedVec = pygame.math.Vector2(math.cos(math.radians(angle)) * speed, math.sin(math.radians(angle)) * speed)

        newX = startPos.x + speedVec.x * time

        newY = startPos.y - ((speedVec.y * time) + (forces.y * 0.5 * time ** 2))

        return pygame.math.Vector2(newX, newY)
