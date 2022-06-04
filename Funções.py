from pygame import mixer
import pygame
from Configurações import DIR_IMG, CORE_IMG,LARGURA_CORE,ALTURA_CORE
from os import path

def tocar_musica(musica,tempo):
    mixer.music.load(musica)
    mixer.music.set_volume(0.7) 
    mixer.music.play(tempo)
    
    

