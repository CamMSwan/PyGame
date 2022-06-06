from os import path

import pygame
pygame.init()

DIR_IMG = path.join(path.dirname(__file__), 'imagens')
DIR_SOM = path.join(path.dirname(__file__), 'sons')
DIR_FONT = path.join(path.dirname(__file__), 'fontes')

LARGURA = 1400
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
GAME_OVER = 2
QUIT = 3

LARGURA_CORE = 50
ALTURA_CORE = 40


CORE_IMG = 'coracao.png'    
POSICOES_CORE1 = [(20, 20), (90, 20), (160, 20)]
POSICOES_CORE2 = [(LARGURA - 210, 20), (LARGURA - 140, 20), (LARGURA - 70, 20)]

VITORIA1 = 1
VITORIA2 = 2