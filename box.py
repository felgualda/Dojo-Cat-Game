from PPlay.sprite import *
from particleHandler import *
import soundmanager

class Box():
    def __init__(self,pos_x,pos_y):
        self.tag='crate'

        self.x = pos_x
        self.y = pos_y

        self.image = Sprite('assets/box.png')
        self.image.set_position(self.x,self.y)

        self.broken = False

    def move_x(self,speed):
        self.x += speed
        self.image.set_position(self.x, self.y)

    def move_y(self,speed):
        self.y += speed
        self.image.set_position(self.x, self.y)

    def Break(self,soundManager):
        if(not self.broken):
            FX_crate(self.x+self.image.width/2,self.y+self.image.height/2)
            soundManager.som6()
        self.broken = True
       
    def Draw(self):
        if(not self.broken):
            self.image.draw()