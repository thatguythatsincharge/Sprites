# template for main
import pygame as pg
import random, math, sys
from settings_template import *
#from sprites import *
from pygame_functions import *

class Game:
    def __init__(self): #stuff that needs to happen on game startup
        # initialize pygame and create window
        pg.init()
        pg.mixer.init()
        self.screen = screenSize(width, height)#pygame.display.set_mode((width, height)) #display surface the reps the screen
        def caption(caption): # creates a function called "caption()" that takes a string perameter
            pg.display.set_caption(caption)
        caption("Astroides")
        #setBackgroundImage("stars.png")
        self.clock = pg.time.Clock()
        #showSprite(rocket)
        self.running = True

    def new(self): # start new game
        self.all_sprites = pg.sprite.Group()
        #self.player = Player()
        #self.all_sprites.add(self.player)
        self.run()

    def run(self): #gameloop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS) # keep the loop running at the same speed by managing time
            self.events()
            self.update()
            self.draw()

    def events(self): #gameloop - events
        # Process input (events)
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                turnLeft()
                printStatus()

            elif keys[pygame.K_RIGHT]:
                turnRight()
                printStatus()

            elif keys[pygame.K_UP]:
                speedUp()
                printStatus()

            elif keys[pygame.K_DOWN]:
                slowDown()
                printStatus()

        ## HANDLES LOOPING ##
            # xPos = global.xPos
            # yPos = global.yPos
            # xSpeed = global.xSpeed
            # ySpeed = global.ySpeed
            # vertSize = global.height
            # horSize = global.width
            xPos += xSpeed                      ## Changes the X-position of the rocket sprite providing the
            if xPos > vertSize + 210:             # illusion of horizontal movementself.
                xPos = -100
            elif xPos < -100:
                xPos = vertSize + 210

            yPos += ySpeed                      ## Changes the Y-position of the rocket sprite providing the
            if yPos > horSize - 300:            #  illusion of vertical movement.
                yPos = -100
            elif yPos < -100:
                yPos = horSize -300

            moveSprite(rocket, xPos, yPos)      # Moves the position of the rocket

            tick(30)                            # Creates open time to allow ESC key to be presses

    def update(self): #gameloop - update
        # Update
        #moveSprite(rocket, xPos, yPos)
        self.all_sprites.update()
        pygame.display.update()

    def draw(self): #gameloop - draw
            # Draw / render
            #self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            # always do this last. after drawing everything, flip the display
            pg.display.flip() # pygame shows what it was drawing in the background.(update display)

    def show_start_screen(self):
        pass

    def show_gameover_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_gameover_screen()

pg.quit()
sys.exit()
