from PPlay.sprite import *
from inimigo import *

class Sala:
    
    def __init__(self, adress, var, cleared):
        
        self.adress = adress

        self.x = self.adress[0] * 1200
        self.y = self.adress[1] * 675

        self.var = var
        self.cleared = cleared

        self.sprite = Sprite('assets/sala/sala.png')
        self.sprite.set_position(self.x,self.y)
        self.portas = [Sprite('assets/sala/passages/TOP_PASSAGE.png'),Sprite('assets/sala/passages/BOTTOM_PASSAGE.png'),Sprite('assets/sala/passages/RIGHT_PASSAGE.png'),Sprite('assets/sala/passages/LEFT_PASSAGE.png')]
        # PORTAS
        self.portas[0].set_position(528+self.x,0+self.y)
        self.portas[1].set_position(528+self.x,573+self.y)
        self.portas[2].set_position(1038+self.x,258+self.y)
        self.portas[3].set_position(self.x,258+self.y)

        self.portaDireita = False
        self.portaEsquerda = False
        self.portaCima = False
        self.portaBaixo = False

        # COLISÃO
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


    def Mover_X(self, speed):
        self.x += speed
        for i in self.renderFrente:
            i.x += speed
        for i in self.col:
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
        for i in self.portas:
            i.y += speed

        for i in self.inimigos:
            i.move_y(speed)

        self.sprite.set_position(self.x, self.y)

    def UpdateEntities(self,jogador,janela):
        for i in range(len(self.inimigos)):
            self.inimigos[i].Update(jogador,janela)

    def DrawSala(self):
        self.sprite.draw()

        #Desenhar portas caso existam salas adjascentes correspondentes
        if self.portaCima:
            self.portas[0].draw()
        if self.portaBaixo:
            self.portas[1].draw()
        if self.portaDireita:
            self.portas[2].draw()
        if self.portaEsquerda:
            self.portas[3].draw()

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
        self.portas.clear()
        self.col.clear()