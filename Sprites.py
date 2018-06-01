
#                      __        __                              
#     _________  _____/ /_____  / /_   ____ _____ _____ ___  ___ 
#    / ___/ __ \/ ___/ //_/ _ \/ __/  / __ `/ __ `/ __ `__ \/ _ \
#   / /  / /_/ / /__/ ,< /  __/ /_   / /_/ / /_/ / / / / / /  __/
#  /_/   \____/\___/_/|_|\___/\__/   \__, /\__,_/_/ /_/ /_/\___/ 
#                                   /____/                       
 

#Import librarys
import pygame, math
from pygame_functions import *
pygame.init()


##game setup##
horSize = 1000
vertSize = 750
screen = pygame.display.set_mode((horSize, vertSize))
#screenSize(horSize, vertSize)


rocket = makeSprite("rocket1.png")
pygame.display.set_caption("Rocket Game")

setBackgroundImage("stars.png")

showSprite(rocket)


#                     _       __    __         
#   _   ______ ______(_)___ _/ /_  / /__  _____
#  | | / / __ `/ ___/ / __ `/ __ \/ / _ \/ ___/
#  | |/ / /_/ / /  / / /_/ / /_/ / /  __(__  ) 
#  |___/\__,_/_/  /_/\__,_/_.___/_/\___/____/  
#                                              
xPos = 500
yPos = 375
spriteDimentions = rocket.get_rect() # returns the width, hieght, and center piont of the rocket
xSpeed = 0
ySpeed = 0
vel = 2
fps= 20
CLOCK = pygame.time.Clock()
run = True
D2R = (math.pi * 2) / 360 #converts radians to degrees
vecDirection = list([[math.cos(D2R * degrees), math.sin(D2R * degrees)] for degrees in xRange(360)]) #finds the coordinates for all the degrees





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
    tick(30)

#    pygame.display.update()

## WHEN 'ESC' IS PRESSED, GAME WINDOW CLOSES ##

endWait() #defined in "pygame_functions"
