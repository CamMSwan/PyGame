from pygame import mixer
def tocar_musica(musica):
    mixer.music.load(musica)
    mixer.music.set_volume(0.7) 
    mixer.music.play(-1)