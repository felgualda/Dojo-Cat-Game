from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.keyboard import *
import menu

def control() -> int:
    w,h = 1200,675
    janela = Window(w,h)
    janela.set_title('Controles')
    fundo = GameImage('assets/f.png')
    fundo.set_position(0,0)
    key = Keyboard()
    cursor = Mouse()
    wasd = GameImage('assets/wasd.png')
    espaco = GameImage('assets/espaco.png')
    botaomouse1 = GameImage('assets/botaomouse1.png')
    wasd.set_position(100,300)
    espaco.set_position(100,400)
    botaomouse1.set_position(200 - botaomouse1.width/2 ,500)

    while True:
        if key.key_pressed('esc'):
            menu.MenuPrincipal()
        fundo.draw()

        janela.draw_text('W move o personagem para cima', 350 , 280 , 20 , (251,116,2) , 'chapaza')
        janela.draw_text('A move o personagem para a esquerda' , 350 , 300 , 20 , (251,116,2) , 'chapaza')
        janela.draw_text('S move o personagem para baixo', 350 , 320 , 20 , (251,116,2) , 'chapaza')
        janela.draw_text('D move o personagem para a direita' , 350 , 340 , 20 , (251,116,2) , 'chapaza')
        janela.draw_text('Usar investida' , 350 , 420 , 20 , (251,116,2) , 'chapaza')
        janela.draw_text('Atacar' , 350 , 520 , 20 , (251,116,2) , 'chapaza')
        wasd.draw()
        espaco.draw()
        botaomouse1.draw()
        janela.update()