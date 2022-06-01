from os import path

import pygame

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

'''largura_coracao = 70
altura_coracao = 60

'''CORE_IMG = pygame.image.load('imagens/coracao.png').convert_alpha()
CORE_2 = CORE_IMG
CORE_3 = CORE_IMG

#----------------Pontos e vidas
coracoes = [CORE_IMG,CORE_2, CORE_3]
pontos_coracoes = [(20, 20), (90, 20), (160, 20)]'''