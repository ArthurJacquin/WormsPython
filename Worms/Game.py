import pygame
from Worms.Player import *
from Worms.Rocket import *
from Worms.Grenade import *


class Game:
    def __init__(self):

        # Player
        self.player = Player(100, 350, 60, 60)
        self.player2 = Player(400, 350, 60, 60)

        self.players = [self.player, self.player2]
        self.currentPlayerIndex = 0

        self.rocketShot = False
        self.grenadeShot = False

        self.time = 0

        # Weapons creation
        self.rocket = Rocket()
        self.grenade = Grenade(-50, -50, 0, 1)

        # Weapon selected
        self.rocketSelected = False
        self.grenadeSelected = False

        # Background sprite
        self.bg = pygame.image.load('Images\Background.jpg')

        # FPS
        self.clock = pygame.time.Clock()

        # Turn time
        self.maxTimePerTurn = 60000
        self.startTurnTime = pygame.time.get_ticks()
        self.currentTurnTime = round(self.startTurnTime / 1000)

        # Turn time text
        self.timer = pygame.font.Font('Font\Freesansbold.ttf', 48)
        self.timerText = self.timer.render(str(self.maxTimePerTurn), True, (255, 0, 0))

    # Update window
    def redrawGameWindow(self, window, screenHeight, screenWidth):
        window.blit(self.bg, (0, 0))
        window.blit(self.timerText, (10, 10))

        pygame.draw.rect(window, (88, 40, 0), (0, screenHeight - 25, screenWidth, 25))

        for player in self.players:
            player.draw(window)

        self.rocket.draw(window)
        self.grenade.draw(window)
        pygame.display.update()

    # Update time text
    def updateTime(self):
        self.currentTurnTime = round((self.maxTimePerTurn - (pygame.time.get_ticks() - self.startTurnTime)) / 1000)
        self.timerText = self.timer.render(str(self.currentTurnTime), True, (255, 0, 0))

    # Switch to next player
    def switchPlayer(self):
        self.currentPlayerIndex += 1
        self.startTurnTime = pygame.time.get_ticks()
        self.currentTurnTime = round(self.startTurnTime / 1000)

        return self.players[self.currentPlayerIndex % len(self.players)]

