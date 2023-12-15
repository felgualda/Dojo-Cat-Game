from PPlay.sprite import *

class Projectile():
    def __init__(self,pos_x,pos_y,vector):
        self.image = Sprite('assets/inimigos/arrow.png',4)
        self.image.set_sequence_time(0,3,30,True)

        self.x = pos_x
        self.y = pos_y

        self.speed = 900

        self.vector = vector

        self.existe = True

    def move_x(self,speed):
        self.x += speed
        self.image.set_position(self.x,self.y)

    def move_y(self,speed):
        self.y += speed
        self.image.set_position(self.x,self.y)

    def Draw(self):
        self.image.draw()

    def Hit(self, jogador,soundmanager):
        jogador.LevarDano(soundmanager)
        self.existe = False

    def Update(self, janela, jogador,soundmanager):
        if(jogador.collided(self.image)):
            self.Hit(jogador,soundmanager)

        if(self.existe):
            self.move_x(self.speed * janela.delta_time() * self.vector[0])
            self.move_y(self.speed * janela.delta_time() * self.vector[1])

        if(self.existe):
            self.image.update()
