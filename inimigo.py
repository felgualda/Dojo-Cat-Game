from PPlay.sprite import *
from PPlay.window import *
import math

class Inimigo:
    def __init__(self,pos,var):
        # Sprites e posições
        self.x = pos[0]
        self.y = pos[1]
        
        self.var = var
        self.image = Sprite('assets/inimigos/ninja.png')

        # Definição de sprite conforme a variação
        if(var == 1):
            self.image = Sprite('assets/inimigos/ninja.png')

        self.image.set_position(self.x,self.y)

        self.centro_x = self.x + self.image.width/2
        self.centro_y = self.y + self.image.height/2

        # Variáveis do inimigo e IA
        self.vida = 100

        self.vel_inimigo_max = 100
        self.state = 0

    def move_x(self,speed):
        self.x += speed
        self.image.set_position(self.x, self.y)

    def move_y(self,speed):
        self.y += speed
        self.image.set_position(self.x, self.y)

    def Draw(self):
        self.image.draw()

    def Stalk(self, target, janela):
        # Vetor normalizado entre inimigo e alvo
        #target.
        norma = math.sqrt((target.x - self.centro_x)**2 + (target.y - self.centro_y)**2)
        vet_x = (target.x - self.centro_x)/norma
        vet_y = (target.y - self.centro_y)/norma

        velx = vet_x * self.vel_inimigo_max * janela.delta_time()
        vely = vet_y * self.vel_inimigo_max * janela.delta_time()

        self.move_x(velx)
        self.move_y(vely)


    def Update(self,jogador,janela):
        self.centro_x = self.x + self.image.width/2
        self.centro_y = self.y + self.image.height/2

        if(self.state==0):
            self.Stalk(jogador,janela)

