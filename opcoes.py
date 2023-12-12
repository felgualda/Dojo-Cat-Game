from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.keyboard import *
from ctrls import *

def Opcoes() -> int:
    w,h = 1200,675
    janela = Window(w,h)
    fundo = GameImage('assets/f.png')
    fundo.set_position(0,0)
    key = Keyboard()
    cursor = Mouse()
    controle = GameImage('assets/botaocontrole.png')
    controle.set_position(janela.width/2 - controle.width/2, janela.height/2 - controle.height/2 - 10)
    timer = 0
    while True:
        timer += janela.delta_time()
        if cursor.is_over_area((controle.x , controle.y),(controle.x + controle.width , controle.y + controle.height)):
            controle = GameImage('assets/botaocontrole2.png')
            controle.set_position(janela.width/2 - controle.width/2, janela.height/2 - controle.height/2 - 10 )
        else:
            controle = GameImage('assets/botaocontrole.png')
            controle.set_position(janela.width/2 - controle.width/2, janela.height/2 - controle.height/2 - 10 )
        if cursor.is_over_area((controle.x , controle.y),(controle.x + controle.width , controle.y + controle.height)) and cursor.is_button_pressed(1) and timer > 0.5:
            x = control()
            print(x)






        if key.key_pressed('esc'):
            break
        fundo.draw()
        controle.draw()
        janela.update()