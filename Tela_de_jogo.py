from pickle import TRUE
import pygame
from Classes import Machado, Player1, Player2
from Configurações import BRANCO, DIR_IMG,FPS,QUIT,GAME,PRETO
from os import path
import Elementos as El


def gameplay(janela):
    tempo_fps = pygame.time.Clock()
    plano_jogo = pygame.image.load(path.join(DIR_IMG, 'fundo_jogo.png')).convert()
    plano_jogo = pygame.transform.scale(plano_jogo, (960,540))
    todos_sprites = pygame.sprite.Group()
    grupo = {}
    grupo['todos_sprites'] = todos_sprites
    
    machado = Machado()
    todos_sprites.add(machado)
    
        
    jogador1 = Player1(grupo)
    jogador2 = Player2(grupo)
    todos_sprites.add(jogador2)
    todos_sprites.add(jogador1)
        
    tecla = {}
    ACABOU = 0
    JOGANDO = 1
    MORTO = 2
    
    rodando = JOGANDO
    while rodando != ACABOU:
        tempo_fps.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                estado = QUIT
                rodando = False

            if evento.type == pygame.KEYUP:
                estado = GAME
                rodando = False
            if rodando == JOGANDO:
                    # Verifica se apertou alguma tecla.
                    if evento.type == pygame.KEYDOWN: #Comandos JOGADOR 1
                        # Dependendo da tecla, altera a velocidade.
                        tecla[evento.key] = True
                        if evento.key == pygame.K_LEFT:
                            jogador1.speedx -= 8
                        if evento.key == pygame.K_RIGHT:
                            jogador1.speedx += 8
                        if evento.key == pygame.K_UP:
                            jogador1.jumping
                    if evento.type == pygame.KEYUP:
                        if evento.key in tecla and tecla[evento.key]:
                            if evento.key == pygame.K_LEFT:
                                jogador1.speedx += 8
                            if evento.key == pygame.K_RIGHT:
                                jogador1.speedx -= 8

                    if evento.type == pygame.KEYDOWN: #Comandos JOGADOR 2
                        tecla[evento.key] = True
                        if evento.key == pygame.K_a:
                            jogador2.speedx -= 8
                        if evento.key == pygame.K_d:
                            jogador2.speedx += 8
                        if evento.key == pygame.K_w:
                            jogador2.jumping
                    if evento.type == pygame.KEYUP:
                        if evento.key in tecla and tecla[evento.key]:
                            if evento.key == pygame.K_a:
                                jogador2.speedx += 8
                            if evento.key == pygame.K_d:
                                jogador2.speedx -= 8
            
        todos_sprites.update()
        janela.fill(BRANCO)  
        janela.blit(plano_jogo, (0, 0))
        todos_sprites.draw(janela)
        pygame.display.update()

    return estado

