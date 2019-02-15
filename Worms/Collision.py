import pygame
from Worms.Physics import *
from Worms.Rocket import *
from Worms.Grenade import *
from Worms.GroundGenerator import *

# Calcul normal sol pour rebonds
def GroundNormal(impactPos, sol):
    pointA = impactPos + 1
    pointB = pygame.math.Vector2(impactPos.x - 1, impactPos.y)
    pointC = impactPos - 1
    pointD = pygame.math.Vector2(impactPos.x, impactPos.y - 1)
    normal = pygame.math.Vector2(0, 0)
    tabPoint = [pointA, pointB, pointC, pointD]

    # pour chaque point dans le terrain, on calcule la moyenne des vecteurs des points
    for point in tabPoint:
        if point in sol:
            normalPoint = normalPoint + tabPoint[point]

    normal = pygame.math.Vector2(impactPos, normalPoint)
    return normal


#rebonds
def CalculRebonds(grenade, time):
    rebonds = 0
    if rebonds > 0 and rebonds <= 2:

        grenade.vel -= 2
        time = 0
        grenade.x = grenade.x
        grenade.y = grenade.y
        newPosRebonds = Physics.CalculateNexPosition(pygame.math.Vector2(grenade.x, grenade.y), grenade.vel,
                                                     pygame.math.Vector2(0, 0), 48, time)
        grenade.x = -newPosRebonds.x
        grenade.y = -newPosRebonds.y

        #Debug
        print("rebonds : ", rebonds)
        rebonds += 1
        return pygame.math.Vector2(grenade.x, grenade.y)
