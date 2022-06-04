from turtle import width
from click import edit
import pygame
from pygame import mixer
from Configurações import ALTURA, DIR_IMG, DIR_SOM,FPS, LARGURA,QUIT,GAME,PRETO
from os import path
import Funções as fun

from Elementos import MUSICA_JOGO

pygame.init()
mixer.init()
#Configurações da janela

def tela_inicial(janela):
  
    tempo_fps = pygame.time.Clock()
    plano_de_fundo = pygame.image.load(path.join(DIR_IMG, 'fundo_inicial.jpg')).convert()
    plano_de_fundo = pygame.transform.scale(plano_de_fundo, (LARGURA,ALTURA))
    pdf_rect = plano_de_fundo.get_rect()
    rodando = True
    fonte = pygame.font.SysFont(None, 60)
    titulo = fonte.render('Red Dead Raposa', True, (0,0,0))
    integrante1 =  fonte.render('Nina Schvartsman', True, (0,0,0))
    integrante1 = pygame.transform.scale(integrante1,(400,200))
    integrante2 =  fonte.render('Cameron Swan', True, (0,0,0))
    integrante3 = fonte.render('Mariana Albuquerque', True, (0,0,0))
    musica = path.join(DIR_SOM,MUSICA_JOGO)
    while rodando:
        tempo_fps.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                estado = QUIT
                rodando = False

            if evento.type == pygame.KEYUP:
                estado = GAME
                rodando = False
                
                if estado == GAME:
                    mixer.music.stop()
                    fun.tocar_musica(musica)
        
        janela.fill(PRETO)  
        janela.blit(plano_de_fundo, pdf_rect)
        janela.blit(titulo, (520,300))
        janela.blit(integrante1, (520,400))
        janela.blit(integrante2, (250,30))
        janela.blit(integrante3, (250,70))
        
    

        pygame.display.flip()

    return estado



