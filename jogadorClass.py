from PPlay.sprite import *
from PPlay.animation import *

class Jogador:
    def __init__(self,pos):
        self.x = pos[0]
        self.y = pos[1]

        self.image = Sprite('assets/gato_animacao-Sheet.png',26)

        self.image.set_sequence_time(0,20,60,True)
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
            #print('estado 1')
            if self.image.get_curr_frame() < 1 or self.image.get_curr_frame() > 8:
                self.image.set_sequence(1, 8, True)

        if(state==2):
            #print('estado 2')
            if self.image.get_curr_frame() < 9 or self.image.get_curr_frame() > 16:
                self.image.set_sequence(9, 16, True)

        if(state==3):
            #print('estado 3')
            if not self.image.get_curr_frame() == 16:
                self.image.set_sequence(16, 16, True)
                self.image.set_curr_frame(16)
        if(state==4):
            #print('estado 4')
            if not self.image.get_curr_frame() == 17:
                self.image.set_sequence(17, 17, True)
                self.image.set_curr_frame(17)

        if(state==5):
            self.image.set_sequence(18, 26, True)

        if(state==6):
            self.image.set_sequence(23, 26, True)