from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.sprite import *
from opcoes import *
from globalVar import *
import game

# DEFINIÇÃO DA JANELA:
fundo = GameImage('assets/f.png')
fundo.set_position(0,0)

jogar = GameImage('assets/botaojogar.png')
opcoes = GameImage('assets/botaoopcoes.png')
sair = GameImage('assets/botaosair.png')

jogar.set_position(janela.width/2 - jogar.width/2, janela.height/2 - jogar.height/2 - 10)
opcoes.set_position(janela.width/2 - opcoes.width/2, janela.height/2 - opcoes.height/2 + 60)
sair.set_position(janela.width/2 - sair.width/2, janela.height/2 + sair.height/2 + 80)

def MenuPrincipal():
    global w,h,janela,cursor,fundo,jogar,opcoes,sair
    cursor.unhide()

    janela.set_title('Dojo Cat | Menu Principal')

    while True:
    # Botão "jogar" escurecer quando o mouse estiver em cima dele:

        if cursor.is_over_area((jogar.x , jogar.y),(jogar.x + jogar.width , jogar.y + jogar.height)):
            jogar = GameImage('assets/botaojogar2.png')
            jogar.set_position(janela.width/2 - jogar.width/2, janela.height/2 - jogar.height/2 - 10 )
        else:
            jogar = GameImage('assets/botaojogar.png')
            jogar.set_position(janela.width/2 - jogar.width/2, janela.height/2 - jogar.height/2 - 10 )

    # Botão "opções" escurecer quando o mouse estiver em cima dele:

        if cursor.is_over_area((opcoes.x , opcoes.y),(opcoes.x + opcoes.width , opcoes.y + opcoes.height)):
            opcoes = GameImage('assets/botaoopcoes2.png')
            opcoes.set_position(janela.width/2 - opcoes.width/2, janela.height/2 - opcoes.height/2 + 60)
        else:
            opcoes = GameImage('assets/botaoopcoes.png')
            opcoes.set_position(janela.width/2 - opcoes.width/2, janela.height/2 - opcoes.height/2 + 60)

    # Botão "sair" escurecer quando o mouse estiver em cima dele:

        if cursor.is_over_area(( sair.x ,sair.y),(sair.x + sair.width, sair.y + sair.height )):
            sair = GameImage("assets/botaosair2.png")
            sair.set_position(janela.width/2 - sair.width/2, janela.height/2 + sair.height/2 + 80)
        else:
            sair = GameImage("assets/botaosair.png")
            sair.set_position(janela.width/2 - sair.width/2, janela.height/2 + sair.height/2 + 80)
        
    # Clique nos botões:
        # Botão "Opcões":
        if cursor.is_over_area((opcoes.x , opcoes.y),(opcoes.x + opcoes.width , opcoes.y + opcoes.height)) and cursor.is_button_pressed(1):   
            # Caso o cursor esteja em cima do botão Opções e o
            # botão esquerdo do mouse for apertado -- > Chamar todo o "opcoes.py".
            x = Opcoes()
            print(x)
        
        # Botão "jogar":
        elif cursor.is_over_area((jogar.x , jogar.y),(jogar.x + jogar.width , jogar.y + jogar.height)) and cursor.is_button_pressed(1):
            # Caso o cursor esteja em cima do botão Jogar,
            # e o botão essquerdo do mouse for apertado --> Chamar todo o "jogar.py".
            x = game.Jogar()
            print(x)
        

        # Botão "sair":
        elif cursor.is_over_area(( sair.x ,sair.y),(sair.x + sair.width, sair.y + sair.height )) and cursor.is_button_pressed(1):
            # Caso o cursor esteja em cimma do botão sair e o
            # botão do mouse for apertado --> Fechar Janela
            janela.close()
        # Desenhos:
        fundo.draw()
        jogar.draw()
        opcoes.draw()
        sair.draw()
        #janela.draw_text('DOJO CAT:',395,50,120,(255,255,255),"Happy Camper")
        #janela.draw_text('A vingança de Nay',415,120,60,(255,255,255),"Happy Camper")
        janela.update()