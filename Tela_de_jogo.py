import pygame
from Classes import Machado, Morte, Player1, Player2
from Configurações import ALTURA, ALTURA_CORE, BRANCO, CORE_IMG, DIR_IMG, DIR_SOM,FPS, GAME_OVER, LARGURA, LARGURA_CORE, POSICOES_CORE1, POSICOES_CORE2,QUIT,GAME,PRETO, VERMELHO
from os import path
from Elementos import DIR_IMG, SOM_DANO
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
    som_dano = path.join(DIR_SOM,SOM_DANO)
    
    jogador1 = Player1(grupo)
    jogador2 = Player2(grupo)
    todos_sprites.add(jogador2)
    todos_sprites.add(jogador1)
    
    dano1 = pygame.sprite.collide_rect(machado,jogador1)
    dano2 = pygame.sprite.collide_rect(machado,jogador2)
        
    vidas1 = 3
    vidas2 = 3
    
    tecla = {}

    
    
    rodando = GAME
    while rodando != GAME_OVER:
        tempo_fps.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if rodando == GAME:
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
                                
        dano1 = pygame.sprite.collide_rect(machado,jogador1)
        dano2 = pygame.sprite.collide_rect(machado,jogador2)        
                        
        if dano1:
            machado.rect.top = ALTURA
            vidas1 -= 1
            fun.tocar_som(som_dano)
            if vidas1 == 0:
                jogador1.kill()
                #morte = Morte(jogador1.rect.x,grupo)
                #todos_sprites.add(morte)
                rodando = GAME_OVER
                
                        
           
        if dano2:
            machado.rect.top = ALTURA
            vidas2 -= 1
            fun.tocar_som(som_dano)
            if vidas2 == 0:
                jogador2.kill()
                #morte = Morte(jogador2.rect.x,grupo)
                #todos_sprites.add(morte)
                rodando = GAME_OVER
                
                        
                        

           
        
        todos_sprites.update()
        
        janela.fill(BRANCO)  
        janela.blit(plano_jogo, (0, 0))
        todos_sprites.draw(janela)
        
    
        coracao = pygame.image.load(path.join(DIR_IMG, CORE_IMG)).convert_alpha()
        coracao = pygame.transform.scale(coracao, (LARGURA_CORE,ALTURA_CORE))
        if vidas2 >= 1:
            janela.blit(coracao, POSICOES_CORE1[0])
            if vidas2 >= 2:
                janela.blit(coracao, POSICOES_CORE1[1])
                if vidas2 == 3:
                    janela.blit(coracao, POSICOES_CORE1[2])
        
        if vidas1 >=1:
            janela.blit(coracao, POSICOES_CORE2[2])
            if vidas1 >= 2:
                janela.blit(coracao, POSICOES_CORE2[1])
                if vidas1 == 3:
                    janela.blit(coracao, POSICOES_CORE2[0])
        
        
        
        
        pygame.display.update()

    
    

    return rodando
        
    

  

