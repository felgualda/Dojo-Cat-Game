from pygame import mixer

class AudioManager():
    def __init__(self) -> None:
        pass

    def som1(self):
        somataquecerto = mixer.Sound('audio/espadadacerta.mp3')
        somataquecerto.set_volume(0.3)
        somataquecerto.play()

    def som2(self):
        somataqueerrado = mixer.Sound('audio/espadadaerrada.mp3')
        somataqueerrado.set_volume(0.3)
        somataqueerrado.play()

    def som4(self):
        somportaabrindo = mixer
        somportaabrindo.music.load('audio/portaabrindo.mp3')
        somportaabrindo.music.set_volume(0.2)
        somportaabrindo.music.play()

    def som5(self):
        somportafechando = mixer
        somportafechando.music.load('audio/portafechando.mp3')
        somportafechando.music.set_volume(0.2)
        somportafechando.music.play()