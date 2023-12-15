from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.collision import *
from PPlay.keyboard import *
from PPlay.mouse import *
import mapgenerator
from jogadorClass import *
from soundmanager import *

# JANELA E DEFINIÇOES
w,h = 1200,675
janela = Window(w,h)

# DISPOSITIVOS DE ENTRADA
key_input = keyboard.Keyboard()
cursor = Mouse()

# SPRITES
jogador = Jogador((0,0))
ultimaDir = 'right'
transitioning = False
crosshair = Sprite('assets/crosshair.png')
fundoEscuro = Sprite('assets/fundopause.png')

todos_sprites = []

# CONFIGURAÇÕES E VARIÁVEIS DO JOGO
velMovimento = 270

podeMover = True
velocity_x = 0                                                         # Velocidade atual do jogador no eixo X
velocity_y = 0                                                         # Velocidade atual do jogador no eixo Y

usandoInvestida = False
velInvestida = 800
distInvestida = 230
timerDistInvestida = 0
inimigosDanificados = []
interactablesAfetados = []

cooldownInvestida = 2
cooldownInvestidaTimer = 2

attacking = False
ataqueTimer = 0

vet_x = 0
vet_y = 0

contadorQuadros = 0
ultimasCoords = []

# GERAÇÃO DE MAPA
mapa = []

# SCREEN SWAP
active_sala = [0,0]

vel_cam_x = 1550
vel_cam_y = 1000
swapRight = False
swapLeft = False
swapUp = False
swapDown = False
timer = 0

soundManager = AudioManager()

timerStartGame = 0

# DESACELERAÇÃO
dc_speed = 1200
# UI
pos_barrainvestida = (w-300,h-50)

# SOM
timersoma = 0

v_str = ''
