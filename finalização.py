from turtle import width
from click import edit
import pygame
from pygame import mixer
from Configurações import ALTURA, DIR_IMG, DIR_SOM,FPS, LARGURA,QUIT,GAME,GAME_OVER
from os import path
import Funções as fun
from Elementos import  MUSICA_JOGO


mixer.init()

def tela_final (janela):

    musica = path.join(DIR_SOM,MUSICA_JOGO)
    tempo_fps = pygame.time.Clock()
    plano_fundo = pygame.image.load(path.join(DIR_IMG, 'fim de tarde.png')).convert()
    plano_fundo = pygame.transform.scale(plano_fundo, (LARGURA,ALTURA))
    pdf_rect = plano_fundo.get_rect()
    rodando = GAME_OVER
    while rodando == GAME_OVER:
        tempo_fps.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = QUIT
                

            if evento.type == pygame.K_SPACE:
                rodando = GAME
                mixer.music.stop()
                fun.tocar_musica(musica)
                
    
        janela.blit(plano_fundo, pdf_rect)

        pygame.display.update()

    return rodando