  # https://pythonspot.com/snake-with-pygame/
'''
Define a class Player
holds the players position and the speed 
define the actions a Player instance can do (movements):
'''
class Player:
    x = 10
    y = 10
    speed = 1

    def moveRight(self):
        self.x = self.x + self.speed
    def moveLeft(self):
        self.x = self.x - self.speed
    def moveUp(self):
        self.y = self.y - self.speed
    def moveDown(self):
        self.y = self.y + self.speed

