import random
from Worms.Game import *


def groundGenerator(height, width, window, tabGround, draw):
    """si le draw est à 1, on dessine la ligne, sinon on ne fait que la refresh"""
    if draw == 1:

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
                print(str(i) + "a plat\n")
                probaStay = 2.5
                probaUp = 0.5

            """on ajoute au tableau tous les pixels situés en dessous"""

            for j in range(hauteurPixel, height):

                tabGround.append((i, j))



    else:
        """on redessine la ligne déjà générée"""

        for pixel in tabGround:
            window.set_at(pixel, (88, 40, 0, 255))
