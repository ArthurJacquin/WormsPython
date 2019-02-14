import math
import pygame
from Worms.Collision import *


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
'''
    @staticmethod
    def GetTrajectory(self, object, sol, startPos, speed, wind, angle):
        position = startPos
        trajPoints = list()
        time = 0
        while(not GroundCollision(object, sol)):
            trajPoints.append(CalculateNextPosition(startPos, speed, wind, angle, time))
            time += 0.05


        return trajPoints
'''

