import pygame
from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.collision import *
from PPlay.keyboard import *
from sala import *
from pygame import *
import mapgenerator

# DEFINIÇÃO DA JANELA
w,h = 1200,675
janela = Window(w,h)
janela.set_background_color((22,22,22))

# DISPOSITIVOS DE ENTRADA
key_input = keyboard.Keyboard()

# SPRITES E ANIMAÇÕES
jogador = Sprite('assets/gato.png',2)

todos_sprites = mapgenerator.todasSalas

# POSIÇÕES INICIAIS
jogador.set_position(w/2-40.5,h/2-40.5)

# CONFIGURAÇÕES E VARIÁVEIS DO JOGO
velMovimento = 270

podeMover = True
velocity_x = 0                                                         # Velocidade atual do jogador no eixo X
velocity_y = 0                                                         # Velocidade atual do jogador no eixo Y

contadorQuadros = 0
ultimasCoords = []

# GERAÇÃO DE MAPA
mapa = mapgenerator.GenerateMap(14,8)


#screen_swap
vel_cam_x = 1550
vel_cam_y = 1000
swapRight = False
swapLeft = False
swapUp = False
swapDown = False
timer = 0

#desaceleração
dc_speed = 1200
x_tela = 0

# FUNÇÕES

v_str = ''
print(mapa)
mapgenerator.SetSalas(mapa)
while True:
    x = jogador.x
    y = jogador.y

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

    # COLISÃO DO JOGADOR
    for i in todos_sprites:
        for j in i.col:
            if(jogador.collided(j)):
                velocity_x = 0
                velocity_y = 0

                jogador.set_position(ultimasCoords[0][0],ultimasCoords[0][1])

    # SPRITE DO JOGADOR
    if(velocity_x > 0):                                                  # Se estiver se movendo pra direita, estado da animação 0 (Direita)
        jogador.set_curr_frame(0)

    elif(velocity_x < 0):                                                # Se estiver se movendo pra esquerda, estado da animação 0 (Esquerda)
        jogador.set_curr_frame(1)

    # MOVIMENTO ENTRE SALAS

    if(jogador.x < 0):                                                   # Jogador passou para sala a ESQUERDA
        swapLeft = True
    if(swapLeft):
        #ultimasCoords.clear()                                             # Limpa a lista de últimas coordenadas para evitar problemas de posicionamento enquanto muda de tela

        tempo_resto = w/vel_cam_x
        vel_jogador = (w-jogador.width-20)/tempo_resto
        
        if(timer <= tempo_resto):
            for s in todos_sprites:
                s.Mover_X(vel_cam_x*janela.delta_time())
            jogador.move_x(vel_jogador*janela.delta_time())
            timer += janela.delta_time()
        else:
            swapLeft = False
            timer = 0

    if(jogador.x > w-jogador.width):                                      # Jogador passou para sala a DIREITA
        swapRight = True
    if(swapRight):
        #ultimasCoords.clear()                                             # Limpa a lista de últimas coordenadas para evitar problemas de posicionamento enquanto muda de tela

        tempo_resto = w/vel_cam_x
        vel_jogador = (w-jogador.width-20)/tempo_resto
        
        if(timer <= tempo_resto):
            for s in todos_sprites:
                s.Mover_X(-vel_cam_x*janela.delta_time())
            jogador.move_x(-vel_jogador*janela.delta_time())
            timer += janela.delta_time()
        else:
            swapRight = False
            timer = 0
        
    if(jogador.y < 0):                                                    # Jogador passou para sala a CIMA
        swapUp = True
    if(swapUp):
        #ultimasCoords.clear()                                             # Limpa a lista de últimas coordenadas para evitar problemas de posicionamento enquanto muda de tela

        tempo_resto = h/vel_cam_y
        vel_jogador = (h-jogador.height-10)/tempo_resto
        
        if(timer <= tempo_resto):
            for s in todos_sprites:
                s.Mover_Y(vel_cam_y*janela.delta_time())
            jogador.move_y(vel_jogador*janela.delta_time())
            timer += janela.delta_time()
        else:
            swapUp = False
            timer = 0

    if(jogador.y > h-jogador.height):                                      # Jogador passou para sala a BAIXO
        swapDown = True
    if(swapDown):
        #ultimasCoords.clear()                                             # Limpa a lista de últimas coordenadas para evitar problemas de posicionamento enquanto muda de tela

        tempo_resto = h/vel_cam_y
        vel_jogador = (h-jogador.height-10)/tempo_resto
        
        if(timer <= tempo_resto):
            for s in todos_sprites:
                s.Mover_Y(-vel_cam_y*janela.delta_time())
            jogador.move_y(-vel_jogador*janela.delta_time())
            timer += janela.delta_time()
        else:
            swapDown = False
            timer = 0

    janela.set_title(v_str)
    v_str = 'x: ' + str(jogador.x) + ' y: ' + str(jogador.y)

    #if(bola.rect.y >= h-bola.height or bola.rect.y <= 0):
        #velocity_y *= -1
    janela.set_background_color(000)
    
    for s in todos_sprites:
        s.DrawSala()

    jogador.draw()

    for s in todos_sprites:
        s.DrawFrenteJogador()
    if(not swapLeft and not swapRight and not swapDown and not swapUp and podeMover):
        jogador.move_x(velocity_x*janela.delta_time())
        jogador.move_y(velocity_y*janela.delta_time())
    
    # REGISTRAR COORDENADAS DOS ÚLTIMOS QUADROS PARA COLISÃO
    ultimasCoords.append((jogador.x,jogador.y))
    if(len(ultimasCoords) > 2):
        ultimasCoords.pop(0)
    
    janela.update()