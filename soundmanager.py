from pygame import mixer

class AudioManager():
    def __init__(self) -> None:
        pass

    def som1(self): # Som da katana batendo no inimigo:
        somataquecerto = mixer.Sound('audio/espadadacerta.mp3')
        somataquecerto.set_volume(0.3)
        somataquecerto.play()

    def som2(self): # Som da katana no vento:
        somataqueerrado = mixer.Sound('audio/espadadaerrada.mp3')
        somataqueerrado.set_volume(0.2)
        somataqueerrado.play()

    def som4(self): # Som da abertura das portas
        somportaabrindo = mixer
        somportaabrindo.music.load('audio/portaabrindo.mp3')
        somportaabrindo.music.set_volume(0.3)
        somportaabrindo.music.play()

    def som5(self): # Som do fechamento das portas
        somportafechando = mixer
        somportafechando.music.load('audio/portafechando.mp3')
        somportafechando.music.set_volume(0.3)
        somportafechando.music.play()
    
    def som6(self): # Som da caixa quebrando:
        somcaixa = mixer.Sound('audio/caixa.mp3')
        somcaixa.set_volume(0.3)
        somcaixa.play()

    def som7(self): # Som do inimigo dando facada no jogador:
        somfacadarecruta = mixer.Sound('audio/facadarecruta.mp3')
        somfacadarecruta.set_volume(0.15)
        somfacadarecruta.play()

    def som8(self): # Som de dano no gato:
        somdanonogato = mixer.Sound('audio/danonogato.mp3')
        somdanonogato.set_volume(0.3)
        somdanonogato.play()

    def som9(self): # Som do inimigo dando flechada no jogador:
        somflechada = mixer.Sound('audio/flechada.mp3')
        somflechada.set_volume(0.15)
        somflechada.play()

    def som10(self): # Som de pegar item:
        sompegaitem = mixer.Sound('audio/pegaitem.mp3')
        sompegaitem.set_volume(0.15)
        sompegaitem.play()

    def som11(self): # Som de clique
        somclique = mixer.Sound('audio/clique.mp3')
        somclique.set_volume(0.1)
        somclique.play()

    def som12(self):
        somwin = mixer.Sound('audio/vitoria.mp3')
        somwin.set_volume(0.3)
        somwin.play()

    def som13(self):
        somlose = mixer.Sound('audio/derrota.mp3')
        somlose.set_volume(0.3)
        somlose.play()


    

