from PPlay.sprite import *
from particleHandler import *

class Spike():
    def __init__(self,pos_x,pos_y):
        self.tag='spike'
        self.image = Sprite('assets/spike.png')

        self.x = pos_x
        self.y = pos_y
        self.image.set_position(self.x,self.y)

    def move_x(self,speed):
        self.x += speed
        self.image.set_position(self.x, self.y)

    def move_y(self,speed):
        self.y += speed
        self.image.set_position(self.x, self.y)
       
    def Draw(self):
        self.image.draw()