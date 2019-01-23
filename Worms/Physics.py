import math
from sympy import pi
from Worms.Vector2 import Vector2

class Physics:

    @staticmethod
    def CalculateSpeedVector(speed, angle):
        vec = Vector2(math.cos(angle * pi / 180), math.sin(angle * pi /180))
        vec *= speed
        return vec

    @staticmethod
    def CalculateNexPosition(startPos, speed, time, wind):
        forces = Vector2(0, -9.81) + wind
        return startPos + speed * time + forces * .5 * (time ** 2)