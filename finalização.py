from turtle import width
from click import edit
import pygame
from pygame import mixer
from Configurações import ALTURA, DIR_IMG, DIR_SOM,FPS, LARGURA,QUIT,GAME,PRETO
from os import path
import Funções as fun


mixer.init()

def tela_final (janela):

    tempo_fps = pygame.time.Clock()
    plano_fundo = pygame.image.load(path.join(DIR_IMG, 'fim de tarde.png')).convert()
    plano_fundo = pygame.transform.scale(plano_fundo, (LARGURA,ALTURA))
    pdf_rect = plano_fundo.get_rect()
    rodando = True
    
    while rodando:
        tempo_fps.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                estado = QUIT
                rodando = False

            if evento.type == pygame.K_SPACE:
                estado = GAME
                rodando = False
    
        janela.blit(plano_fundo, pdf_rect)

        pygame.display.update()

    return estado