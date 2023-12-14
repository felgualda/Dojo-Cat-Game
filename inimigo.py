from PPlay.sprite import *
from PPlay.window import *
from particleHandler import *
import math
import random

class Inimigo:
    def __init__(self,pos,var):
        # Sprites e posições
        self.x = pos[0]
        self.y = pos[1]

        self.tag = 'enemy'

        self.vivo = True
        
        self.var = var
        self.image = Sprite('assets/inimigos/ninja-sheet.png')
        self.dmgSheet = Sprite('assets/inimigos/archer-sheet-dmg.png',53)
        
        self.hitbox = Sprite('assets\inimigos\enemy-hitbox.png')
        self.hitbox.set_position(self.x+42,self.y-18)

        # Definição de sprite conforme a variação
        if(var == 1):
            self.image = Sprite('assets/inimigos/ninja-sheet.png',36)
            self.dmgSheet = Sprite('assets/inimigos/ninja-sheet-dmg.png',36)

            self.dmgSheet.set_sequence_time(0,36,120)
            self.image.set_sequence_time(0,36,120)
        if(var == 2):
            self.image = Sprite('assets/inimigos/archer-sheet.png',53)
            self.dmgSheet = Sprite('assets/inimigos/archer-sheet-dmg.png',53)

            self.image.set_sequence_time(0,52,120)
            self.dmgSheet.set_sequence_time(0,52,120)

        self.image.set_position(self.x,self.y)

        self.centro_x = self.x + self.image.width/2
        self.centro_y = self.y + self.image.height/2

        # Variáveis do inimigo e IA
        self.vida = 100

        self.dirJogador = []

        if(self.var==2):
            self.vel_inimigo_max = 135
        if(self.var==1):
            self.vel_inimigo_max = 100
        self.state = 0

        self.podeAtacar = False
        self.attackCooldown = 0.8
        if(self.var==1):
            self.attackCooldown = 0.8
        if(self.var==2):
            self.attackCooldown = 2
        self.attackCooldownTimer = random.uniform(0,self.attackCooldown)

        self.distanciaMira = 1000
        self.mirando = False
        self.atirou = False
        self.facing = 'right'

        self.velx = 0
        self.vely = 0

        self.levouDano = False
        self.tempoSpriteDano = 0.25
        self.tempoSpriteTimer = 0

        self.ultimasCoords = []

    def move_x(self,speed):
        self.x += speed
        self.image.set_position(self.x, self.y)
        self.dmgSheet.set_position(self.x,self.y)

    def move_y(self,speed):
        self.y += speed
        self.image.set_position(self.x, self.y)
        self.dmgSheet.set_position(self.x,self.y)

    def Draw(self):
        if(self.levouDano):
            self.dmgSheet.draw()
        else:
            self.image.draw()
        #self.hitbox.draw()

    def LevarDano(self,dano):
        if(self.vivo):
            FX_blood(self.centro_x,self.centro_y)
            self.vida -= dano
            self.levouDano = True

        if(self.vida <= 0):
            self.Morrer()

    def Morrer(self):
        self.vivo = False

    def Stalk(self, target, janela,col,colportas):
        # Vetor normalizado entre inimigo e alvo
        #target.
        norma = math.sqrt(((target.x +target.width/2) - self.centro_x)**2 + ((target.y +target.height/2) - self.centro_y)**2)
        vet_x = ((target.x +target.width/2)- self.centro_x)/norma
        vet_y = ((target.y+target.height/2)- self.centro_y)/norma

        self.velx = vet_x * self.vel_inimigo_max * janela.delta_time()
        self.vely = vet_y * self.vel_inimigo_max * janela.delta_time()

        if(self.var==2):
            for c in col:
                if(self.image.collided(c)):
                    self.velx = 0
                    self.vely = 0
                    self.x = self.ultimasCoords[0][0]
                    self.y = self.ultimasCoords[0][1]
                    self.image.set_position(self.x,self.y)
            for c in colportas:
                if(self.image.collided(c)):
                    self.velx = 0
                    self.vely = 0
                    self.x = self.ultimasCoords[0][0]
                    self.y = self.ultimasCoords[0][1]
                    self.image.set_position(self.x,self.y)
        
        self.ultimasCoords.append((self.x,self.y))
        if(len(self.ultimasCoords) > 2):
            self.ultimasCoords.pop(0)

        if(self.var == 1):
            self.move_x(self.velx)
            self.move_y(self.vely)
        if(self.var == 2):
            if(not self.levouDano):
                if(norma > self.distanciaMira/3):
                    self.move_x(self.velx)
                    self.move_y(self.vely)
                else:
                    self.move_x(-self.velx/2)
                    self.move_y(-self.vely/2)

        return norma
        
    def Attack(self,target):
        norma = math.sqrt(((target.x +target.width/2) - self.centro_x)**2 + ((target.y +target.height/2) - self.centro_y)**2)
        vet_x = ((target.x +target.width/2)- self.centro_x)/norma
        vet_y = ((target.y+target.height/2)- self.centro_y)/norma

        if(self.var==1):
            if(self.image.get_curr_frame()==25 or self.image.get_curr_frame()==35):
                self.state=0

            if(self.velx > 0):
                if self.image.get_curr_frame() < 18 or self.image.get_curr_frame() > 26:
                    self.image.set_sequence(18,26,True)
                if self.dmgSheet.get_curr_frame() < 18 or self.dmgSheet.get_curr_frame() > 26:
                    self.dmgSheet.set_sequence(18,26,True)
            if(self.velx < 0):
                if self.image.get_curr_frame() < 28 or self.image.get_curr_frame() > 36:
                    self.image.set_sequence(28,36,True)
                if self.dmgSheet.get_curr_frame() < 28 or self.dmgSheet.get_curr_frame() > 36:
                    self.dmgSheet.set_sequence(28,36,True)
            
            if(self.image.get_curr_frame()==31 or self.image.get_curr_frame()==21):
                #Frame de ataque
                if(self.hitbox.collided(target.colisao)):
                    if(target.tag=='player' and self.podeAtacar):
                        target.LevarDano()
                        self.podeAtacar = False
                        self.attackCooldownTimer = 0
                        
        if(self.var==2):
            if(target.x < self.x and not self.mirando):
                self.mirando = True
                self.dirJogador = [vet_x,vet_y]
                if self.image.get_curr_frame() < 34 or self.image.get_curr_frame() > 52:
                    self.image.set_sequence(34,52,True)
                if self.dmgSheet.get_curr_frame() < 34 or self.dmgSheet.get_curr_frame() > 52:
                    self.dmgSheet.set_sequence(34,52,True)

            if(target.x >= self.x and not self.mirando):
                self.mirando = True
                self.dirJogador = [vet_x,vet_y]
                if self.image.get_curr_frame() < 15 or self.image.get_curr_frame() > 33:
                    self.image.set_sequence(15,33,True)
                if self.dmgSheet.get_curr_frame() < 15 or self.dmgSheet.get_curr_frame() > 33:
                    self.dmgSheet.set_sequence(15,33,True)
            
            if(self.image.get_curr_frame()==29 or self.image.get_curr_frame()==48):
                if(vet_x < 0 and self.facing=='left'):
                    self.dirJogador = [vet_x,vet_y]
                elif(vet_x >= 0 and self.facing=='right'):
                    self.dirJogador = [vet_x,vet_y]

                #Frame de ataque
                if(self.podeAtacar):
                    self.atirou = True
                self.podeAtacar = False
                self.attackCooldownTimer = 0

            if(self.image.get_curr_frame()==32 or self.image.get_curr_frame()==51):
                # Fim da animação
                self.mirando = False
                self.state=0


    def Update(self,jogador,janela,colisoes,colportas):
        if(self.vivo):
            if(jogador.x > self.x and self.mirando == False):
                self.facing = 'right'
            if(jogador.x <= self.x and self.mirando == False):
                self.facing = 'left'

            if(not self.podeAtacar):
                self.attackCooldownTimer += janela.delta_time()
            if(not self.podeAtacar and self.attackCooldownTimer >= self.attackCooldown):
                self.podeAtacar = True

            if(self.levouDano):
                self.tempoSpriteTimer += janela.delta_time()
            if(self.tempoSpriteTimer >= self.tempoSpriteDano):
                self.levouDano = False
                self.tempoSpriteTimer = 0

            # APRENDIZ
            if(self.var==1):
                if(self.velx > 0 and not self.levouDano and self.state==0):
                    self.hitbox.set_position(self.x+42,self.y+27)
                    if self.image.get_curr_frame() < 1 or self.image.get_curr_frame() > 7:
                        self.image.set_sequence(1,7,True)
                    if self.dmgSheet.get_curr_frame() < 1 or self.dmgSheet.get_curr_frame() > 7:
                        self.dmgSheet.set_sequence(1,7,True)
                if(self.velx < 0 and not self.levouDano and self.state==0):
                    self.hitbox.set_position(self.x-6,self.y+27)
                    if self.image.get_curr_frame() < 8 or self.image.get_curr_frame() > 14:
                        self.image.set_sequence(8,14,True)
                    if self.dmgSheet.get_curr_frame() < 8 or self.dmgSheet.get_curr_frame() > 14:
                        self.dmgSheet.set_sequence(8,14,True)

            # ARQUEIRO

            if(self.var==2):
                if(self.velx > 0 and not self.levouDano and self.state==0):
                    if self.image.get_curr_frame() < 1 or self.image.get_curr_frame() > 7:
                        self.image.set_sequence(1,7,True)
                    if self.dmgSheet.get_curr_frame() < 1 or self.dmgSheet.get_curr_frame() > 7:
                        self.dmgSheet.set_sequence(1,7,True)
                if(self.velx < 0 and not self.levouDano and self.state==0):
                    self.hitbox.set_position(self.x-6,self.y+27)
                    if self.image.get_curr_frame() < 8 or self.image.get_curr_frame() > 14:
                        self.image.set_sequence(8,14,True)
                    if self.dmgSheet.get_curr_frame() < 8 or self.dmgSheet.get_curr_frame() > 14:
                        self.dmgSheet.set_sequence(8,14,True)

            self.image.update()
            self.dmgSheet.update()

            self.centro_x = self.x + self.image.width/2
            self.centro_y = self.y + self.image.height/2

            if(self.state==0 and self.var ==1):
                self.Stalk(jogador,janela,colisoes,colportas)

            if(self.state==1 and self.var==1):
               self.Attack(jogador)

            if(self.state==1 and self.var==2):
                self.Attack(jogador)

            if(self.state==0 and self.var==2):
                x = self.Stalk(jogador,janela,colisoes,colportas)
                if(x < self.distanciaMira and self.podeAtacar):
                    self.state = 1
            
            if(self.var==1):
                if(self.hitbox.collided(jogador.colisao) and self.podeAtacar):
                    self.state = 1
            
            if(self.atirou):
                return self.atirou
            return False

