from globalVar import *
from PPlay.sprite import *

vetCoracoes = [Sprite('assets/hearts.png',2) for x in range(vida_max)]
tam_coracao_x = vetCoracoes[0].width

for i in range(len(vetCoracoes)):
    vetCoracoes[i].set_position(pos_barravida[0] + i * tam_coracao_x + offset_barravida *i, pos_barravida[1])

def drawCoracoes():
    for i in range(len(vetCoracoes)):
        vetCoracoes[i].draw()

def levarDano():
    pass