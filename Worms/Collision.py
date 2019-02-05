import pygame
from Worms.Physics import *
from Worms.Rocket import *

#récupération de la position de la balle
def ImpactPoint(rocket):
    impactPos = pygame.math.Vector2(rocket.x + (rocket.radius/2), rocket.y + (rocket.radius/2)) #+ajout du vecteur de la trajectoire pour avoir le point qui suit la trajectoire
    return impactPos

#Collision avec le sol
#def GroundCollision(impactPos, #index des points du terrain):

#Calcul normal sol pour rebonds
def GroundNormal (impactPos):
    pointA = impactPos + 1
    pointB = pygame.math.Vector2(impactPos.x - 1, impactPos.y)
    pointC = impactPos - 1
    pointD = pygame.math.Vector2(impactPos.x, impactPos.y - 1)

#peut-être plus opti de les mettre dans un tableau
    #pour chaque point dans le terrain
    if point in #terrain:
        normal = #vecteur2(coordonné du point, point d'impact)
    #moyenne vecteur normal
    return normal