import pygame
import os
from Configurações import DIR_IMG, DIR_SOM, DIR_FONT, LARGURA

FOX_IMG = 'imagem_humberto.png'
LARGURA_FOX = 85
ALTURA_FOX = 100

def carregar_elementos():
    elementos = {}
    elementos[FOX_IMG] = pygame.image.load(os.path.join(DIR_IMG, 'imagem_humberto.png')).convert_alpha()
    elementos[FOX_IMG] = pygame.transform.scale(elementos['imagem_humberto.png'], (LARGURA_FOX, ALTURA_FOX))
    return elementos