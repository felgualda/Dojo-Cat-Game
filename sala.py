from PPlay.sprite import *
from inimigo import *

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
        self.abrindoPortas = True

        self.passagem[0].set_position(528+self.x,0+self.y)
        self.passagem[1].set_position(528+self.x,573+self.y)
        self.passagem[2].set_position(1038+self.x,258+self.y)
        self.passagem[3].set_position(self.x,258+self.y)

        self.portas[0].set_position(537+self.x,81+self.y)
        self.portas[0].set_sequence_time(0,21,30,True)
        
        self.portas[1].set_position(537+self.x,594+self.y)
        self.portas[1].set_sequence_time(0,21,30,True)

        self.portas[2].set_position(1062+self.x,267+self.y)
        self.portas[2].set_sequence_time(0,21,30,True)

        self.portas[3].set_position(123+self.x,267+self.y)
        self.portas[3].set_sequence_time(0,21,30,True)

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
        if(self.var == 1):
            self.inimigos = [Inimigo((self.x + 1200/2, self.y + 675/2),1)]
        

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

    def AbrirPortas(self):
        self.abrindoPortas = True
        for p in self.portas:
            if p.get_curr_frame() <= 0 or p.get_curr_frame() >= 10:
                p.set_sequence(0,10,True)
            if(p.get_curr_frame()==9):
                self.portasAbertas=True
                self.abrindoPortas=False

    def FecharPortas(self):
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

        self.sprite.set_position(self.x, self.y)

    def UpdateEntities(self,jogador,janela):
        for i in self.inimigos:
            i.Update(jogador,janela)
            if(not i.vivo):
                self.inimigos.remove(i)
        if(len(self.inimigos)<=0):
            self.cleared=True

        if(not self.cleared and self.portasAbertas):
            self.FecharPortas()
        
        if(self.cleared and not self.portasAbertas):
            self.AbrirPortas()

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

        for p in self.portas:
            p.update()

    def DrawFrenteJogador(self):
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

        for i in self.inimigos:
            i.Draw()

    def Delete(self):
        # DELETA A SALA E TUDO ASSOCIADO A ELA
        self.inimigos.clear()
        #self.sprite = Sprite(None)
        self.passagem.clear()
        self.col.clear()