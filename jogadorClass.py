from PPlay.sprite import *
from PPlay.animation import *

class Jogador:
    def __init__(self,pos):
        self.x = pos[0]
        self.y = pos[1]

        self.image = Sprite('assets/gato_animacao-Sheet.png',20)

        self.image.set_sequence_time(0,20,50,True)
        self.image.set_sequence(0,0,True)

        self.image.set_position(self.x-self.image.width/2,self.y-self.image.height/2)

        self.width = self.image.width
        self.height = self.image.height

    def collided(self,col):
        return self.image.collided(col)
    
    def set_position(self,x,y):
        self.x = x
        self.y = y
        self.image.set_position(self.x,self.y)

    def draw(self):
        self.image.draw()

    def move_x(self,speed):
        self.x += speed
        self.image.set_position(self.x, self.y)

    def move_y(self,speed):
        self.y += speed
        self.image.set_position(self.x, self.y)

    def update(self):
        #print(str(self.image.get_initial_frame()) + ' ' + str(self.image.get_final_frame()) + ' ' + str(self.image.get_curr_frame()))
        self.image.update()
        
    def setAnim(self, state):
        if(state==1):
            if self.image.get_curr_frame() < 2 or self.image.get_curr_frame() > 9:
                self.image.set_sequence(2, 9, True)

        if(state==2):
            if self.image.get_curr_frame() < 11 or self.image.get_curr_frame() > 18:
                self.image.set_sequence(11, 18, True)

        if(state==3):
            if not self.image.get_curr_frame() == 18:
                self.image.set_sequence(18, 18, True)
                self.image.set_curr_frame(18)
        if(state==4):
            if not self.image.get_curr_frame() == 19:
                self.image.set_sequence(19, 19, True)
                self.image.set_curr_frame(19)