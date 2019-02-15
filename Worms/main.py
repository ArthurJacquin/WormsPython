from Worms.Game import *
from Worms.GroundGenerator import *
from Worms.Collision import *
from Worms.Physics import *
import time
from Worms.Menu import *

pygame.init()

# Open window
screenWidth = 850
screenHeight = 480
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Worms")
sol = list()
game = Game(sol, screenHeight, screenWidth)
menu = Menu()
currentPlayer = game.players[game.currentPlayerIndex]
rocket = game.rocket
grenade = game.grenade

#groundGenerator(screenHeight, screenWidth, window, sol, 1)

# main loop
windowOpen = 1
while windowOpen:

    # time between frames
    game.clock.tick(30)

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
            if event.key == pygame.K_SPACE and game.grenadeSelected:
                grenade.setupForShoot(currentPlayer, currentPlayer.facing)
                currentPlayer.hasShot = True
                game.grenadeShot = True
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
            if not currentPlayer.isShooting:
                currentPlayer.isShooting = True

            game.updatePower()

            if grenade.vel >= 20:
                grenade.setupForShoot(currentPlayer, currentPlayer.facing)
                currentPlayer.hasShot = True
                game.grenadeShot = True
                currentPlayer.isShooting = False
                currentPlayer.shootPowerBar.width = 0

    else:
        currentPlayer.standing = True
        currentPlayer.walkCount = 0

    # Move crosshair
    if keys[pygame.K_UP] and currentPlayer.crosshair.angle < 180:
        currentPlayer.crosshair.move(1)

    if keys[pygame.K_DOWN] and currentPlayer.crosshair.angle > 0:
        currentPlayer.crosshair.move(-1)

    # Player with ground collision
    fall = 0
    for player in game.players:
        pixelDetector = (player.x, player.y + player.height - 20)
        for i in sol[player.x - 20 : player.x + 20]:
           if pixelDetector not in sol:
               fall = 1
           else:
                fall = 0
        #if fall == 1:
        #    player.y += 3
        #else :
            #todo: gérer la marche sur le sol

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

    fallRocket = 0
    # Rocket
    if game.rocketShot:
        game.time += 0.05
        newPos = Physics.CalculateNexPosition(pygame.math.Vector2(rocket.x, rocket.y), rocket.vel,
                                              pygame.math.Vector2(5, 0), currentPlayer.crosshair.angle, game.time)

        #Rocket with Ground collision
        for i in sol[int(rocket.x) - 20 : int(rocket.x) + 20]:
            if rocket.y + rocket.radius <= i[1]:
                fallRocket = 0
            else:
                fallRocket = 1
                break
        if fallRocket == 0:
            rocket.y = newPos.y
            rocket.x = newPos.x
        else:
            rocket.y = rocket.y
            rocket.x = rocket.x
            rocket.radius += 2
            if rocket.radius > 30:
                rocket.radius = 0
                game.rocketShot = False
                game.rocketSelected = False
                game.time = 0
                game.rocket.vel = 3

                # player switch
                game.players[game.currentPlayerIndex % len(game.players)].hasShot = False
                currentPlayer = game.switchPlayer()

        # Rocket with player collision
        for player in game.players:
            rect = pygame.Rect(player.x, player.y, player.width, player.height)
            if rect.collidepoint(rocket.x, rocket.y) and player != currentPlayer:
                rocket.x = player.x + player.width/2
                rocket.y = player.y + player.height/2
                rocket.radius += 2
                if rocket.radius > 30:
                    rocket.radius = 0
                    game.rocketShot = False
                    game.rocketSelected = False
                    game.time = 0
                    game.rocket.vel = 3
                    # todo : gérer player life

                    # player switch
                    game.players[game.currentPlayerIndex % len(game.players)].hasShot = False
                    currentPlayer = game.switchPlayer()

    # Grenade
    if game.grenadeShot:
        game.time += 0.05
        newPos = Physics.CalculateNexPosition(pygame.math.Vector2(grenade.x, grenade.y), grenade.vel,
                                              pygame.math.Vector2(5, 0), currentPlayer.crosshair.angle, game.time)

        # Rocket with Ground collision
        for i in sol[int(grenade.x) - 10 : int(grenade.x) + 10]:
            if grenade.y + grenade.radius <= i[1]:
                fallGrenade = 0
            else:
                fallGrenade = 1
                break

        if fallGrenade == 0:
            grenade.x = newPos.x
            grenade.y = newPos.y
        else:
            grenade.x = grenade.x
            grenade.y = grenade.y


            #todo : delay avant explosion
            grenade.radius += 2
            if grenade.radius > 20:
                grenade.radius = 0
                game.grenadeShot = False
                game.grenadeSelected = False
                game.time = 0
                game.grenade.vel = 0

                # todo : gérer player life

                # player switch
                game.players[game.currentPlayerIndex % len(game.players)].hasShot = False
                currentPlayer = game.switchPlayer()

        # Rocket with player collision
        for player in game.players:
            rect = pygame.Rect(player.x, player.y, player.width, player.height)
            if rect.collidepoint(grenade.x, grenade.y) and player != currentPlayer:
                grenade.x = player.x + player.width / 2
                grenade.y = player.y + player.height / 2
                grenade.radius += 2
                if grenade.radius > 20:
                    grenade.radius = 0
                    game.grenadeShot = False
                    game.grenadeSelected = False
                    game.time = 0
                    game.grenade.vel = 0
                    print("collision with player")
                    # todo : gérer player life

                    # player switch
                    game.players[game.currentPlayerIndex % len(game.players)].hasShot = False
                    currentPlayer = game.switchPlayer()

    game.redrawGameWindow(window, screenHeight, screenWidth)

# def grenade():

pygame.quit()