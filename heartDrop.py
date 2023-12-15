from PPlay.sprite import *

class Coracao():
    def __init__(self,pos_x,pos_y):
        self.x = pos_x
        self.y = pos_y

        self.tag='coracao'

        self.image = Sprite('assets/hearts.png',2)
        self.image.set_position(self.x,self.y)

        self.podeColetar = False
        self.existe = True

        self.espera = 0.8
        self.timer = 0

    def move_x(self,speed):
        self.x += speed
        self.image.set_position(self.x, self.y)

    def move_y(self,speed):
        self.y += speed
        self.image.set_position(self.x, self.y)

    def Coletar(self,soundmanager,vida):
        if(self.existe and self.podeColetar):
            soundmanager.som10()
            vida.ganharVida()
            self.existe=False

    def Draw(self,janela):
        if(self.existe):
            self.timer+=janela.delta_time()
            if(self.timer >= self.espera):
                self.podeColetar = True

            self.image.draw()
