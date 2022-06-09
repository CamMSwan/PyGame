'''Funções para tocar as musicas e sons'''

from pygame import mixer

'''Musicas de fundo'''
def tocar_musica(musica):
    mixer.music.load(musica)
    mixer.music.set_volume(0.7) 
    mixer.music.play(-1)

'''Sons de acontecimentos'''
def tocar_som(som):
    s = mixer.Sound(som)
    mixer.Sound.play(s)


