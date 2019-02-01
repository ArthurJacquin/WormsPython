import pygame


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2
        self.isJumping = False
        self.jumpCount = 10
        self.jumpHeight = 0.1
        self.left = False
        self.right = False
        self.walkCount = 0
        self.hasShot = False
        self.facing = 1

        # Player Sprites
        self.walkRight = [pygame.image.load('Images\Rwalk1.png'),
                          pygame.image.load('Images\Rwalk2.png'),
                          pygame.image.load('Images\Rwalk3.png'),
                          pygame.image.load('Images\Rwalk4.png'),
                          pygame.image.load('Images\Rwalk5.png'),
                          pygame.image.load('Images\Rwalk6.png'),
                          pygame.image.load('Images\Rwalk7.png'),
                          pygame.image.load('Images\Rwalk8.png'),
                          pygame.image.load('Images\Rwalk9.png'),
                          pygame.image.load('Images\Rwalk10.png'),
                          pygame.image.load('Images\Rwalk11.png'),
                          pygame.image.load('Images\Rwalk12.png'),
                          pygame.image.load('Images\Rwalk13.png'),
                          pygame.image.load('Images\Rwalk14.png'),
                          pygame.image.load('Images\Rwalk15.png')]
        self.walkLeft = [pygame.image.load('Images\Lwalk1.png'),
                         pygame.image.load('Images\Lwalk2.png'),
                         pygame.image.load('Images\Lwalk3.png'),
                         pygame.image.load('Images\Lwalk4.png'),
                         pygame.image.load('Images\Lwalk5.png'),
                         pygame.image.load('Images\Lwalk6.png'),
                         pygame.image.load('Images\Lwalk7.png'),
                         pygame.image.load('Images\Lwalk8.png'),
                         pygame.image.load('Images\Lwalk9.png'),
                         pygame.image.load('Images\Lwalk10.png'),
                         pygame.image.load('Images\Lwalk11.png'),
                         pygame.image.load('Images\Lwalk12.png'),
                         pygame.image.load('Images\Lwalk13.png'),
                         pygame.image.load('Images\Lwalk14.png'),
                         pygame.image.load('Images\Lwalk15.png')]
        self.char = pygame.image.load('Images\Rwalk1.png')

    def draw(self, win):
        if self.walkCount + 1 >= 45:
            self.walkCount = 0

        if self.left:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(self.char, (self.x,self.y))
