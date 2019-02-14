import pygame
from Worms.Game import *


class Menu:
    def __init__(self):
        self.menuBg = pygame.image.load('Images\Background.jpg')
        self.font = pygame.font.Font('Font\Freesansbold.ttf', 55)
        self.isActive = True

    def displayMenu(self, window, screenWidth, screenHeight):
        menu = True

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            window.blit(self.menuBg, (0, 0))

            pygame.draw.rect(window, (0, 0, 255), (screenWidth / 2 - 75, screenHeight / 2 - 100, 150, 75))
            pygame.draw.rect(window, (0, 0, 255), (screenWidth / 2 - 75, screenHeight / 2 + 25, 150, 75))

            playText = self.font.render('PLAY', True, (255, 255, 255))
            quitText = self.font.render('QUIT', True, (255, 255, 255))

            window.blit(playText, (screenWidth / 2 - 70, screenHeight / 2 - 85))
            window.blit(quitText, (screenWidth / 2 - 70, screenHeight / 2 + 40))

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if screenWidth / 2 - 75 < mouse[0] < screenWidth / 2 + 75 and screenHeight / 2 - 100 < mouse[1] < screenHeight / 2 - 25 and click[0] == 1:
                pygame.display.update()
                self.isActive = False
                menu = False
            if screenWidth / 2 - 75 < mouse[0] < screenWidth / 2 + 75 and screenHeight / 2 + 25 < mouse[1] < screenHeight / 2 + 100 and click[0] == 1:
                pygame.quit()
                quit()

            pygame.display.update()

