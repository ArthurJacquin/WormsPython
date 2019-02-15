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
        forces = pygame.math.Vector2(0, -9.81)
        speedVec = pygame.math.Vector2(math.cos(math.radians(angle)) * speed, math.sin(math.radians(angle)) * speed)

        newX = startPos.x + speedVec.x * time

        newY = startPos.y - ((speedVec.y * time) + (forces.y * 0.5 * time ** 2))

        return pygame.math.Vector2(newX, newY)

    @staticmethod
    def GetTrajectory(startpos, speed, sol, wind, angle):
        trajPoints = [(round(startpos.x),round(startpos.y))]
        time = 0

        newPos = Physics.CalculateNexPosition(pygame.math.Vector2(startpos.x,startpos.y), speed, wind, angle, time)

        while not sol[round(newPos[0])][1] <= newPos[1] and 0 < newPos[0] < 840:
            trajPoints.append((round(newPos.x), round(newPos.y)))
            newPos = Physics.CalculateNexPosition(pygame.math.Vector2(startpos.x,startpos.y), speed, wind, angle, time)
            time += 0.05


        return trajPoints


