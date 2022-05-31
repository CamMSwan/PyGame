import pygame
from Classes import Player1, Player2
from Configurações import DIR_IMG,FPS,QUIT,GAME,PRETO
from os import path
import Elementos as El


def gameplay(janela):
    tempo_fps = pygame.time.Clock()
    plano_jogo = pygame.image.load(path.join(DIR_IMG, 'fundo2.png')).convert()
    plano_jogo = pygame.transform.scale(plano_jogo, (960,540))
    elementos = El.carregar_elementos()
    todos_sprites = pygame.sprite.Group()
    grupo = {}
    grupo['todos_sprites'] = todos_sprites
    
    jogador1 = Player1(grupo,elementos)
    jogador2 = Player2(grupo,elementos)
    todos_sprites.add(jogador2)
    todos_sprites.add(jogador1)
    
    for i in range(8):
        machado = Meteor(assets)
        all_sprites.add(meteor)
        all_meteors.add(meteor)
    
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
        janela.blit(plano_jogo, (0, 0))
        todos_sprites.draw(janela)
        pygame.display.update()
        pygame.quit()

    while rodando:
        tempo_fps.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jogador1.speedx -= 8
                if event.key == pygame.K_RIGHT:
                    jogador1.speedx += 8
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    jogador1.speedx += 8
                if event.key == pygame.K_RIGHT:
                    jogador1.speedx -= 8
    
    pygame.display.flip()

    return estado

