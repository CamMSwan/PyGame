import pygame
from Classes import carinha
from Configurações import DIR_IMG,FPS,QUIT,GAME,PRETO
from os import path
import Elementos as El

def gameplay(janela):
    tempo_fps = pygame.time.Clock()

    elementos = El.carregar_elementos()
    todos_sprites = pygame.sprite.Group()
    groups = {}
    groups['todos_sprites'] = todos_sprites
    
    player = carinha(groups, elementos)
    todos_sprites.add(player)
    
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
        todos_sprites.update()
        janela.fill(PRETO)  
        todos_sprites.draw(janela)
        pygame.display.flip()

    return estado
