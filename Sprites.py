# ROCKET GAME #

import pygame
from pygame_functions import *
pygame.init()

horSize = 1000
vertSize = 750
screenSize(horSize, vertSize)

setBackgroundImage("stars.png")

rocket = makeSprite("rocket1.png")
showSprite(rocket)

xPos = 500
yPos = 375
xSpeed = 0
ySpeed = 0
vel = 2
fps= 20
CLOCK = pygame.time.Clock()
run = True

while run:
    CLOCK.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        transformSprite(rocket, -90, 1)
        xSpeed -= vel
    if keys[pygame.K_RIGHT]:
        transformSprite(rocket, 90, 1)
        xSpeed += vel
    if keys[pygame.K_UP]:
        transformSprite(rocket, 0, 1)
        ySpeed -= vel
    if keys[pygame.K_DOWN]:
        transformSprite(rocket, 180, 1)
        ySpeed += vel
        
    #Combinations
    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        transformSprite(rocket, -45, 1)
        xSpeed -= vel/2
        ySpeed -= vel/2
    if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        transformSprite(rocket, 45, 1)
        xSpeed += vel/2
        ySpeed -= vel/2
    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        transformSprite(rocket, -135, 1)
        xSpeed -= vel/2
        ySpeed += vel/2
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        transformSprite(rocket, 135, 1)
        xSpeed += vel/2
        ySpeed += vel/2
    if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
        transformSprite(rocket, 0, 1)
        ySpeed = 0
    if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
        transformSprite(rocket, 0, 1)
        xSpeed = 0
## HANDLES LOOPING ##
    xPos += xSpeed
    if xPos > vertSize + 210:
        xPos = -100
    elif xPos < -100:
        xPos = vertSize + 210

    yPos += ySpeed
    if yPos > horSize - 300:
        yPos = -100
    elif yPos < -100:
        yPos = horSize -300

    moveSprite(rocket, xPos, yPos)
## ALLOWS CHECKING TO SEE IF ESCAPE IS PRESSED ##
    tick(30)

#    pygame.display.update()

## WHEN 'ESC' IS PRESSED, GAME WINDOW CLOSES ##

endWait()
