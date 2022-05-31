import pygame
import os
from Configurações import DIR_IMG, DIR_SOM, DIR_FONT, LARGURA

FOX_IMG = 'raposa.png'
LARGURA_FOX = 150
ALTURA_FOX = 165

DOUTOR_IMG = 'imagem_resina.png'
LARGURA_DR = 150
ALTURA_DR = 165

PLANO_DE_FUNDO = 'fundo2.png'
MENU = 'fundo1.png'

MACHADO = 'Animação machado'
LARGURA_M = 32
ALTURA_M = 32
machado_anim = []

def carregar_elementos():
    elementos = {}
    elementos[FOX_IMG] = pygame.image.load(os.path.join(DIR_IMG, 'raposa.png')).convert_alpha()
    elementos[FOX_IMG] = pygame.transform.scale(elementos['raposa.png'], (LARGURA_FOX, ALTURA_FOX))
    elementos[DOUTOR_IMG] = pygame.image.load(os.path.join(DIR_IMG, 'imagem_resina.png')).convert_alpha()
    elementos[DOUTOR_IMG] = pygame.transform.scale(elementos['imagem_resina.png'], (LARGURA_DR, ALTURA_DR))
    i = 1
    while i < 5:
        arquivo = os.path.join(DIR_IMG,MACHADO, 'axe-{}.png'.format(i))
        img = pygame.image.load(arquivo).convert()
        img = pygame.transform.scale(img, (32, 32))
        machado_anim.append(img)
        i += 1
    elementos[MACHADO] = machado_anim
    return elementos

