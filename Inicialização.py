from turtle import width
from click import edit
import pygame
from Configurações import DIR_IMG,FPS,QUIT,GAME,PRETO
from os import path

pygame.init()

#Configurações da janela

def tela_inicial(janela):
    tempo_fps = pygame.time.Clock()
    plano_de_fundo = pygame.image.load(path.join(DIR_IMG, 'plano3.jpg')).convert()
    plano_de_fundo = pygame.transform.scale(plano_de_fundo, (960,540))
    pdf_rect = plano_de_fundo.get_rect()

    rodando = True
    fonte = pygame.font.SysFont(None, 60)
    text = fonte.render('Duelo Cowboy', True, (0,0,0))

    while rodando:
        tempo_fps.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                estado = QUIT
                rodando = False

            if evento.type == pygame.KEYUP:
                estado = GAME
                rodando = False

        janela.fill(PRETO)  
        janela.blit(plano_de_fundo, pdf_rect)
        janela.blit(text, (400,150))


        pygame.display.flip()

    return estado



