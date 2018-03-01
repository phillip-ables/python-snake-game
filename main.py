  # https://pythonspot.com/snake-with-pygame/
from pygame.locals import *
import pygame
import time
'''
A player object can be created and 
variables can be modified using the movement methods.
We link those methods to the events. 
In Pygame we can get non-blocking keyboard input using this code:
'''
pygame.init()
pygame.event.pump()
keys = pygame.key.get_pressed()
'''
Define a class Player
holds the players position and the speed 
define the actions a Player instance can do (movements):
'''
class Player:
    x = 0  # position
    y = 0
    speed = 32  # speed
    direction = 0

    def update(self):
        if self.direction == 0:
            self.x = self.x + self.speed
        if self.direction == 1:
            self.x = self.x - self.speed
        if self.direction == 2:
            self.y = self.y - self.speed
        if self.direction == 3:
            self.y = self.y + self.speed

    def moveRight(self):
        self.direction = 0
    def moveLeft(self):
        self.direction = 1
    def moveUp(self):
        self.direction = 2
    def moveDown(self):
        self.direction = 3

class App:
    windowWidth = 800  # to play one must have a field
    windowHeight = 600
    player = 0

    def __init__(self):  # set the values of variables etc. - just after memory is allocated for it.
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = Player()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)  # set h and w and hardwarHW runs overspeed if fullyscreen or something
        
        pygame.display.set_caption('Pygame snake example')        
        self._running = True
        self._image_surf = pygame.image.load("pygame.jpg").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.moveRight()
            if(keys[K_LEFT]):
                self.player.moveLeft()
            if(keys[K_UP]):
                self.player.moveUp()
            if(keys[K_DOWN]):
                self.player.moveDown()

            if(keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_clenaup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
    time.sleep (100.0 / 1000.0)
