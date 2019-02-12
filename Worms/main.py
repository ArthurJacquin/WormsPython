from Worms.Game import *
from Worms.GroundGenerator import *
from Worms.Collision import *
import numpy as np
from Worms.Menu import *

pygame.init()

# Open window
screenWidth = 850
screenHeight = 480
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Worms")
sol = list()
game = Game(sol)
menu = Menu()
currentPlayer = game.players[game.currentPlayerIndex]
rocket = game.rocket
grenade = game.grenade

groundGenerator(screenHeight, screenWidth, window, sol, 1)

# main loop
windowOpen = 1
while windowOpen:

    # time between frames
    game.clock.tick(60)

    if menu.isActive:
        menu.displayMenu(window, screenWidth, screenHeight)

    game.updateTime()

    currentPlayer.updatePlayerUI()

    # Switch player if time = 0
    if pygame.time.get_ticks() - game.startTurnTime > game.maxTimePerTurn:
        currentPlayer = game.switchPlayer()

    keys = pygame.key.get_pressed()

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windowOpen = 0

        if event.type == pygame.KEYUP and currentPlayer.isShooting:
            if event.key == pygame.K_SPACE and game.rocketSelected:
                rocket.setupForShoot(currentPlayer, currentPlayer.facing)
                currentPlayer.hasShot = True
                game.rocketShot = True
                currentPlayer.isShooting = False
                currentPlayer.shootPowerBar.width = 0

    # Weapon selection
    if keys[pygame.K_1]:
        game.rocketSelected = True
        game.grenadeSelected = False

    if keys[pygame.K_2]:
        game.rocketSelected = False
        game.grenadeSelected = True

    # movements
    if keys[pygame.K_LEFT] and currentPlayer.x > currentPlayer.vel:
        currentPlayer.x -= currentPlayer.vel
        currentPlayer.left = True
        currentPlayer.right = False
        currentPlayer.standing = False

    elif keys[pygame.K_RIGHT] and currentPlayer.x < screenWidth - currentPlayer.width - currentPlayer.vel:
        currentPlayer.x += currentPlayer.vel
        currentPlayer.right = True
        currentPlayer.left = False
        currentPlayer.standing = False

    elif keys[pygame.K_SPACE] and not currentPlayer.hasShot:

        if game.rocketSelected:
            # Increase power
            if not currentPlayer.isShooting:
                currentPlayer.isShooting = True

            game.updatePower()

            #Shoot if max power
            if rocket.vel >= 20:
                rocket.setupForShoot(currentPlayer, currentPlayer.facing)
                currentPlayer.hasShot = True
                game.rocketShot = True
                currentPlayer.isShooting = False
                currentPlayer.shootPowerBar.width = 0

        if game.grenadeSelected:
            # Grenade shot
            grenade = Grenade(round(currentPlayer.x + currentPlayer.width // 2),
                              round(currentPlayer.y + currentPlayer.height // 2), 6, currentPlayer.facing)
            currentPlayer.hasShot = True
            game.grenadeShot = True
    else:
        currentPlayer.standing = True
        currentPlayer.walkCount = 0

    # Move crosshair
    if keys[pygame.K_UP] and currentPlayer.crosshair.angle < 180:
        currentPlayer.crosshair.move(1)

    if keys[pygame.K_DOWN] and currentPlayer.crosshair.angle > 0:
        currentPlayer.crosshair.move(-1)

    for player in game.players:
        if player.y + 45 < screenHeight - 25 and not player.isJumping:
            player.y += 9

    # Jump
    if not currentPlayer.isJumping:
        if keys[pygame.K_RETURN]:
            currentPlayer.isJumping = True
            currentPlayer.right = False
            currentPlayer.left = False
            currentPlayer.walkCount = 0
    else:
        if currentPlayer.jumpCount >= -10:
            neg = 1
            if currentPlayer.jumpCount < 0:
                neg = -1

            currentPlayer.y -= (currentPlayer.jumpCount ** 2) * currentPlayer.jumpHeight * neg
            currentPlayer.jumpCount -= 1
        else:
            currentPlayer.isJumping = False
            currentPlayer.jumpCount = 10

    # Weapons
    if currentPlayer.left:
        currentPlayer.facing = -1
    else:
        currentPlayer.facing = 1

    # Rocket
    if game.rocketShot: #and rocket.y + 3 < screenHeight - 25 and rocket.x < screenWidth and rocket.x > 0 and rocket.y < screenHeight and rocket.y > 0: # Si pas de collision
            game.time += 0.05
            newPos = Physics.CalculateNexPosition(pygame.math.Vector2(rocket.x, rocket.y), rocket.vel,
                                                  pygame.math.Vector2(5, 0), currentPlayer.crosshair.angle, game.time)
            rocket.x = newPos.x
            rocket.y = newPos.y
            pos = (rocket.x, rocket.y)


            for i in sol:
                if pos == sol:
                    continue
                dist = np.linalg.norm(pos - sol[i])
                if dist < rocket.radius:
                    print("collision")

    #Collision -> explosion
    elif game.rocketShot:
        rocket.radius += 2
        if rocket.radius > 30:
            rocket.radius = 0
            game.rocketShot = False
            game.rocketSelected = False
            game.time = 0
            game.rocket.vel = 0

            #player switch
            game.players[game.currentPlayerIndex % len(game.players)].hasShot = False
            currentPlayer = game.switchPlayer()

    # Grenade
    if game.grenadeShot:
        if grenade.x < screenWidth and grenade.x > 0 and grenade.y < screenHeight and grenade.y > 0:
            game.time += 0.05
            newPos = Physics.CalculateNexPosition(pygame.math.Vector2(grenade.x, grenade.y), grenade.vel,
                                                  pygame.math.Vector2(0, 0), currentPlayer.crosshair.angle, game.time)

            grenade.x = newPos.x
            grenade.y = newPos.y

    # elif collision and nbRebond < 5:
    # grenade.ResetSpeedVector()
    # grenade.grenadeShot()
    # else:
    # explosion()

    game.redrawGameWindow(window, screenHeight, screenWidth)

# def grenade():

pygame.quit()