import random
from Worms.Game import *


def groundGenerator(height, width, tabSurface):

    hauteurPixel = int(height - height / 8)
    probaUp = 1
    probaStay =2

    """ pour chaque pixel de la longueur, on monte ou on descend d'un pixel et on le colorie en rouge"""
    for i in range(0, width):

        choix = random.uniform(0.0, 3)

        """si le random est supérieur a probaUp, on descend et on inverse les probas"""
        if (choix <= probaUp):
            hauteurPixel = hauteurPixel - 1
            probaUp = 2
            probaStay = 2.5

        elif choix <=  probaStay and probaUp < choix:

            hauteurPixel = hauteurPixel + 1
            probaStay= 1.0
            probaUp = 0.5

        else:
            probaStay = 2.5
            probaUp = 0.5

        tabSurface.append((i, hauteurPixel))

def groundRefresh(height, window, tabSurface):

    for pixel in tabSurface:

        for i in range(pixel[1], height):
            window.set_at((pixel[0], i), (88, 40, 0, 255))
