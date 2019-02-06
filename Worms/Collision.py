import pygame
from Worms.Physics import *
from Worms.Rocket import *
from Worms.Grenade import *

#récupération de la position de la balle
def ImpactPointRocket(rocket):
    impactPos = pygame.math.Vector2(rocket.x + (rocket.radius/2), rocket.y + (rocket.radius/2))
    #+ajout du vecteur de la trajectoire pour avoir le point qui suit la trajectoire
    return impactPos

def ImpactPointGrenade(grenade):
    impactPos = pygame.math.Vector2(grenade.x + (grenade.radius/2), grenade.y + (grenade.radius/2))
    return impactPos

#Calcul normal sol pour rebonds
def GroundNormal(impactPos):
    pointA = impactPos + 1
    pointB = pygame.math.Vector2(impactPos.x - 1, impactPos.y)
    pointC = impactPos - 1
    pointD = pygame.math.Vector2(impactPos.x, impactPos.y - 1)
    normal = pygame.math.Vector2(0, 0)
    tabPoint = [pointA, pointB, pointC, pointD]

    #pour chaque point dans le terrain, on calcule la moyenne des vecteurs des points
    for point in tabPoint :
        if point in #terrain:
            normal = normal + tabPoint[point]
    return normal

#if we define dx=x2-x1 and dy=y2-y1, then the normals are (-dy, dx) and (dy, -dx).
#normal = pygame.math.Vector2(normal, point d'impact)

#Collision avec le sol
def GroundCollision(impactPos, normal, rocket, grenade): #index des points du terrain):
    for i in #terrain :
        if i == impactPos:

