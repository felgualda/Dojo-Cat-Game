from PPlay.keyboard import *

# DISPOSITIVOS DE ENTRADA
key_input = Keyboard()

# CONFIGURAÇÕES E VARIÁVEIS DO JOGO
velMovimento = 270

podeMover = True
velocity_x = 0                                                         # Velocidade atual do jogador no eixo X
velocity_y = 0                                                         # Velocidade atual do jogador no eixo Y

# Desaceleração
dc_speed = 1200
x_tela = 0

def Movimento(jogador,janela):
    global velocity_x, velocity_y
    # MOVIMENTO DO JOGADOR
    if(key_input.key_pressed('w')):                                      # Tecla W Pressionada
        velocity_y = -velMovimento
    elif(velocity_y < 0):
        velocity_y+=dc_speed*janela.delta_time()

    if(key_input.key_pressed('s')):                                      # Tecla S Pressionada
        velocity_y = velMovimento
    elif(velocity_y > 0):
        velocity_y-=dc_speed*janela.delta_time()
    
    if(key_input.key_pressed('a')):                                      # Tecla A Pressionada
        velocity_x = -velMovimento
    elif(velocity_x < 0):
        velocity_x+=dc_speed*janela.delta_time()

    if(key_input.key_pressed('d')):                                     # Tecla D Pressionada
        velocity_x = velMovimento
    elif(velocity_x > 0):
        velocity_x-=dc_speed*janela.delta_time()

    if(velocity_x < 10 and velocity_x > -10):                           # Desacelerar jogador (Zerar a velocidade com valores próximos de 0)
        velocity_x = 0
    if(velocity_y < 10 and velocity_y > -10):
        velocity_y = 0            

    if(podeMover):
        jogador.move_x(velocity_x*janela.delta_time())
        jogador.move_y(velocity_y*janela.delta_time())