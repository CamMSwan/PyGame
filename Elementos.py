import pygame
import os
from Configurações import DIR_IMG, DIR_SOM, DIR_FONT, LARGURA

FOX_IMG = 'imagem_humberto.png'
LARGURA_FOX = 85
ALTURA_FOX = 100

DOUTOR_IMG = 'imagem_resina.png'
LARGURA_DR = 85
ALTURA_DR = 100


def carregar_elementos():
    elementos = {}
    elementos[FOX_IMG] = pygame.image.load(os.path.join(DIR_IMG, 'imagem_humberto.png')).convert_alpha()
    elementos[FOX_IMG] = pygame.transform.scale(elementos['imagem_humberto.png'], (LARGURA_FOX, ALTURA_FOX))
    elementos[DOUTOR_IMG] = pygame.image.load(os.path.join(DIR_IMG, 'imagem_resina.png')).convert_alpha()
    elementos[DOUTOR_IMG] = pygame.transform.scale(elementos['imagem_resina.png'], (LARGURA_DR, ALTURA_DR))
    return elementos