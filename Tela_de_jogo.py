import pygame
from Classes import player1, player2
from Configurações import DIR_IMG,FPS,QUIT,GAME,PRETO
from os import path
import Elementos as El

def gameplay(janela):
    tempo_fps = pygame.time.Clock()
    
    elementos = El.carregar_elementos()
    todos_sprites = pygame.sprite.Group()
    grupo = {}
    grupo['todos_sprites'] = todos_sprites
    
    jogador1 = player1(grupo,elementos)
    jogador2 = player2(grupo,elementos)
    
    
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
        janela.draw(jogador1)
        janela.draw(jogador2)

    while rodando:
        tempo_fps.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jogador1.speedx += 8
                if event.key == pygame.K_RIGHT:
                    jogador1.speedx += 8
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    jogador1.speedx += 8
                if event.key == pygame.K_RIGHT:
                    jogador1.speedx += 8
    pygame.display.flip()

    return estado
