import pygame
from Worms.Player import *
from Worms.Rocket import *
from Worms.Physics import *
from Worms.Grenade import *

pygame.init()

#Open window
screenWidth = 850
screenHeight = 480
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Worms")

#Player
player = Player(100, 350, 60, 60)


rocketShot = False
grenadeShot = False

time = 0

#Weapon selected
rocketSelected = False
grenadeSelected = False

#Background sprite
bg = pygame.image.load('Images\Background.jpg')

#FPS
clock = pygame.time.Clock()

#Update window
def redrawGameWindow():
    window.blit(bg, (0,0))
    pygame.draw.rect(window,(88, 40, 0), (0, screenHeight - 25, screenWidth, 25))
    player.draw(window)

    if rocketShot:
        rocket.draw(window)

    if grenadeShot:
        grenade.draw(window)
    pygame.display.update()

#main loop
windowOpen = 1
while windowOpen:
    #time between frames
    clock.tick(60)

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windowOpen = 0


    keys = pygame.key.get_pressed()

    #Weapon selected
    if keys[pygame.K_1]:
        rocketSelected = True
        grenadeSelected = False
    if keys[pygame.K_2]:
        rocketSelected = False
        grenadeSelected = True

    # movements
    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pygame.K_RIGHT] and player.x < screenWidth - player.width - player.vel :
        player.x += player.vel
        player.right = True
        player.left = False
        player.standing = False
    elif keys[pygame.K_SPACE] and not player.hasShot:
        if rocketSelected:
            # Rocket shot
            rocket = Rocket(round(player.x + player.width // 2), round(player.y + player.height // 2), 6, facing)
            player.hasShot = True
            rocketShot = True
        if grenadeSelected:
            grenade = Grenade(round(player.x + player.width // 2), round(player.y + player.height // 2), 6, facing)
            player.hasShot = True
            grenadeShot = True
    else:
        player.standing = True
        player.walkCount = 0

    if player.y + 45 < screenHeight - 25 and not player.isJumping:
        player.y += 9

    #Jump
    if not player.isJumping:
        if keys[pygame.K_RETURN]:
            player.isJumping = True
            player.right = False
            player.left = False
            player.walkCount = 0
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1

            player.y -= (player.jumpCount ** 2) * player.jumpHeight * neg
            player.jumpCount -= 1
        else:
            player.isJumping = False
            player.jumpCount = 10

    #Weapons
    if player.left:
        facing = -1
    else:
        facing = 1

    #Rocket
    if rocketShot and rocket.y + 3 < screenHeight - 25:
        if rocket.x < screenWidth and rocket.x > 0 and rocket.y < screenHeight and rocket.y > 0:
            #Formule de trajectoire à mettre ici
            time +=0.02
            newPos = Physics.CalculateNexPosition(pygame.math.Vector2(rocket.x, rocket.y), rocket.vel, pygame.math.Vector2(5,0),50 , facing, time)

            rocket.x = newPos.x
            rocket.y = newPos.y

        else:
            rocketShot = False
    elif rocketShot:
        rocket.radius += 2
        if rocket.radius > 30:
            rocket.radius = 0
            rocketShot = False

    #Grenade
    if grenadeShot:
        if grenade.x < screenWidth and grenade.x > 0 and grenade.y < screenHeight and grenade.y > 0:
            time += 0.02
            newPos = Physics.CalculateNexPosition(pygame.math.Vector2(grenade.x, grenade.y), grenade.vel,
                                                  pygame.math.Vector2(0, 0), 45, facing, time)

            grenade.x = newPos.x
            grenade.y = newPos.y

    #elif collision and nbRebond < 5:
        #grenade.ResetSpeedVector()
        #grenade.grenadeShot()
    #else:
        #explosion()

    redrawGameWindow()

#def grenade():

pygame.quit()
