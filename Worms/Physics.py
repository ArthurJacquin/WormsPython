import math
import pygame


class Physics:

    @staticmethod
    def CalculateSpeedVector(speed, angle):
        vec = pygame.math.Vector2(math.cos(math.radians(angle)), math.sin(math.radians(angle)))
        vec *= speed
        return vec

    # Calculate coordinates of the projectile for the next frame
    @staticmethod
    def CalculateNexPosition(startPos, speed, angle, time):
        gravity = pygame.math.Vector2(0, -9.81)
        speedVec = pygame.math.Vector2(math.cos(math.radians(angle)) * speed, math.sin(math.radians(angle)) * speed)

        newX = startPos.x + speedVec.x * time

        newY = startPos.y - ((speedVec.y * time) + (gravity.y * 0.5 * time ** 2))

        return pygame.math.Vector2(newX, newY)

    # Calculate coordinates of the projectile affected by wind for the next frame
    @staticmethod
    def CalculateNextPositionWithWind(startpos, speed, angle, wind, time, mass):
        gravity = pygame.math.Vector2(0, -9.81)

        VZero = pygame.math.Vector2(math.cos(math.radians(angle)) * speed, -math.sin(math.radians(angle)) * speed)

        newX = 0.5 * 1/mass * wind.x * time ** 2 + VZero.x * time + startpos.x
        newY = startpos.y + (0.5 * (-gravity.y + 1/mass * wind.y) * time ** 2 + VZero.y * time)

        return pygame.math.Vector2(newX, newY)

    @staticmethod
    def GetTrajectory(startpos, speed, sol, angle, wind = pygame.math.Vector2(0, 0), useWind = False, mass = 1):
        trajPoints = [(round(startpos.x), round(startpos.y))]

        time = 0

        if useWind:
            newPos = Physics.CalculateNextPositionWithWind(pygame.math.Vector2(startpos.x, startpos.y), speed, angle, wind, time, mass)
        else:
            newPos = Physics.CalculateNexPosition(pygame.math.Vector2(startpos.x,startpos.y), speed, angle, time)

        while not sol[round(newPos[0])][1] <= newPos[1] and 0 < newPos[0] < 840:
            trajPoints.append((round(newPos.x), round(newPos.y)))

            if useWind:
                newPos = Physics.CalculateNextPositionWithWind(pygame.math.Vector2(startpos.x, startpos.y), speed,
                                                               angle, wind,  time, mass)
            else:
                newPos = Physics.CalculateNexPosition(pygame.math.Vector2(startpos.x, startpos.y), speed, angle, time)

            time += 0.05

        return trajPoints


