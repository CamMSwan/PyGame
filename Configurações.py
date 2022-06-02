from os import path

import pygame
pygame.init()

DIR_IMG = path.join(path.dirname(__file__), 'imagens')
DIR_SOM = path.join(path.dirname(__file__), 'sons')
DIR_FONT = path.join(path.dirname(__file__), 'fontes')

LARGURA = 1500
ALTURA = 780
FPS = 60 

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

INIC = 0
GAME = 1
QUIT = 2

LARGURA_CORE = 50
ALTURA_CORE = 40


CORE_IMG = 'coracao.png'    
POSICOES_CORE = [(20, 20), (90, 20), (160, 20)]

