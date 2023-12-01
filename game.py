from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.collision import *
from PPlay.keyboard import *
from PPlay.mouse import *
from vida import *
import math

from globalVar import *

def Jogar():
    # VARIÁVEIS GLOBAIS
    global w,h
    global janela

    global jogador
    global ultimaDir
    global transitioning

    global velocity_y, velocity_x
    global usandoInvestida, velInvestida, distInvestida, timerDistInvestida
    global cooldownInvestida, cooldownInvestidaTimer

    global anguloMouse
    global vet_x, vet_y
    global contadorQuadros
    global ultimasCoords

    global mapa

    global active_sala
    global vel_cam_x
    global vel_cam_y
    global swapRight, swapLeft, swapDown, swapUp
    global timer

    global dc_speed

    global v_str

    cursor.hide()
    janela.set_title('Dojo Cat - Build Incompleta')

    while True:

        # MOVIMENTO DO JOGADOR
        if(key_input.key_pressed('w') and not usandoInvestida):                                      # Tecla W Pressionada
            velocity_y = -velMovimento
        elif(velocity_y < 0 and not usandoInvestida):
            transitioning = True
            velocity_y = 0
            #velocity_y+=dc_speed*janela.delta_time()

        if(key_input.key_pressed('s') and not usandoInvestida):                                      # Tecla S Pressionada
            velocity_y = velMovimento
        elif(velocity_y > 0 and not usandoInvestida):
            velocity_y = 0
            transitioning = True
            #velocity_y-=dc_speed*janela.delta_time()
        
        if(key_input.key_pressed('a') and not usandoInvestida):                                      # Tecla A Pressionada
            velocity_x = -velMovimento
            ultimaDir = 'left'
            transitioning = False
        elif(velocity_x < 0 and not usandoInvestida):
            transitioning = True
            velocity_x = 0
            #velocity_x+=dc_speed*janela.delta_time()

        if(key_input.key_pressed('d') and not usandoInvestida):                                     # Tecla D Pressionada
            velocity_x = velMovimento
            ultimaDir = 'right'
            transitioning = False
        elif(velocity_x > 0 and not usandoInvestida):
            velocity_x = 0
            transitioning = True
            #velocity_x-=dc_speed*janela.delta_time()

        # INVESTIDA
        if(not usandoInvestida):
            cooldownInvestidaTimer += janela.delta_time()

            jogador_centro_x = jogador.x + jogador.width / 2
            jogador_centro_y = jogador.y + jogador.height / 2
            cursor_x, cursor_y = cursor.get_position()

            mouse_x_relativo = cursor_x - jogador_centro_x
            mouse_y_relativo = cursor_y - jogador_centro_y

            tempoInvestida = distInvestida/velInvestida

            if (jogador_centro_x != 0 or jogador_centro_y != 0) and (cursor_x != 0 or cursor_y != 0):
                vet_x = (mouse_x_relativo)  / (math.sqrt((mouse_x_relativo)**2 + (mouse_y_relativo)**2))
                vet_y = (mouse_y_relativo) / (math.sqrt((mouse_y_relativo)**2 + (mouse_x_relativo)**2))
            else:
                vet_x = 0
                vet_y = 0

        if(key_input.key_pressed('space') and not usandoInvestida and cooldownInvestidaTimer > cooldownInvestida and not (swapDown or swapLeft or swapRight or swapUp)):
            usandoInvestida = True
        if(usandoInvestida):
            timerDistInvestida += janela.delta_time()
            if(timerDistInvestida <= tempoInvestida):
                velocity_x = velInvestida * vet_x
                velocity_y = velInvestida * vet_y
            else:
                cooldownInvestidaTimer = 0
                usandoInvestida = False
                timerDistInvestida = 0


        if(velocity_x < 10 and velocity_x > -10 and not usandoInvestida):                           # Desacelerar jogador (Zerar a velocidade com valores próximos de 0)
            velocity_x = 0
        if(velocity_y < 10 and velocity_y > -10 and not usandoInvestida):
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
            jogador.setAnim(1)

        if(velocity_x == -velMovimento):                                                # Se estiver se movendo pra esquerda, estado da animação 0 (Esquerda)
            jogador.setAnim(2)
        
        if((velocity_y == velMovimento or velocity_y == -velMovimento) and not usandoInvestida):
            if(ultimaDir=='left'):
                jogador.setAnim(2)
                
            if(ultimaDir=='right'):
                jogador.setAnim(1)

        if(usandoInvestida):
            if(mouse_x_relativo > 0):
                jogador.setAnim(3)
                ultimaDir = 'right'
            if(mouse_x_relativo < 0):
                jogador.setAnim(4)
                ultimaDir = 'left'

        if(velocity_x == 0 and velocity_y == 0):
            if(ultimaDir=='left'):
                jogador.image.set_sequence(9,9,True)
            if(ultimaDir=='right'):
                jogador.image.set_sequence(0,0,True)

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
                active_sala[0] -= 1
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
                active_sala[0] += 1
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
                active_sala[1] -= 1

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
                active_sala[1] += 1

        #janela.set_title(v_str)
        #v_str = str(active_sala)

        janela.set_background_color((22,22,22))
        
        for s in todos_sprites:
            s.DrawSala()

        jogador.draw()

        for s in todos_sprites:
            s.DrawFrenteJogador()
            if(active_sala[0] == s.adress[0] and active_sala[1] == s.adress[1] and not swapDown and not swapLeft and not swapRight and not swapUp):
                s.UpdateEntities(jogador,janela)

        if(not swapLeft and not swapRight and not swapDown and not swapUp and podeMover):
            jogador.move_x(velocity_x*janela.delta_time())
            jogador.move_y(velocity_y*janela.delta_time())

        # REGISTRAR COORDENADAS DOS ÚLTIMOS QUADROS PARA COLISÃO
        ultimasCoords.append((jogador.x,jogador.y))
        if(len(ultimasCoords) > 2):
            ultimasCoords.pop(0)

        # CROSSHAIR
        crosshair.set_position(cursor_x-crosshair.width/2,cursor_y-crosshair.height/2)
        crosshair.draw()

        drawCoracoes()

        jogador.update()
        janela.update()