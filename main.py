from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.collision import *
from PPlay.keyboard import *
from PPlay.mouse import *
from sala import *
from pygame import *
import math
import mapgenerator

# DEFINIÇÃO DA JANELA
w,h = 1200,675
janela = Window(w,h)
janela.set_background_color((22,22,22))

# DISPOSITIVOS DE ENTRADA
key_input = keyboard.Keyboard()
cursor = Mouse()

# SPRITES E ANIMAÇÕES
jogador = Sprite('assets/gato_animacao-Sheet.png',18)
jogador.set_sequence_time(0,18,50,True)
jogador.set_sequence(0,0,True)
ultimaDir = 'right'
transitioning = False

todos_sprites = mapgenerator.todasSalas

# POSIÇÕES INICIAIS
jogador.set_position(w/2-40.5,h/2-40.5)

# CONFIGURAÇÕES E VARIÁVEIS DO JOGO
velMovimento = 270

podeMover = True
velocity_x = 0                                                         # Velocidade atual do jogador no eixo X
velocity_y = 0                                                         # Velocidade atual do jogador no eixo Y

usandoInvestida = False
velInvestida = 200
distInvestida = 200
timerDistInvestida = 0
anguloMouse = 0

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
        ultimaDir = 'left'
        transitioning = False
    elif(velocity_x < 0):
        transitioning = True
        velocity_x+=dc_speed*janela.delta_time()

    if(key_input.key_pressed('d')):                                     # Tecla D Pressionada
        velocity_x = velMovimento
        ultimaDir = 'right'
        transitioning = False
    elif(velocity_x > 0):
        transitioning = True
        velocity_x-=dc_speed*janela.delta_time()

    # INVESTIDA

    mouse_x_relativo = cursor.get_position()[0] - jogador.x - jogador.width/2
    mouse_y_relativo = cursor.get_position()[1] - jogador.y - jogador.height/2

    tempoInvestida = distInvestida/velInvestida
    
    if(not usandoInvestida):
        jogador_centro_x = jogador.x - jogador.width / 2
        jogador_centro_y = jogador.y - jogador.height / 2
        cursor_x, cursor_y = cursor.get_position()
        if (jogador_centro_x != 0 or jogador_centro_y != 0) and (cursor_x != 0 or cursor_y != 0):
            try:
                anguloMouse = math.degrees(math.acos(((cursor_x-jogador_centro_x)*(-cursor_y-jogador_centro_y))/((cursor_x-jogador_centro_x)*math.sqrt((-cursor_y-jogador_centro_y)**2 + 1))))
            except:
                anguloMouse = 0
        else:
            anguloMouse = 0

    if(key_input.key_pressed('space')):
        usandoInvestida = True
    if(usandoInvestida):
        timerDistInvestida += janela.delta_time()
        if(timerDistInvestida <= tempoInvestida):
            velocity_x = velInvestida * distInvestida
            velocity_y = velInvestida * distInvestida

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
    if(velocity_x == velMovimento):                                                  # Se estiver se movendo pra direita, estado da animação 0 (Direita)
        if jogador.get_curr_frame() < 2 or jogador.get_curr_frame() > 9:
            jogador.set_sequence(2, 9, True)

    if(velocity_x == -velMovimento):                                                # Se estiver se movendo pra esquerda, estado da animação 0 (Esquerda)
        if jogador.get_curr_frame() < 11 or jogador.get_curr_frame() > 18:
            jogador.set_sequence(11, 18, True)
    
    if(transitioning):
        if(ultimaDir=='left'):
            jogador.set_curr_frame(10)
        if(ultimaDir=='right'):
            jogador.set_curr_frame(1)

    if(velocity_x == 0):
        transitioning = False

        if(ultimaDir=='left'):
            jogador.set_sequence(9,9,True)
        if(ultimaDir=='right'):
            jogador.set_sequence(0,0,True)


    # MOVIMENTO ENTRE SALAS

    if(jogador.x < 0):                                                   # Jogador passou para sala a ESQUERDA
        swapLeft = True
    if(swapLeft):

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
    v_str = 'x: ' + str(mouse_x_relativo) + ' y: ' + str(mouse_y_relativo) + ' ang: ' + str(anguloMouse)

    janela.set_background_color((22,22,22))
    
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
    
    jogador.update()
    janela.update()