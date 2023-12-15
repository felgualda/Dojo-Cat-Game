from PPlay.sprite import *

class Vida():
    def __init__(self):
        self.vida_max = 5
        self.vida_atual = self.vida_max

        self.pos_barravida = (15,675 - 50)
        self.offset_barravida = 5

        self.invencivel = False
        self.levouDano = False
        self.tempoInvencivel = 1

        self.vetCoracoes = [Sprite('assets/hearts.png',2) for x in range(self.vida_max)]
        self.tam_coracao_x = self.vetCoracoes[0].width

        for i in range(len(self.vetCoracoes)):
            self.vetCoracoes[i].set_position(self.pos_barravida[0] + i * self.tam_coracao_x + self.offset_barravida *i, self.pos_barravida[1])

    def drawCoracoes(self):
        for i in range(len(self.vetCoracoes)):
            self.vetCoracoes[i].draw()

    def levarDano(self,soundmanager):
        if(not self.invencivel):
            soundmanager.som8()
            self.vida_atual -= 1
            self.atualizarCoracoes()
            self.levouDano = True

    def ganharVida(self):
        self.vida_atual += 1
        self.atualizarCoracoes()


    def atualizarCoracoes(self):
        for i in range(self.vida_max):
            if i < self.vida_atual:
                self.vetCoracoes[i].set_curr_frame(0)
            else:
                self.vetCoracoes[i].set_curr_frame(1)