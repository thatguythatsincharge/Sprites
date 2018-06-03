import math
import pygame
from pygame_functions import *
# set up a window for pygame to use
WIDTH = 720
HEIGHT = 480
FPS = 30 # how fast the game runs (frames per second)

# define colors in rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


##### pygame cannot find this stupid file for some fucked up reason#####
rocket = pygame.image.load("rocket1.png")

#center = rocket.get_rect.center() # returns center piont of the rocket
###################
xPos = 500
yPos = 375
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
#vecDirection = list([[math.cos(R2D * degrees), math.sin(R2D * degrees)] for degrees in xRange(360)])
#finds the coordinates for all the degrees
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screenArea = pygame.display.get_surface()
