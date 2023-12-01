from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.keyboard import *

def Opcoes() -> int:
    w,h = 1200,675
    janela = Window(w,h)
    fundo = GameImage('assets/f.png')
    fundo.set_position(0,0)
    key = Keyboard()
    while True:
        if key.key_pressed('esc'):
            break
        fundo.draw()
        janela.update()