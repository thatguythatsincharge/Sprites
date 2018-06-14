import math
import pygame
from pygame_functions import *

# define colors in rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# set up a window for pygame to use
width = 1080
height = 1080
hWidth = width/2
hHeight = height/2
screen = pygame.display.set_mode((width, height))

rocket = makeSprite("images/rocket1.png")
#center = rocket.get_rect.center() # returns center piont of the rocket
xPos = hWidth
yPos = hHeight
xSpeed = 0
ySpeed = 0
vertSize = height
horSize = width
vel = 0
FPS = 60 # how fast the game runs (frames per second)
angle = 0
rAngle = math.radians(angle)
changeAngle = 0
# deg = 5
# rotSpeed = 250
# xVel = math.cos(angle)-xPos
# yVel = math.sin(angle)-yPos
# slope = yVel / xVel
# run = True
# R2D = (math.pi * 2) / 360 #converts radians to degrees
# #vecDirection = list([[math.cos(R2D * degrees), math.sin(R2D * degrees)] for degrees in xRange(360)])
# #finds the coordinates for all the degrees
# screen = pygame.display.set_mode((width, height))
# screenArea = pygame.display.get_surface()

# functions
def turnLeft():
    """Rotates the rocket clockwise"""
    global angle, changeAngle, rAngle, xSpeed, ySpeed, vel
    changeAngle -= 15
    angle += changeAngle
    changeAngle = 0
    if angle >= 360:
        angle -= 360
    elif angle < 0:
        angle += 360
    rAngle = math.radians(angle)
    vel = math.sin(rAngle)/math.cos(rAngle)
    xSpeed = math.sin(rAngle * (-vel))
    ySpeed = math.cos(rAngle * vel)
    transformSprite(rocket, angle, 1)
    return()

def turnRight():
    """Rotates the rocket clockwise"""
    global angle, changeAngle, rAngle, xSpeed, ySpeed, vel
    changeAngle += 15
    angle += changeAngle
    changeAngle = 0
    if angle >= 360:
        angle -= 360
    elif angle < 0:
        angle += 360
    rAngle = math.radians(angle)
    vel = math.sin(rAngle)/math.cos(rAngle)
    xSpeed = math.sin(rAngle)*(-vel)
    ySpeed = math.cos(rAngle)*(vel)
    transformSprite(rocket, angle, 1)
    return()

def speedUp():
    """Accelerates rocket in its current direction"""
    global xSpeed, ySpeed, vel, rAngle
    vel -= 1
    #rAngle = math.radians(angle)
    xSpeed = math.sin(rAngle)*(-vel)
    ySpeed = math.cos(rAngle)*(vel)
    return ()

def slowDown():
    """Decelerates rocket in direction 180 degrees to its current direction"""
    global xSpeed, ySpeed, vel, rAngle
    vel += 1
    #rAngle = math.radians(angle)
    xSpeed = math.sin(rAngle)*(-vel)
    ySpeed = math.cos(rAngle)*(vel)
    return()
# for diagnostics
def printStatus():
    """Displays direction and velocity statistics on the shell"""
    print("vel: " + str(vel))
    print("Angle: " + str(angle))
    print("rAngle: " + str(rAngle))
    print("xSpeed: " + str(xSpeed))
    print("ySpeed: " + str(ySpeed))
