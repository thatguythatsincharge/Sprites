# template for main
import pygame as pg
import random, math
from settings_template import *
#from sprites import *
from pygame_functions import *

class Game:
    def __init__(self): #stuff that needs to happen on game startup
        # initialize pygame and create window
        pg.init()
        pg.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) #display surface the reps the screen
        def caption(caption): # creates a function called "caption()" that takes a string perameter
            pg.display.set_caption(caption)
        caption("Astroides")
        #setBackgroundImage("stars.png")
        self.clock = pg.time.Clock()
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


    def update(self): #gameloop - update
        # Update
        #moveSprite(rocket, xPos, yPos)
        self.all_sprites.update()
        pygame.display.update()


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
            #xPos += xSpeed
            #if xPos > vertSize + 210:
            #    xPos = -100
            #elif xPos < -100:
            #    xPos = vertSize + 210

           #yPos += ySpeed
            #if yPos > horSize - 300:
                yPos = -100
            #elif yPos < -100:
            #    yPos = horSize -300


    def draw(self): #gameloop - draw
            # Draw / render
            self.screen.fill(BLACK)
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
