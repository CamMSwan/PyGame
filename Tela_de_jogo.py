import pygame
from Configurações import DIR_IMG,FPS,QUIT,GAME,PRETO
from os import path

def gameplay(janela):
    tempo_fps = pygame.time.Clock()
    
    rodando = True
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

        pygame.display.flip()

    return estado