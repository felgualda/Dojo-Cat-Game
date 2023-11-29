from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.collision import *
from PPlay.keyboard import *
from PPlay.mouse import *
from globalVar import *
from sala import *
from pygame import *
import game
import mapgenerator

janela.set_background_color((22,22,22))


print(mapa)
mapgenerator.SetSalas(mapa)

game.Jogar()
