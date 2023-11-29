from PPlay.sprite import *

class Inimigo:
    def __init__(self,pos,var):
        # Sprites e posições
        self.x = pos[0]
        self.y = pos[1]
        self.var = var
        self.image = Sprite()
        self.image.set_position(self.x,self.y)

        # Definição de sprite conforme a variação
        if(var == 1):
            self.image = Sprite('assets/inimigos/ninja.png')

        # Variáveis do inimigo e IA
        self.vida = 100

        self.velocidade = 200
        self.state = 0

    def Draw(self):
        self.image.draw()

    def Stalk(self, target):
        # Vetor normalizado entre inimigo e alvo
        #target.
        pass

    def Update(self):
        if(self.state==0):
            pass
