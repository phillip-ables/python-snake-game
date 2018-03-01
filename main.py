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
  # pygame.init()
  # pygame.event.pump()
  # keys = pygame.key.get_pressed()
'''
Define a class Player
holds the players position and the speed 
define the actions a Player instance can do (movements):
'''
class Apple:
    x = 0
    y = 0
    step = 44

    def __init__(self, x, y):
        self.x = x * self.step
        self.y = y * self.step

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))

class Player:
    x = []  # position
    y = []
    step = 44  # speed
    direction = 0
    length = 3;

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):  # is this where the player(10) is used
        self.length = length
        for i in range(0, length):
            self.x.append(0)  # what the hell am i appending here
            self.y.append(0)

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
                # update previous position
            for i in range(self.length-1, 0, -1):
                print("self.x["+str(i)+"] = self.x["+str(i-1)+"]")
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

                # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    def moveRight(self):
        self.direction = 0
    def moveLeft(self):
        self.direction = 1
    def moveUp(self):
        self.direction = 2
    def moveDown(self):
        self.direction = 3

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))

class App:
    windowWidth = 800  # to play one must have a field
    windowHeight = 600
    player = 0
    apple = 0

    def __init__(self):  # set the values of variables etc. - just after memory is allocated for it.
        self._running = True
        self._display_surf = None  # why does it need to instantiate these variables on init
        self._image_surf = None
        self._apple_surf = None
        self.player = Player(10)
        self.apple = Apple(5, 5)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)  # set h and w and hardwarHW runs overspeed if fullyscreen or something
        
        pygame.display.set_caption('Pygame Sanke')        
        self._running = True
        self._image_surf = pygame.image.load("pygame.jpg").convert()
        self._apple_surf = pygame.image.load("pillow.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.player.update()
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))  # what am i filling
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
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

            time.sleep (50.0 / 1000.0);
        self.on_clenaup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()