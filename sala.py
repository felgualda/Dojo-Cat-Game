from PPlay.sprite import *

class Sala:
    
    def __init__(self, adress, var, clear):
        
        self.adress = adress

        self.x = self.adress[0] * 1200
        self.y = self.adress[1] * 675

        self.var = var
        self.clear = clear

        self.sprite = Sprite('assets/sala/sala.png')
        self.sprite.set_position(self.x,self.y)
        self.portas = [Sprite('assets/sala/passages/TOP_PASSAGE.png'),Sprite('assets/sala/passages/BOTTOM_PASSAGE.png'),Sprite('assets/sala/passages/RIGHT_PASSAGE.png'),Sprite('assets/sala/passages/LEFT_PASSAGE.png')]
        # PORTAS
        self.portas[0].set_position(546+self.x,0+self.y)
        self.portas[1].set_position(543+self.x,573+self.y)
        self.portas[2].set_position(1038+self.x,273+self.y)
        self.portas[3].set_position(self.x,273+self.y)

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
        

        # RENDER DEPOIS
        self.renderFrente = [Sprite('assets/sala/left_passage_southwall.png'), Sprite('assets/sala/right_passage_southwall.png'), Sprite('assets/sala/room_southwall.png'),Sprite('assets/sala/botoom_wal_Nodoorl.png'),Sprite('assets/sala/top_frame.png')]
        
        # POSIÇÕES
        self.renderFrente[0].set_position(0+self.x,390+self.y)
        self.renderFrente[1].set_position(1062+self.x,390+self.y)
        self.renderFrente[2].set_position(138+self.x,594+self.y)
        self.renderFrente[3].set_position(138+self.x,594+self.y)
        self.renderFrente[4].set_position(555+self.x,36+self.y)

        self.col[0].set_position(self.x,self.y)
        self.col[1].set_position(1065+self.x,self.y)
        self.col[2].set_position(138+self.x,self.y)
        self.col[3].set_position(645+self.x,self.y)
        self.col[4].set_position(self.x,429+self.y)
        self.col[5].set_position(1062+self.x,429+self.y)
        self.col[6].set_position(138+self.x,633+self.y)
        self.col[7].set_position(645+self.x,633+self.y)

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
        self.sprite.set_position(self.x, self.y)

    def Mover_Y(self, speed):
        self.y += speed
        for i in self.renderFrente:
            i.y += speed
        for i in self.col:
            i.y += speed
        for i in self.portas:
            i.y += speed
        self.sprite.set_position(self.x, self.y)

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