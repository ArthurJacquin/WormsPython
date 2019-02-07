import pygame
from Worms.Physics import *
from Worms.Rocket import *
from Worms.Grenade import *
from Worms.GroundGenerator import *
from Worms.main import *

#récupération de la position de la balle
def GroundCollisionRocket(rocket, sol):
    pos = (rocket.x, rocket.y)
    for i in sol:
        if pos == sol[i]:
            impactPos = pygame.math.Vector2(rocket.x + (rocket.radius/2), rocket.y + (rocket.radius/2))
            break
    return impactPos

def GroundCollisionGrenade(grenade, sol):
    pos = (rocket.x, rocket.y)
    for i in sol :
        if pos == sol[i]:
            impactPos = pygame.math.Vector2(grenade.x + (grenade.radius/2), grenade.y + (grenade.radius/2))
            break
    return impactPos

#Calcul normal sol pour rebonds
def GroundNormal(impactPos, sol):
    pointA = impactPos + 1
    pointB = pygame.math.Vector2(impactPos.x - 1, impactPos.y)
    pointC = impactPos - 1
    pointD = pygame.math.Vector2(impactPos.x, impactPos.y - 1)
    normal = pygame.math.Vector2(0, 0)
    tabPoint = [pointA, pointB, pointC, pointD]

    #pour chaque point dans le terrain, on calcule la moyenne des vecteurs des points
    for point in tabPoint :
        if point in sol:
            normalPoint = normalPoint + tabPoint[point]

    normal = pygame.math.Vector2(impactPos, normalPoint)
    return normal

#Collision avec le sol
def Rebond(impactPos, grenade, sol):
    rebonds = 0
    while(rebonds != 2):
        #calcul du rebond
