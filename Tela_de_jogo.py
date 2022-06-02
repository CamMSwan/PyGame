import pygame
from Classes import Machado, Player1, Player2
from Configurações import ALTURA, ALTURA_CORE, BRANCO, CORE_IMG, DIR_IMG, DIR_SOM,FPS, LARGURA, LARGURA_CORE, POSICOES_CORE,QUIT,GAME,PRETO, VERMELHO
from os import path
from Elementos import DIR_IMG
import Funções as fun

def gameplay(janela):
    tempo_fps = pygame.time.Clock()
    plano_jogo = pygame.image.load(path.join(DIR_IMG, 'fundo_jogo.png')).convert()
    plano_jogo = pygame.transform.scale(plano_jogo, (LARGURA,ALTURA))
    todos_sprites = pygame.sprite.Group()
    grupo = {}
    grupo['todos_sprites'] = todos_sprites
    
    machado = Machado()
    todos_sprites.add(machado)
    
    
    jogador1 = Player1(grupo)
    jogador2 = Player2(grupo)
    todos_sprites.add(jogador2)
    todos_sprites.add(jogador1)
        
    vidas = 2
    
    tecla = {}
    ACABOU = 0
    JOGANDO = 1
    MORTO = 2
    
    rodando = JOGANDO
    while rodando != ACABOU:
        tempo_fps.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
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
        
        '''tile_map = [
            '.................................................',
            '.................................................',
            '.................................................',
            '.................................................',
            '............XXXXXXXXXX........XXXXXXXXXXX........',
            '.................................................',
            '.................................................',
            '.................................................']'''
        
        todos_sprites.update()
        
        janela.fill(BRANCO)  
        janela.blit(plano_jogo, (0, 0))
        todos_sprites.draw(janela)
        
        '''for i in range(0,vidas):
            coracoes = [0]*vidas
            coracao = pygame.image.load(path.join(DIR_IMG, CORE_IMG)).convert_alpha()
            coracao = pygame.transform.scale(coracao, (LARGURA_CORE,ALTURA_CORE))
            coracoes[i] = coracao
            janela.blit(coracoes[i],POSICOES_CORE[i])   '''
            
        coracao = pygame.image.load(path.join(DIR_IMG, CORE_IMG)).convert_alpha()
        coracao = pygame.transform.scale(coracao, (LARGURA_CORE,ALTURA_CORE))
        if vidas >= 1:
            janela.blit(coracao, POSICOES_CORE[0])
            if vidas >= 2:
                janela.blit(coracao, POSICOES_CORE[1])
                if vidas == 3:
                    janela.blit(coracao, POSICOES_CORE[2])
        
        
        
        pygame.display.update()

  

