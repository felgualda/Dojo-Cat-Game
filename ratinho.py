from PPlay.sprite import *
import random
import math

class Ratinho():
    def __init__(self, pos_x, pos_y):
        self.tag='ratinho'

        self.x = pos_x
        self.y = pos_y

        self.vel = 110

        self.image = Sprite('assets/ratinho.png', 9)
        self.image.set_sequence_time(0,8,60,True)

        self.tempoMudarDir = 3.5
        self.mudarDirTimer = 0
        self.started = False

        self.dirX = 0
        self.dirY = 1

    def move_x(self, speed):
        self.x += speed
        self.image.set_position(self.x, self.y)

    def move_y(self, speed):
        self.y += speed
        self.image.set_position(self.x, self.y)

    def Draw(self):
        self.image.draw()

    def Update(self, janela):
        self.mudarDirTimer += janela.delta_time()
        if not self.started:
            self.image.set_sequence(0, 0,True)

        if (self.x < 138 or self.x > 1062) and self.started:
            self.dirX = -self.dirX

        if (self.y < 144 or self.y > 585) and self.started:
            self.dirY = -self.dirY

        if self.mudarDirTimer >= self.tempoMudarDir:
            if not self.started:
                self.started = True

            # Gera valores aleatórios para as componentes x e y do vetor
            self.dirX = random.uniform(-1, 1)
            self.dirY = random.uniform(-1, 1)

            # Normaliza o vetor para torná-lo unitário
            magnitude = math.sqrt(self.dirX**2 + self.dirY**2)
            if magnitude != 0:
                self.dirX /= magnitude
                self.dirY /= magnitude

            self.mudarDirTimer = 0

        if self.dirX > 0:
            if not (1 < self.image.get_curr_frame() < 4):
                self.image.set_sequence(1, 4, True)
        elif self.dirX < 0:
            if not (5 < self.image.get_curr_frame() < 8):
                self.image.set_sequence(5, 8, True)

        self.move_x(self.vel * janela.delta_time() * self.dirX)
        self.move_y(self.vel * janela.delta_time() * self.dirY)

        self.image.update()