import pygame
from Worms.Player import *
from Worms.Rocket import *
from Worms.Physics import *
from Worms.Vector2 import Vector2

pygame.init()

#Open window
screenWidth = 850
screenHeight = 480
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Worms")

#Player
player = Player(100, screenHeight - 65, 60, 60)
rocketShot = False

#Background sprite
bg = pygame.image.load('Images\Background.jpg')

#FPS
clock = pygame.time.Clock()

#Update window
def redrawGameWindow():
    window.blit(bg, (0,0))
    pygame.draw.rect(window,(88, 41, 0), (0, screenHeight - 25, screenWidth, 25))
    player.draw(window)

    if rocketShot:
        rocket.draw(window)
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

    #movements
    keys = pygame.key.get_pressed()

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
        # Rocket shot
        rocket = Rocket(round(player.x + player.width // 2), round(player.y + player.height // 2), 6, (0, 0, 0), facing)
        player.hasShot = True
        rocketShot = True
    else:
        player.standing = True
        player.walkCount = 0

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
    if rocketShot:
        if rocket.x < screenWidth and rocket.x > 0 and rocket.y < screenHeight and rocket.y > 0:
            #Formule de trajectoire à mettre ici
            speedVector = Physics.CalculateSpeedVector(rocket.vel, 45)
            newPos = Physics.CalculateNexPosition(Vector2(rocket.x, rocket.y), speedVector, 0.1, Vector2(0,0))
            rocket.x = newPos.x
            rocket.y = newPos.y

        else:
            rocketShot = False

    redrawGameWindow()

pygame.quit()
