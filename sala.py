from PPlay.sprite import *

class Sala:
    
    def __init__(self, pos, var, clear):
        
        self.x = pos[0]
        self.y = pos[1]
        #self.paredes = paredes
        self.var = var
        self.clear = clear
        self.sprite = Sprite('assets/sala/sala.png')
        self.sprite.set_position(pos[0],pos[1])

        #colisão
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
        

        #renderizar em frente ao jogador
        self.renderFrente = [Sprite('assets/sala/left_passage_southwall.png'), Sprite('assets/sala/right_passage_southwall.png'), Sprite('assets/sala/room_southwall.png')]
        
        #posições
        self.renderFrente[0].set_position(0+self.x,390+self.y)
        self.renderFrente[1].set_position(1062+self.x,390+self.y)
        self.renderFrente[2].set_position(138+self.x,594+self.y)

        self.col[0].set_position(self.x,self.y)
        self.col[1].set_position(1065+self.x,self.y)
        self.col[2].set_position(138+self.x,self.y)
        self.col[3].set_position(645+self.x,self.y)
        self.col[4].set_position(self.x,429+self.y)
        self.col[5].set_position(1062+self.x,429+self.y)
        self.col[6].set_position(138+self.x,633+self.y)
        self.col[7].set_position(645+self.x,594+self.y)

    def Mover_X(self, speed):
        self.x += speed
        for i in self.renderFrente:
            i.x += speed
        for i in self.col:
            i.x += speed
        self.sprite.set_position(self.x, self.y)

    def Mover_Y(self, speed):
        self.y += speed
        for i in self.renderFrente:
            i.y += speed
        for i in self.col:
            i.y += speed
        self.sprite.set_position(self.x, self.y)

    def DrawSala(self):
        self.sprite.draw()
    
    def DrawFrenteJogador(self):
        for i in range(len(self.renderFrente)):
            self.renderFrente[i].draw()
