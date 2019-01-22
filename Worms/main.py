import pygame
from Player import *
pygame.init()

#Open window
screenWidth = 850
screenHeight = 480
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tuto")

#Player
player = Player(300, 410, 60, 60)

#Background sprite
bg = pygame.image.load('Images\Background.jpg')

#FPS
clock = pygame.time.Clock()

#Update window
def redrawGameWindow():
    window.blit(bg, (0,0))
    player.draw(window)
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
    elif keys[pygame.K_RIGHT] and player.x < screenWidth - player.width - player.vel :
        player.x += player.vel
        player.right = True
        player.left = False
    else:
        player.right = False
        player.left = False
        player.walkCount = 0

    #Jump
    if not player.isJumping:
        if keys[pygame.K_SPACE]:
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

    redrawGameWindow()

pygame.quit()
