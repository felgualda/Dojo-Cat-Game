from PPlay.sprite import *
from globalVar import *
import math
from ratinho import *

class BossBattle():
    def __init__(self,x,y) -> None:
        #BOSS
        self.tag='boss'

        self.started = False

        self.bossImage = Sprite('assets/inimigos/boss_sheet.png',24)
        self.bossDmgImage = Sprite('assets/inimigos/boss_sheet_dmg.png',24)
        self.mortoSprite = Sprite('assets/rato-morto.png')

        self.bossbar = Sprite('assets/bossbar.png',22)
        self.bossbar.set_position(294,29)

        self.quadro = 0

        self.tempoSpawnRatinhos = 7
        self.timerSpawnRatinhos = 6
        self.ratinhos = []

        self.bossImage.set_position(x+600-self.bossImage.width/2,y+337.5-self.bossImage.height/2)
        self.bossDmgImage.set_position(x+600-self.bossImage.width/2,y+337.5-self.bossImage.height/2)
        self.mortoSprite.set_position(496,334)

        self.bossImage.set_sequence_time(0,23,120,True)
        self.bossDmgImage.set_sequence_time(0,23,120,True)

        self.bossAttackRange = 230
        self.bossState = 0

        self.socando = False
        self.podeAtacar = False

        self.bossSocoCooldown = 3.5
        self.bossSocoCooldownTimer = 0

        self.vivo = True
        self.vidaMax = 770
        self.vida = self.vidaMax
        self.levouDano = False

        self.tempoSpriteDano = 0.25
        self.tempoSpriteTimer = 0

        self.esperaFim = 5
        self.esperaFimTimer = 0
        self.venceu = False

    def move_x(self,speed):
        self.bossImage.x += speed
        self.bossDmgImage.x += speed

    def move_y(self,speed):
        self.bossImage.y += speed
        self.bossDmgImage.y += speed

    def Draw(self):
        for r in self.ratinhos:
            r.Draw()

        if(self.vivo):
            if(self.levouDano):
                self.bossDmgImage.draw()
            else:
                self.bossImage.draw()
        else:
            self.mortoSprite.draw()
        
    def DrawBossBar(self):
        if(self.started):
            self.bossbar.draw()

    def Attack(self,jogador,soundmanager):
        norma = math.sqrt(((jogador.x +jogador.width/2) - (self.bossImage.x+self.bossImage.width/2))**2 + ((jogador.y +jogador.height/2) - (self.bossImage.y+self.bossImage.height/2))**2)

        if(self.bossImage.x+self.bossImage.width/2 > jogador.x and not self.socando):
            self.socando = True
            if self.bossImage.get_curr_frame() < 16 or self.bossImage.get_curr_frame() > 23:
                self.bossImage.set_sequence(16,23,True)
            if self.bossDmgImage.get_curr_frame() < 16 or self.bossDmgImage.get_curr_frame() > 23:
                self.bossDmgImage.set_sequence(16,23,True)

        if(self.bossImage.x+self.bossImage.width/2 <= jogador.x and not self.socando):
            self.socando = True
            if self.bossImage.get_curr_frame() < 8 or self.bossImage.get_curr_frame() > 15:
                self.bossImage.set_sequence(8,15,True)
            if self.bossDmgImage.get_curr_frame() < 8 or self.bossDmgImage.get_curr_frame() > 15:
                self.bossDmgImage.set_sequence(8,15,True)

        if(self.bossImage.get_curr_frame()==12 or self.bossImage.get_curr_frame()==21):
            # Frame de ataque
            if(self.podeAtacar and norma < self.bossAttackRange):
                jogador.LevarDano(soundmanager)
            self.podeAtacar = False
            self.bossSocoCooldownTimer = 0

        if(self.bossImage.get_curr_frame()==14 or self.bossImage.get_curr_frame()==22):
            # Fim da animação
            self.socando = False
            self.bossState=0

    def LevarDano(self,dano):
        if(self.vivo):
            self.vida -= dano
            self.levouDano = True
            self.quadro = ((self.vidaMax-self.vida)//35)

    def Update(self,jogador,janela,soundmanager):
        
        if(self.bossbar.get_curr_frame() != self.quadro):
            self.bossbar.set_curr_frame(self.quadro)

        if(self.vivo):
            if(self.vida <= 0):
                self.vivo = False

            if(self.levouDano):
                self.tempoSpriteTimer += janela.delta_time()
            if(self.tempoSpriteTimer >= self.tempoSpriteDano):
                self.levouDano = False
                self.tempoSpriteTimer = 0

            if(not self.podeAtacar):
                self.bossSocoCooldownTimer += janela.delta_time()
            if(not self.podeAtacar and self.bossSocoCooldownTimer >= self.bossSocoCooldown):
                self.podeAtacar = True

            norma = math.sqrt(((jogador.x +jogador.width/2) - (self.bossImage.x+self.bossImage.width/2))**2 + ((jogador.y +jogador.height/2) - (self.bossImage.y+self.bossImage.height/2))**2)

            if(self.bossState == 0):
                if(self.bossImage.x+self.bossImage.width/2 > jogador.x):
                    if self.bossImage.get_curr_frame() < 4 or self.bossImage.get_curr_frame() > 7:
                        self.bossImage.set_sequence(4,7,True)
                    if self.bossDmgImage.get_curr_frame() < 4 or self.bossDmgImage.get_curr_frame() > 7:
                        self.bossDmgImage.set_sequence(4,7,True)

                if(self.bossImage.x+self.bossImage.width/2 <= jogador.x):
                    if self.bossImage.get_curr_frame() < 0 or self.bossImage.get_curr_frame() > 3:
                        self.bossImage.set_sequence(0,3,True)
                    if self.bossDmgImage.get_curr_frame() < 0 or self.bossDmgImage.get_curr_frame() > 3:
                        self.bossDmgImage.set_sequence(0,3,True)

            if(norma <= self.bossAttackRange and self.podeAtacar):
                self.bossState = 1

            if(self.bossState==1):
                self.Attack(jogador,soundmanager)

            self.timerSpawnRatinhos += janela.delta_time()
            if(self.timerSpawnRatinhos >= self.tempoSpawnRatinhos and len(self.ratinhos) <= 10):
                self.ratinhos.append(Ratinho(315,129))
                self.ratinhos.append(Ratinho(834,129))
                self.timerSpawnRatinhos = 0

            for r in self.ratinhos:
                r.Update(janela)
            
            self.bossDmgImage.update()
            self.bossImage.update()
            self.bossbar.update
        else:
            self.ratinhos = []
            self.esperaFimTimer += janela.delta_time()
            if(self.esperaFimTimer >= self.esperaFim):
                self.venceu = True

