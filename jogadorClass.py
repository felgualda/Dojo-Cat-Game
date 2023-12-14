from PPlay.sprite import *
from PPlay.animation import *
from vida import *
from pygame import mixer

class Jogador:
    def __init__(self,pos):
        self.x = pos[0]
        self.y = pos[1]

        self.tag = 'player'
        self.vida = Vida()
        
        self.image = Sprite('assets/gato_animacao-Sheet.png',36)

        self.colisao = Sprite('assets/colisao_player.png')

        self.hitbox = Sprite('assets/hitbox_player.png')

        self.image.set_sequence_time(0,36,60,True)
        self.image.set_sequence(0,0,True)

        self.image.set_position(self.x-self.image.width/2,self.y-self.image.height/2)

        self.enemiesInRange = []
        self.interactablesInRange = []

        self.width = self.image.width
        self.height = self.image.height

        self.toggle = False# Toggle no draw quando jogador está invencivel
        self.invencivelTimer = 0
        self.invencivelTimerSec = 0

    def LevarDano(self):
        self.vida.levarDano()

    def collided(self,col):
        return self.colisao.collided(col)
    
    def CheckHitbox(self,other):
        if(other.tag=='enemy'):
            if(self.hitbox.collided(other.image) and not other in self.enemiesInRange):
                self.enemiesInRange.append(other)
            if(not self.hitbox.collided(other.image) and other in self.enemiesInRange):
                self.enemiesInRange.remove(other)
        if(other.tag=='boss'):
            if(self.hitbox.collided(other.bossImage) and not other in self.enemiesInRange):
                self.enemiesInRange.append(other)
            if(not self.hitbox.collided(other.bossImage) and other in self.enemiesInRange):
                self.enemiesInRange.remove(other)
        if(other.tag=='crate'):
            if(self.hitbox.collided(other.image) and not other in self.interactablesInRange):
                self.interactablesInRange.append(other)
            if(not self.hitbox.collided(other.image) and other in self.interactablesInRange):
                self.interactablesInRange.remove(other)

    def attack(self,soundmanager):
        if len(self.enemiesInRange) != 0:
            soundmanager.som1()
        if len(self.enemiesInRange) == 0 and len(self.interactablesInRange) == 0:
            soundmanager.som2()
        
        for e in self.enemiesInRange:
            e.LevarDano(100)
            if(not e.vivo):
                self.enemiesInRange.remove(e)

        for e in self.interactablesInRange:
            e.Break()
            if(e.broken):
                self.interactablesInRange.remove(e)
    
    def set_position(self,x,y):
        self.x = x
        self.y = y
        self.image.set_position(self.x,self.y)

    def draw(self):
        if(self.vida.levouDano):
            if(self.toggle):
                self.image.draw()
        else:
            self.image.draw()
        #self.colisao.draw()
        #self.hitbox.draw()

    def move_x(self,speed):
        self.x += speed
        self.image.set_position(self.x, self.y)

    def move_y(self,speed):
        self.y += speed
        self.image.set_position(self.x, self.y)

    def update(self, ultimaDir,janela):
        #print(str(self.image.get_initial_frame()) + ' ' + str(self.image.get_final_frame()) + ' ' + str(self.image.get_curr_frame()))
        self.image.update()
        self.colisao.set_position(self.x+27,self.y+3)

        if(ultimaDir=='right'):
            self.hitbox.set_position(self.x+57,self.y-18)
        if(ultimaDir=='left'):
            self.hitbox.set_position(self.x+60-self.hitbox.width,self.y-18)

        if(self.vida.levouDano):
            self.vida.invencivel = True
            self.invencivelTimer+=janela.delta_time()
            self.invencivelTimerSec+=janela.delta_time()
            if(self.invencivelTimerSec >= 0.1):
                self.toggle = not self.toggle
                self.invencivelTimerSec = 0
            if(self.invencivelTimer >= self.vida.tempoInvencivel):
                self.vida.levouDano = False
                self.vida.invencivel = False
                self.toggle = False
                self.invencivelTimer = 0
                self.invencivelTimerSec = 0
        

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
            if self.image.get_curr_frame() < 18 or self.image.get_curr_frame() > 26:
                self.image.set_sequence(18, 26, True)

        if(state==6):
            if self.image.get_curr_frame() < 27 or self.image.get_curr_frame() > 35:
                self.image.set_sequence(27, 35, True)