from globalVar import *
from PPlay.sprite import *

barraInvestida = Sprite('assets/dash-bar.png',36)

barraInvestida.set_sequence(0,36,False)
barraInvestida.set_total_duration(cooldownInvestida*1000)
barraInvestida.set_position(pos_barrainvestida[0],pos_barrainvestida[1])

def drawBarra():
    barraInvestida.update()
    barraInvestida.draw()