#                      __        __
#     _________  _____/ /_____  / /_   ____ _____ _____ ___  ___
#    / ___/ __ \/ ___/ //_/ _ \/ __/  / __ `/ __ `/ __ `__ \/ _ \
#   / /  / /_/ / /__/ ,< /  __/ /_   / /_/ / /_/ / / / / / /  __/
#  /_/   \____/\___/_/|_|\___/\__/   \__, /\__,_/_/ /_/ /_/\___/
#                                   /____/
#Import librarys
import pygame, math, random
from pygame_functions import *
pygame.init()
pygame.mixer.init()

#                     _       __    __
#   _   ______ ______(_)___ _/ /_  / /__  _____
#  | | / / __ `/ ___/ / __ `/ __ \/ / _ \/ ___/
#  | |/ / /_/ / /  / / /_/ / /_/ / /  __(__  )
#  |___/\__,_/_/  /_/\__,_/_.___/_/\___/____/
#
xPos = 500
yPos = 375
##### pygame cannot find file for some fucked up reason#####
#rocket = makeSprite("images\\rocket.png")
#center = rocket.get_rect.center() # returns center piont of the rocket
xSpeed = 0
ySpeed = 0
angle = 0
deg = 5
rotSpeed = 250
xVel = math.cos(angle)-xPos
yVel = math.sin(angle)-yPos
slope = yVel / xVel
run = True
R2D = (math.pi * 2) / 360 #converts radians to degrees
#vecDirection = list([[math.cos(R2D * degrees), math.sin(R2D * degrees)] for degrees in xRange(360)]) #finds the coordinates for all the degrees


##window setup##
width = 400
height = 400
fps= 50 #game speed

# define colors in rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

surface = pygame.display.set_mode((width, height))
surfaceArea = pygame.display.get_surface()
surface.blit(surface)
pygame.display.set_caption("Rocket Game")
CLOCK = pygame.time.Clock()
surface.fill(BLACK)
#image = loadImage("stars.png")
#setBackgroundImage(image)
showSprite(rocket)
all_sprites = pygame.sprite.Group()

#                                                     _
#     ____ _____ _____ ___  ___     ___  ____  ____ _(_)___  ___
#    / __ `/ __ `/ __ `__ \/ _ \   / _ \/ __ \/ __ `/ / __ \/ _ \
#   / /_/ / /_/ / / / / / /  __/  /  __/ / / / /_/ / / / / /  __/
#   \__, /\__,_/_/ /_/ /_/\___/   \___/_/ /_/\__, /_/_/ /_/\___/
#  /____/                                   /____/

while run:
    CLOCK.tick(fps)
    #                          __     __                    ____     _
    #    ___ _   _____  ____  / /_   / /_  ____ _____  ____/ / /__  (_)___  ____ _
    #   / _ \ | / / _ \/ __ \/ __/  / __ \/ __ `/ __ \/ __  / / _ \/ / __ \/ __ `/
    #  /  __/ |/ /  __/ / / / /_   / / / / /_/ / / / / /_/ / /  __/ / / / / /_/ /
    #  \___/|___/\___/_/ /_/\__/  /_/ /_/\__,_/_/ /_/\__,_/_/\___/_/_/ /_/\__, /
    #                                                                    /____/

    #allows for quiting the game and closing the window by clicking the 'X' button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        angle += deg
        transformSprite(rocket, angle, 1)
        xSpeed -= xVel
        ySpeed += yVel
    if keys[pygame.K_RIGHT]:
        angle -= deg
        transformSprite(rocket, angle, 1)
        xSpeed += xVel
        ySpeed += yVel
    if keys[pygame.K_UP]:
        if angle < 0:
            angle += deg
        elif angle > 0:
            angle -= deg
        transformSprite(rocket, angle, 1)
        xSpeed
        ySpeed
    if keys[pygame.K_DOWN]:
        if angle < 0:
            angle -= 5
        transformSprite(rocket, angle, 1)
        xSpeed
        ySpeed
    #Combinations#
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
   # tick(30)

    pygame.display.update()

## WHEN 'ESC' IS PRESSED, GAME WINDOW CLOSES ##

endWait() #defined in "pygame_functions"
