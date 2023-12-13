from PPlay.sprite import *
from PPlay.window import *
from particleHandler import *
import math

class Inimigo:
    def __init__(self,pos,var):
        # Sprites e posições
        self.x = pos[0]
        self.y = pos[1]

        self.tag = 'enemy'

        self.vivo = True
        
        self.var = var
        self.image = Sprite('assets/inimigos/ninja.png')
        
        self.hitbox = Sprite('assets\inimigos\enemy-hitbox.png')
        self.hitbox.set_position(self.x+42,self.y-18)


        # Definição de sprite conforme a variação
        if(var == 1):
            self.image = Sprite('assets/inimigos/ninja-Sheet-export.png',24)
            self.image.set_sequence_time(0,25,120)

        self.image.set_position(self.x,self.y)

        self.centro_x = self.x + self.image.width/2
        self.centro_y = self.y + self.image.height/2

        # Variáveis do inimigo e IA
        self.vida = 100

        self.vel_inimigo_max = 100
        self.state = 0

        self.velx = 0
        self.vely = 0

        self.levouDano = False
        self.tempoSpriteDano = 0.25
        self.tempoSpriteTimer = 0

    def move_x(self,speed):
        self.x += speed
        self.image.set_position(self.x, self.y)

    def move_y(self,speed):
        self.y += speed
        self.image.set_position(self.x, self.y)

    def Draw(self):
        self.image.draw()
        self.hitbox.draw()

    def LevarDano(self,dano):
        FX_blood(self.centro_x,self.centro_y)
        self.vida -= dano
        self.levouDano = True

        if(self.vida <= 0):
            self.Morrer()

    def Morrer(self):
        self.vivo = False

    def Stalk(self, target, janela):
        # Vetor normalizado entre inimigo e alvo
        #target.
        norma = math.sqrt(((target.x +target.width/2) - self.centro_x)**2 + ((target.y +target.height/2) - self.centro_y)**2)
        vet_x = ((target.x +target.width/2)- self.centro_x)/norma
        vet_y = ((target.y+target.height/2)- self.centro_y)/norma

        self.velx = vet_x * self.vel_inimigo_max * janela.delta_time()
        self.vely = vet_y * self.vel_inimigo_max * janela.delta_time()

        if(not self.levouDano):
            self.move_x(self.velx)
            self.move_y(self.vely)
        
    def Attack(self,target):
        if(self.velx > 0):
            if self.image.get_curr_frame() < 16 or self.image.get_curr_frame() > 19:
                self.image.set_sequence(16,19,True)
        if(self.velx < 0):
            if self.image.get_curr_frame() < 19 or self.image.get_curr_frame() > 22:
                self.image.set_sequence(19,22,True)
        
        if(self.image.get_curr_frame()==17 or self.image.get_curr_frame()==20):
            #Frame de ataque
            if(self.hitbox.collided(target.colisao)):
                if(target.tag=='player'):
                    pass

        if(self.image.get_curr_frame()==18 or self.image.get_curr_frame()==21):
            self.state=0


    def Update(self,jogador,janela):
        if(self.vivo):
            if(self.levouDano):
                self.tempoSpriteTimer += janela.delta_time()
                if(self.velx > 0):
                    self.image.set_curr_frame(22)
                if(self.velx < 0):
                    self.image.set_curr_frame(23)
            if(self.tempoSpriteTimer >= self.tempoSpriteDano):
                self.levouDano = False
                self.tempoSpriteTimer = 0

            if(self.velx > 0 and not self.levouDano and self.state==0):
                self.hitbox.set_position(self.x+42,self.y+18)
                if self.image.get_curr_frame() < 1 or self.image.get_curr_frame() > 7:
                    self.image.set_sequence(1,7,True)
            if(self.velx < 0 and not self.levouDano and self.state==0):
                self.hitbox.set_position(self.x-6,self.y+18)
                if self.image.get_curr_frame() < 8 or self.image.get_curr_frame() > 14:
                    self.image.set_sequence(8,14,True)

            if(not self.levouDano):
                self.image.update()

            self.centro_x = self.x + self.image.width/2
            self.centro_y = self.y + self.image.height/2

            if(self.state==0):
                self.Stalk(jogador,janela)

            if(self.state==1):
                self.Attack(jogador)

            if(self.hitbox.collided(jogador.colisao)):
                self.state = 1

