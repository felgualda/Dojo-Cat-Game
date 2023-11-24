from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.collision import *
from PPlay.keyboard import *
from PPlay.mouse import *
import mapgenerator

# JANELA E DEFINIÇOES
w,h = 1200,675
janela = Window(w,h)

# DISPOSITIVOS DE ENTRADA
key_input = keyboard.Keyboard()
cursor = Mouse()

# SPRITES
jogador = Sprite('assets/gato_animacao-Sheet.png',18)
ultimaDir = 'right'
transitioning = False

todos_sprites = mapgenerator.todasSalas

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

# SCREEN SWAP
vel_cam_x = 1550
vel_cam_y = 1000
swapRight = False
swapLeft = False
swapUp = False
swapDown = False
timer = 0

# DESACELERAÇÃO
dc_speed = 1200

v_str = ''
