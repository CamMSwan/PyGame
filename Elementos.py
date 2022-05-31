import pygame
import os
from Configurações import DIR_IMG, DIR_SOM, DIR_FONT, LARGURA

FOX_IMG = 'imagem2.png'
LARGURA_FOX = 85
ALTURA_FOX = 100

DOUTOR_IMG = 'imagem_resina.png'
LARGURA_DR = 85
ALTURA_DR = 100

PLANO_DE_FUNDO = 'fundo2.png'
MENU = 'fundo1.png'

MACHADO = 'Animação machado'
machado_anim = []

def carregar_elementos():
    elementos = {}
    elementos[FOX_IMG] = pygame.image.load(os.path.join(DIR_IMG, 'imagem2.png')).convert_alpha()
    elementos[FOX_IMG] = pygame.transform.scale(elementos['imagem2.png'], (LARGURA_FOX, ALTURA_FOX))
    elementos[DOUTOR_IMG] = pygame.image.load(os.path.join(DIR_IMG, 'imagem_resina.png')).convert_alpha()
    elementos[DOUTOR_IMG] = pygame.transform.scale(elementos['imagem_resina.png'], (LARGURA_DR, ALTURA_DR))
    '''for i in range(4):
        arquivo = os.path.join(DIR_IMG,MACHADO, 'axe-1{}.png'.format(i))
        img = pygame.image.load(arquivo).convert()
        img = pygame.transform.scale(img, (32, 32))
        machado_anim.append(img)
    elementos[MACHADO] = machado_anim'''
    return elementos