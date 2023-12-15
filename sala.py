from PPlay.sprite import *
from inimigo import *
from box import *
from spike import *
from pygame import mixer
from projectile import *
from bossbattle import *

class Sala:
    
    def __init__(self, adress, var):
        
        self.adress = adress

        self.x = self.adress[0] * 1200
        self.y = self.adress[1] * 675

        self.var = var
        self.cleared = False

        self.sprite = Sprite('assets/sala/sala.png')
        self.sprite.set_position(self.x,self.y)
        self.passagem = [Sprite('assets/sala/passages/TOP_PASSAGE.png'),Sprite('assets/sala/passages/BOTTOM_PASSAGE.png'),Sprite('assets/sala/passages/RIGHT_PASSAGE.png'),Sprite('assets/sala/passages/LEFT_PASSAGE.png')]
        self.portas = [Sprite('assets/portas/porta-cima_sheet.png',22),Sprite('assets/portas/porta-baixo_Sheet.png',22),Sprite('assets/portas/porta-direita_sheet.png',22),Sprite('assets/portas/porta-esquerda_sheet.png',22)]

        # PORTAS
        self.portasAbertas = True
        self.abrindoPortas = False

        self.passagem[0].set_position(528+self.x,0+self.y)
        self.passagem[1].set_position(528+self.x,573+self.y)
        self.passagem[2].set_position(1038+self.x,258+self.y)
        self.passagem[3].set_position(self.x,258+self.y)

        self.portas[0].set_position(537+self.x,81+self.y)
        self.portas[0].set_sequence_time(0,21,80,True)
        
        self.portas[1].set_position(537+self.x,594+self.y)
        self.portas[1].set_sequence_time(0,21,80,True)

        self.portas[2].set_position(1062+self.x,267+self.y)
        self.portas[2].set_sequence_time(0,21,80,True)

        self.portas[3].set_position(123+self.x,267+self.y)
        self.portas[3].set_sequence_time(0,21,80,True)

        self.portaDireita = False
        self.portaEsquerda = False
        self.portaCima = False
        self.portaBaixo = False

        # COLISÃO
        self.colPortas = []
        self.col = []
        for i in range(8):
            if i < 2:
                self.col.append(Sprite('assets/sala/up_corner_placeholder.png'))
            elif i < 4:
                self.col.append(Sprite('assets/sala/up_placeholder.png'))
            elif i < 6:
                self.col.append(Sprite('assets/sala/down_corner_placeholder.png'))
            else:
                self.col.append(Sprite('assets/sala/down_placeholder.png'))

        # INIMIGOS
        self.inimigos = []
        self.projectiles = []
        
        # MISC
        self.interactables = []
        self.spikes = []

        # VARIAÇÃO DE SALA
        if(self.var == 1):
            self.inimigos = [Inimigo((self.x + 1200/2, self.y + 675/2),2),Inimigo((self.x + 1200/2, self.y + 200),2),Inimigo((self.x + 350, self.y + 675/2),1),Inimigo((self.x + 850, self.y + 675/2),1)]
            self.interactables = [Box(self.x + 170,self.y+178),Box(self.x+908,self.y+511)]
        if(self.var == 2):
            self.inimigos = [Inimigo((self.x+250 , self.y+178 ),1),Inimigo((self.x+170 , self.y+511 ),1),Inimigo((self.x+908 , self.y+511 ),1)]
            self.interactables = [Box(self.x+170,self.y+178),Box(self.x+908,self.y+178)]
            self.spikes = [Spike(self.x+170,self.y+258),Spike(self.x+908,self.y+258),Spike(self.x+599-36,self.y+362)]
        if(self.var == 3):
            self.inimigos = [Inimigo((self.x+170 , self.y+288 ),1),Inimigo((self.x+170 , self.y+178 ),2),Inimigo((self.x+908 , self.y+178 ),2)]
            self.interactables= [Box(self.x+170,self.y+511),Box(self.x+908,self.y+511)]
            self.spikes = [Spike(self.x+250,self.y+178),Spike(self.x+250,self.y+511),Spike(self.x+828,self.y+178),Spike(self.x+828,self.y+511)]

        if(self.var == 4):
            self.inimigos = [Inimigo((self.x+170 , self.y+511 ),1),Inimigo((self.x+908 , self.y+288 ),1),Inimigo((self.x+908 , self.y+178 ),2)]
            self.interactables = [Box(self.x + 170,self.y+178),Box(self.x+908,self.y+511)]
            self.spikes = [Spike(self.x+679-36,self.y+362),Spike(self.x+599-36,self.y+362),Spike(self.x+519-36,self.y+362)]

        if(self.var == 5):
            self.inimigos = [Inimigo((self.x+270 , self.y+178 ),1),Inimigo((self.x+808 , self.y+178 ),1),Inimigo((self.x+170 , self.y+178 ),2),Inimigo((self.x+908 , self.y+511 ),2)]
            self.interactables = [Box(self.x+908,self.y+178),Box(self.x+170,self.y+511)]
            self.spikes = [Spike(self.x+599-36,self.y+282),Spike(self.x+599-36,self.y+362),Spike(self.x+599-36,self.y+442)]

        if(self.var == 6):
            self.inimigos = [Inimigo((self.x+170 , self.y+178 ),1),Inimigo((self.x+170 , self.y+511 ),1)]
            self.interactables = [Box(self.x+908,self.y+511),Box(self.x+908,self.y+178)]
            self.spikes = [Spike(self.x+679-36,self.y+362),Spike(self.x+599-36,self.y+362),Spike(self.x+519-36,self.y+362)]

        if(self.var == 7):
            self.inimigos = [Inimigo((self.x+808 , self.y+178 ),1),Inimigo((self.x+808 , self.y+511 ),1),Inimigo((self.x+908 , self.y+178 ),2),Inimigo((self.x+908 , self.y+511 ),2)]
            self.interactables = [Box(self.x + 170,self.y+178),Box(self.x+170,self.y+511)]
            self.spikes = [Spike(self.x+170,self.y+258),Spike(self.x+250,self.y+258),Spike(self.x+170,self.y+431)]

        if(self.var == 8):
            self.inimigos = [Inimigo((self.x+808 , self.y+178 ),1),Inimigo((self.x+250 , self.y+511 ),1),Inimigo((self.x+808 , self.y+511 ),2)]
            self.interactables = [Box(self.x + 170,self.y+178),Box(self.x+908,self.y+178),Box(self.x+170,self.y+511),Box(self.x+908,self.y+511)]
            self.spikes = [Spike(self.x+250,self.y+258),Spike(self.x+250,self.y+431),Spike(self.x+828,self.y+258),Spike(self.x+828,self.y+431)]

        if(self.var == 9):
            self.inimigos = [Inimigo((self.x+170 , self.y+178 ),1) ,Inimigo((self.x+908 , self.y+511 ),1),Inimigo((self.x+728 , self.y+178 ),2),Inimigo((self.x+908 , self.y+368 ),2)]
            self.interactables = [Box(self.x+170,self.y+431),Box(self.x+250,self.y+511)]
            self.spikes = [Spike(self.x+908,self.y+178),Spike(self.x+908,self.y+258),Spike(self.x+828,self.y+178)]

        if(self.var == 10):
            self.inimigos = [Inimigo((self.x+908 , self.y+178 ),1),Inimigo((self.x+751 , self.y+511 ),2),Inimigo((self.x+908 , self.y+431 ),2)]
            self.interactables = [Box(self.x + 250,self.y+178),Box(self.x + 170,self.y+258)]
            self.spikes = [Spike(self.x+457,self.y+511),Spike(self.x+457,self.y+431),Spike(self.x+671+36,self.y+511),Spike(self.x+671-36,self.y+431)]

        if(self.var == 11):
            self.inimigos = [Inimigo((self.x+908 , self.y+511 ),1),Inimigo((self.x+170 , self.y+178 ),1),Inimigo((self.x+170 , self.y+401 ),2),Inimigo((self.x+270 , self.y+511 ),2)]
            self.interactables = [Box(self.x+828,self.y+178),Box(self.x+908,self.y+258)]
            self.spikes = [Spike(self.x+748,self.y+178),Spike(self.x+828,self.y+258)]

        if(self.var == 12):
            self.inimigos = [Inimigo((self.x+170 , self.y+288 ),2),Inimigo((self.x+270 , self.y+178 ),2)]
            self.interactables = [Box(self.x+828,self.y+511),Box(self.x+908,self.y+431)] 
            self.spikes = [Spike(self.x+599-36,self.y+362),Spike(self.x+748,self.y+511),Spike(self.x+828,self.y+431)]

        if(self.var == 13):
            self.inimigos = [Inimigo((self.x+908 , self.y+178 ),1),Inimigo((self.x+170 , self.y+511 ),1),Inimigo((self.x+908 , self.y+511 ),2)]
            self.interactables = [Box(self.x + 170,self.y+178),Box(self.x + 250,self.y+178)] 
            self.spikes = [Spike(self.x+599-36,self.y+282),Spike(self.x+599-36,self.y+362),Spike(self.x+599-36,self.y+442)]
	
        if(self.var == 14):
            self.inimigos = [Inimigo((self.x+170 , self.y+511 ),1),Inimigo((self.x+808 , self.y+178 ),1),Inimigo((self.x+908 , self.y+178 ),2),Inimigo((self.x+908 , self.y+511 ),2)]
            self.interactables = [Box(self.x + 170,self.y+178),Box(self.x + 170,self.y+258)]
            self.spikes = [Spike(self.x+679-36,self.y+362),Spike(self.x+599-36,self.y+362),Spike(self.x+519-36,self.y+362)]

        if(self.var == 15):
            self.inimigos = [Inimigo((self.x+170 , self.y+178 ),2),Inimigo((self.x+908 , self.y+178 ),2)]
            self.interactables = [Box(self.x+170,self.y+511),Box(self.x+250,self.y+511)]
            self.spikes = [Spike(self.x+170,self.y+264),Spike(self.x+250,self.y+264),Spike(self.x+908+36,self.y+264),Spike(self.x+828+36,self.y+264)]

        if(self.var == 16):
            self.inimigos = [Inimigo((self.x+170 , self.y+178 ),1),Inimigo((self.x+908 , self.y+178 ),2),Inimigo((self.x+908 , self.y+511 ),2)]
            self.interactables = [Box(self.x+170,self.y+511),Box(self.x+170,self.y+431)]
            self.spikes = [Spike(self.x+250,self.y+511),Spike(self.x+330,self.y+511)]
	
        if(self.var == 17):
            self.inimigos = [Inimigo((self.x+170 , self.y+511 ),1),Inimigo((self.x+908 , self.y+178 ),1),Inimigo((self.x+170 , self.y+178 ),2)]
            self.interactables = [Box(self.x+908,self.y+511),Box(self.x+828,self.y+511)]
            self.spikes = [Spike(self.x+908,self.y+431),Spike(self.x+748,self.y+511)]

        if(self.var == 18):
            self.inimigos = [Inimigo((self.x+908 , self.y+178 ),1),Inimigo((self.x+270 , self.y+511 ),1),Inimigo((self.x+170 , self.y+178 ),2),Inimigo((self.x+170 , self.y+511 ),2)]
            self.interactables = [Box(self.x+908,self.y+511),Box(self.x+908,self.y+431)]
            self.spikes = [Spike(self.x+599-36,self.y+362),Spike(self.x+828,self.y+511)]

        if(self.var == 19):
            self.inimigos = [Inimigo((self.x+170 , self.y+178 ),1),Inimigo((self.x+908 , self.y+401 ),1),Inimigo((self.x+908 , self.y+511 ),2),Inimigo((self.x+170 , self.y+511 ),2)]
            self.interactables = [Box(self.x+908,self.y+178),Box(self.x+828,self.y+178)]
            self.spikes = [Spike(self.x+599-36,self.y+362),Spike(self.x+908,self.y+258)]

        if(self.var == 20):
            self.inimigos = [Inimigo((self.x+170 , self.y+178 ),2),Inimigo((self.x+170 , self.y+511 ),2)]
            self.interactables = [Box(self.x+908,self.y+178),Box(self.x+908,self.y+258)]
            self.spikes = [Spike(self.x+519-36,self.y+282),Spike(self.x+519-36,self.y+442),Spike(self.x+679-36,self.y+282),Spike(self.x+679-36,self.y+442)]
        
        if(self.var == 21):
            self.inimigos = []
            self.interactables = [Box(self.x+599-36,self.y+362),Box(self.x+519-36,self.y+282),Box(self.x+519-36,self.y+442),Box(self.x+679-36,self.y+282),Box(self.x+679-36,self.y+442)]
            self.spikes = [Spike(self.x+439-36,self.y+202),Spike(self.x+439-36,self.y+522),Spike(self.x+759-36,self.y+202),Spike(self.x+759-36,self.y+522),Spike(self.x+359-36,self.y+202),Spike(self.x+359-36,self.y+522),Spike(self.x+289-36,self.y+202),Spike(self.x+289-36,self.y+522),Spike(self.x+839-36,self.y+202),Spike(self.x+919-36,self.y+202),Spike(self.x+839-36,self.y+522),Spike(self.x+919-36,self.y+522)]
	    

        # BOSS
        if(self.var==30):
            self.bossBattle = BossBattle(self.x,self.y)

        # RENDER DEPOIS
        self.renderFrente = [Sprite('assets/sala/left_passage_southwall.png'), Sprite('assets/sala/right_passage_southwall.png'), Sprite('assets/sala/room_southwall.png'),Sprite('assets/sala/botoom_wal_Nodoorl.png'),Sprite('assets/sala/top_frame.png')]
        
        # POSIÇÕES
        self.renderFrente[0].set_position(0+self.x,405+self.y)
        self.renderFrente[1].set_position(1062+self.x,405+self.y)
        self.renderFrente[2].set_position(138+self.x,594+self.y)
        self.renderFrente[3].set_position(138+self.x,594+self.y)
        self.renderFrente[4].set_position(537+self.x,36+self.y)

        self.col[0].set_position(self.x,self.y)
        self.col[1].set_position(1065+self.x,self.y)
        self.col[2].set_position(138+self.x,self.y)
        self.col[3].set_position(663+self.x,self.y)
        self.col[4].set_position(self.x,444+self.y)
        self.col[5].set_position(1062+self.x,444+self.y)
        self.col[6].set_position(138+self.x,633+self.y)
        self.col[7].set_position(663+self.x,633+self.y)

        for p in self.portas:
            p.set_sequence(20,20,True)

    def SetPortas(self, l):
        if ((self.adress[0],self.adress[1]+1) in l):
            #Tem sala em baixo
            self.portaBaixo = True
        else:
            c = Sprite('assets/sala/bottom_door_placeholder.png')
            c.set_position(555+self.x,633+self.y)
            self.col.append(c)
        if ((self.adress[0],self.adress[1]-1) in l):
            #Tem sala em cima
            self.portaCima = True
        else:
            c = Sprite('assets/sala/top_door_placeholder.png')
            c.set_position(555+self.x,0+self.y)
            self.col.append(c)
        if ((self.adress[0]+1,self.adress[1]) in l):
            #Tem sala na direita
            self.portaDireita = True
        else:
            c = Sprite('assets/sala/side_door_placeholder.png')
            c.set_position(1062+self.x,279+self.y)
            self.col.append(c)
        if ((self.adress[0]-1,self.adress[1]) in l):
            #Tem sala na esquerda
            self.portaEsquerda = True
        else:
            c = Sprite('assets/sala/side_door_placeholder.png')
            c.set_position(0+self.x,279+self.y)
            self.col.append(c)

    def AbrirPortas(self,soundmanager):
        if(not self.abrindoPortas):
            soundmanager.som4()
        self.abrindoPortas = True
        for p in self.portas:
            if p.get_curr_frame() <= 0 or p.get_curr_frame() >= 10:
                p.set_sequence(0,10,True)
            if(p.get_curr_frame()==9):
                self.portasAbertas=True
                self.abrindoPortas=False

    def FecharPortas(self,soundmanager):
        if(not self.abrindoPortas):
            soundmanager.som5()
        self.abrindoPortas = True
        for p in self.portas:
            if p.get_curr_frame() <= 11 or p.get_curr_frame() >= 21:
                p.set_sequence(11,21,True)
            if(p.get_curr_frame()==20):
                self.portasAbertas=False
                self.abrindoPortas=False

    def Mover_X(self, speed):
        self.x += speed
        for i in self.renderFrente:
            i.x += speed
        for i in self.col:
            i.x += speed
        for i in self.passagem:
            i.x += speed
        for i in self.portas:
            i.x += speed

        for i in self.inimigos:
            i.move_x(speed)

        for i in self.interactables:
            i.move_x(speed)

        for i in self.spikes:
            i.move_x(speed)

        if(self.var==30):
            self.bossBattle.move_x(speed)

        self.sprite.set_position(self.x, self.y)

    def Mover_Y(self, speed):
        self.y += speed
        for i in self.renderFrente:
            i.y += speed
        for i in self.col:
            i.y += speed
        for i in self.passagem:
            i.y += speed
        for i in self.portas:
            i.y += speed

        for i in self.inimigos:
            i.move_y(speed)

        for i in self.interactables:
            i.move_y(speed)

        for i in self.spikes:
            i.move_y(speed)
        
        if(self.var==30):
            self.bossBattle.move_y(speed)

        self.sprite.set_position(self.x, self.y)

    def UpdateEntities(self,jogador,janela,soundmanager):
        if(self.var==30):
            self.bossBattle.Update(jogador,janela)

        for i in self.projectiles:
            if(not i.existe):
                self.projectiles.remove(i)
            else:
                i.Update(janela,jogador)

        for i in self.interactables:
            if(i.broken):
                self.interactables.remove(i)

        for i in self.inimigos:
            if(i.var==2):
                if(i.Update(jogador,janela,self.col,self.colPortas)):
                    i.atirou = False
                    self.projectiles.append(Projectile(i.centro_x,i.centro_y,i.dirJogador))
            else:
                i.Update(jogador,janela,self.col,self.colPortas)
            if(not i.vivo):
                self.inimigos.remove(i)
        if(len(self.inimigos)<=0 and not self.var==30):
            self.cleared=True
        if(self.var==30):
            self.cleared = not self.bossBattle.vivo

        if(not self.cleared and self.portasAbertas):
            self.FecharPortas(soundmanager)
        
        if(self.cleared and not self.portasAbertas):
            self.AbrirPortas(soundmanager)

        if(not self.abrindoPortas and self.portasAbertas):
            for p in self.portas:
                if p.get_curr_frame() != 21:
                    p.set_sequence(21,21,True)

        if(not self.abrindoPortas and not self.portasAbertas):
            for p in self.portas:
                if p.get_curr_frame() !=20:
                    p.set_sequence(20,20,True)
            
        if(not self.cleared):
            cp1 = Sprite('assets/portas/bottom_door_placeholder.png')
            cp1.set_position(555+self.x,633+self.y)
            

            cp2 = Sprite('assets/portas/top_door_placeholder.png')
            cp2.set_position(555+self.x,0+self.y)

            cp3 = Sprite('assets/portas/side_door_placeholder.png')
            cp3.set_position(1062+self.x,279+self.y)

            cp4 = Sprite('assets/portas/side_door_placeholder.png')
            cp4.set_position(0+self.x,279+self.y)
            self.colPortas = [cp1,cp2,cp3,cp4]
        if(self.cleared):
            self.colPortas.clear()
            

        # Coloca portas na lista de colisão caso cleared seja falso
        
    def DrawSala(self):
        self.sprite.draw()

        #Desenhar portas caso existam salas adjascentes correspondentes
        if self.portaCima:
            self.passagem[0].draw()
            self.portas[0].draw()
        if self.portaBaixo:
            self.passagem[1].draw()
            self.portas[1].draw()
        if self.portaDireita:
            self.passagem[2].draw()
            self.portas[2].draw()
        if self.portaEsquerda:
            self.passagem[3].draw()
            self.portas[3].draw()
        
        for b in self.interactables:
            b.Draw()
        
        for i in self.spikes:
            i.Draw()

        for i in self.projectiles:
            i.Draw()

        for i in range(len(self.portas)):
            self.portas[i].update()

        if(self.var==30):
            self.bossBattle.Draw()

    def DrawFrenteJogador(self):
        for i in self.inimigos:
            i.Draw()

        if self.portaDireita:
            self.renderFrente[1].draw()

        if self.portaEsquerda:
            self.renderFrente[0].draw()

        if self.portaBaixo:
            self.renderFrente[2].draw()
        else:
            self.renderFrente[3].draw()
        
        if self.portaCima:
            self.renderFrente[4].draw()

    def Delete(self):
        # DELETA A SALA E TUDO ASSOCIADO A ELA
        self.inimigos.clear()
        #self.sprite = Sprite(None)
        self.passagem.clear()
        self.col.clear()