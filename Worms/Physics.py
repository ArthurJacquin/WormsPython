import math
import pygame

class Physics:

    def to_pygame(coords, height, obj_height):
        """Convert an object's coords into pygame coordinates (lower-left of object => top left in pygame coords)."""
        return (coords[0], height - coords[1] - obj_height)

    @staticmethod
    def CalculateSpeedVector(speed, angle, direction):
        vec = pygame.math.Vector2(math.cos(angle * math.pi / 180) * direction, math.sin(angle * math.pi /180))
        vec *= speed
        return vec

    @staticmethod
    def CalculateNexPosition(startPos, speed, wind, angle, direction, time):
        gravity = -9.81
        speedVec = pygame.math.Vector2(math.cos(math.radians(angle)) * speed, math.sin(math.radians(angle)) * speed)

        if direction == 1:
            newX = startPos.x + speedVec.x * time
        else:
            newX = startPos.x - speedVec.x * time

        newY = startPos.y - ((speedVec.y * time) + (gravity * 0.5 * time ** 2))

        return pygame.math.Vector2(newX, newY)


