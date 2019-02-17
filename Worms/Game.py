import pygame
from Worms.Player import *
from Worms.Rocket import *
from Worms.Grenade import *
from Worms.Crosshair import *
from Worms.GroundGenerator import *


class Game:
    def __init__(self, sol, screenHeight, screenWidth):

        self.sol = sol
        self.players = list()

        # Player
        for i in range(0, 4):
            player = Player(random.randrange(20, screenWidth - 50), 200, 60, 60)
            self.players.append(player)

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

        # Wind
        self.wind = pygame.math.Vector2(3, 2)

        # Background sprites
        self.bg = pygame.image.load('Images\Background.jpg')

        # FPS
        self.clock = pygame.time.Clock()

        # Turn time
        self.maxTimePerTurn = 60000
        self.startTurnTime = 0
        self.currentTurnTime = round(self.startTurnTime / 1000)

        # Turn time text
        self.fontTime = pygame.font.Font('Font\Freesansbold.ttf', 48)
        self.timerText = self.fontTime.render(str(self.maxTimePerTurn), True, (255, 0, 0))

        #windText
        self.fontWind = pygame.font.Font('Font\Freesansbold.ttf', 20)
        self.windText = self.fontWind.render("Wind : x: %.1f  y: %.1f" % (self.wind.x, self.wind.y * -1), True, (0, 0, 0))

        # Weapon sprites
        self.bazookaSprite = pygame.image.load('Images\Bazooka.png')
        self.grenadeSprite = pygame.image.load('Images\Grenade.png')

        #ground generation
        groundGenerator(screenHeight, screenWidth, self.sol)

        #Trajectory
        self.displayTrajectory = False
        self.powerForDisplay = 5

    # Update window
    def redrawGameWindow(self, window, screenHeight, screenWidth):
        window.blit(self.bg, (0, 0))
        window.blit(self.timerText, (10, 10))

        groundRefresh(screenHeight, window, self.sol)

        # Timer
        window.blit(self.timerText, (10, 10))

        # Selected weapon
        if self.rocketSelected:
            window.blit(self.bazookaSprite, (screenWidth - 50, screenHeight - 50))
        if self.grenadeSelected:
            window.blit(self.grenadeSprite, (screenWidth - 50, screenHeight - 50))

        # Wind Indicator
        window.blit(self.windText, (screenWidth - 200, 10))

        # Players
        for player in self.players:
            player.draw(window)

        # Crosshair
        self.players[self.currentPlayerIndex % len(self.players)].crosshair.draw(window)

        # Trajectory
        if self.displayTrajectory:
            if self.rocketSelected:
                traj = Physics.GetTrajectory(pygame.math.Vector2(self.players[self.currentPlayerIndex].x + self.players[self.currentPlayerIndex].width/2,
                                                                 self.players[self.currentPlayerIndex].y + self.players[self.currentPlayerIndex].height/2),
                                                                 self.powerForDisplay, self.sol, self.players[self.currentPlayerIndex].crosshair.angle,
                                                                 self.wind, True, 1)

                for pixel in traj:
                    window.set_at(pixel, (0, 0, 0))

            if self.grenadeSelected:
                traj = Physics.GetTrajectory(pygame.math.Vector2(self.players[self.currentPlayerIndex].x + self.players[self.currentPlayerIndex].width/2,
                                                                 self.players[self.currentPlayerIndex].y + self.players[self.currentPlayerIndex].height/2),
                                                                 self.powerForDisplay, self.sol, self.players[self.currentPlayerIndex].crosshair.angle)

                for pixel in traj:
                    window.set_at(pixel, (0, 0, 0))

        # Shoot power bar
        if self.players[self.currentPlayerIndex].isShooting:
            self.players[self.currentPlayerIndex].shootPowerBar.draw(window)

        # Weapons
        if self.rocketShot:
            self.rocket.draw(window)
        if self.grenadeShot:
            self.grenade.draw(window)



        pygame.display.update()

    # Update time text
    def updateTime(self):
        if self.startTurnTime == 0:
            self.startTurnTime = pygame.time.get_ticks()
        self.currentTurnTime = round((self.maxTimePerTurn - (pygame.time.get_ticks() - self.startTurnTime)) / 1000)
        self.timerText = self.fontTime.render(str(self.currentTurnTime), True, (255, 0, 0))

    # Switch to next player
    def switchPlayer(self):
        self.players[self.currentPlayerIndex].right = False
        self.players[self.currentPlayerIndex].left = False


        self.currentPlayerIndex = (self.currentPlayerIndex + 1) % len(self.players)
        self.startTurnTime = pygame.time.get_ticks()
        self.currentTurnTime = round(self.startTurnTime / 1000)

        #Update wind
        self.wind = pygame.math.Vector2(random.randrange(-5, 5), random.randrange(-2.0, 2.0))

        self.windText = self.fontWind.render("Wind : x: %.1f  y: %.1f" % (self.wind.x, self.wind.y * -1), True, (0, 0, 0))

        self.powerForDisplay = 5

        return self.players[self.currentPlayerIndex]

    def updatePower(self):
        self.players[self.currentPlayerIndex].shootPowerBar.width += 1
        self.rocket.vel += 0.2
        self.grenade.vel += 0.2


    def damagePlayer(self, player):
        i = 0
        for p in self.players:
            if p == player:
                self.players.remove(p)
                return i
            i += 1

    def endGame(self, menu):
        menu.isActive = True





