'''Importa os elementos e pacotes necessários'''
import pygame
from Classes import Plataforma, Player1, Player2
from Configurações import ALTURA, ALTURA_CORE, CORE_IMG, DIR_IMG, DIR_SOM, DT,FPS, GAME_OVER, LARGURA, LARGURA_CORE, POSICOES_CORE1, POSICOES_CORE2, PRETO,QUIT,GAME, VITORIA1, VITORIA2
from os import path
from Elementos import ALTURA_POS_P, MUSICA_FINAL, SOM_DANO
import Musicas as mus

'''Função de tela inicial que recebe a tela com as dimensões usadas'''
def gameplay(janela):
    
    '''Variavel de ajuste da tempo'''
    tempo_fps = pygame.time.Clock()
    '''Carrega os elementos pro plano de fundo'''
    plano_jogo = pygame.image.load(path.join(DIR_IMG, 'fundo_jogo.png')).convert()
    plano_jogo = pygame.transform.scale(plano_jogo, (LARGURA,ALTURA))
    
    '''Cria grupos dos sprites'''
    todos_sprites = pygame.sprite.Group()
    todas_balas = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()
    jogadores = pygame.sprite.Group()
    explosoes = pygame.sprite.Group()
    dinamites = pygame.sprite.Group()
    
    '''Dicionario para guardar grupos'''
    grupo = {}
    grupo['todos_sprites'] = todos_sprites
    grupo['todas_balas'] = todas_balas
    grupo['Plataformas'] = plataformas
    grupo['explosoes'] = explosoes
    grupo['dinamites'] = dinamites
    
    '''Som de quando tomar dano'''
    som_dano = path.join(DIR_SOM,SOM_DANO)
    
    '''Carrega plataformas'''
    plataforma1 = Plataforma(1000,ALTURA_POS_P)
    plataforma2 = Plataforma(400,ALTURA_POS_P)
    todos_sprites.add(plataforma1)
    todos_sprites.add(plataforma2)
    plataformas.add(plataforma1)
    plataformas.add(plataforma2)
    
    '''carrega jogadores'''
    jogador1 = Player1(grupo)
    jogador2 = Player2(grupo)
    todos_sprites.add(jogador2)
    todos_sprites.add(jogador1)
    jogadores.add(jogador1)
    jogadores.add(jogador2)

    '''Define direção inicial dos jogadores'''
    direcao1 = 'E'
    direcao2 = 'D'
    
    '''Quntidade de vidas de cada jogador'''
    vidas1 = 3
    vidas2 = 3
    
    '''Condição para ficar em cima da plataforma'''
    encima1 = True
    encima2 = True
    
    '''Dicionario para armazenar telcas usadas'''
    tecla = {}

    '''Variavel para armazenar o ganhador'''
    vitoria = 0
    
    '''Loop principal'''
    rodando = GAME
    while rodando != GAME_OVER and rodando != QUIT:
        '''Velocidade da tela'''
        tempo_fps.tick(FPS)
        
        '''Verifica eventos'''
        for evento in pygame.event.get():
            
            '''Se fechou a tela'''
            if evento.type == pygame.QUIT:
                rodando = QUIT

            '''Se tiver rodando'''
            if rodando == GAME:
                    '''Verifica se apertou alguma tecla.'''
                    if evento.type == pygame.KEYDOWN: 
                        '''Comandos jogador 1
                             Dependendo da tecla...'''
                        tecla[evento.key] = True
                        
                        '''Movimenta para a esquerda'''
                        if evento.key == pygame.K_LEFT:
                            jogador1.speedx -= 8*DT
                            direcao1 = 'E'
                            
                        '''Movimenta para a direita'''
                        if evento.key == pygame.K_RIGHT:
                            jogador1.speedx += 8*DT
                            direcao1 = 'D'
                        
                        '''Pula'''
                        if evento.key == pygame.K_UP:
                            jogador1.jump()
                        
                        '''Desce da plataforma'''
                        if evento.key == pygame.K_DOWN:
                            encima1 = False
                        
                        '''Atira para a direção do jogador 1'''
                        if evento.key == pygame.K_SLASH:
                            if direcao1 == 'D':
                                jogador1.atirarD()
                            if direcao1 == 'E':
                                jogador1.atirarE()
                        
                        '''Joga dinamite para a direção do jogador 1'''
                        if evento.key == pygame.K_PERIOD:
                            if direcao1 == 'D':
                                jogador1.especialD()
                            if direcao1 == 'E':
                                jogador1.especialE()
                            
                    '''Verifica se soltou a tecla'''      
                    if evento.type == pygame.KEYUP:
                        if evento.key in tecla and tecla[evento.key]:
                            if evento.key == pygame.K_LEFT:
                                jogador1.speedx += 8*DT
                                
                            if evento.key == pygame.K_RIGHT:
                                jogador1.speedx -= 8*DT
                                    
                            if evento.key == pygame.K_DOWN:
                                encima1 = True
                    
                    '''Comandos jogador 2:
                            Dependendo da tecla...'''           
                    if evento.type == pygame.KEYDOWN: 
                        tecla[evento.key] = True
                        
                        '''Movimenta para a esquerda'''
                        if evento.key == pygame.K_a:
                            jogador2.speedx -= 8*DT
                            direcao2 = 'E'
                            
                        '''Movimenta para a direita'''
                        if evento.key == pygame.K_d:
                            jogador2.speedx += 8*DT
                            direcao2 = 'D'
                            
                        '''Pula'''
                        if evento.key == pygame.K_w:
                            jogador2.jump()
                            
                        '''Desce da plataforma'''
                        if evento.key == pygame.K_s:
                                encima2 = False
                                
                        '''Atira para a direção do jogador 1'''
                        if evento.key == pygame.K_q:
                            if direcao2 == 'D':
                                jogador2.atirarD()
                            if direcao2 == 'E':
                                jogador2.atirarE()
                                
                        '''Joga dinamite para a direção do jogador 1'''
                        if evento.key == pygame.K_1:
                            if direcao2 == 'D':
                                jogador2.especialD()
                            if direcao2 == 'E':
                                jogador2.especialE()
                            
                    '''Verifica se soltou a tecla'''               
                    if evento.type == pygame.KEYUP:
                        if evento.key in tecla and tecla[evento.key]:
                            if evento.key == pygame.K_a:
                                jogador2.speedx += 8*DT
                            if evento.key == pygame.K_d:
                                jogador2.speedx -= 8*DT
                            if evento.key == pygame.K_s:
                                encima2 = True
         
        
        '''Detecta colisão dos tiros com jogador'''
        dano_tiro1 = pygame.sprite.spritecollide(jogador1, todas_balas, True) 
        if dano_tiro1:
            mus.tocar_som(som_dano)
            vidas1 -= 1
        dano_tiro2 = pygame.sprite.spritecollide(jogador2, todas_balas, True, pygame.sprite.collide_mask)
        if dano_tiro2:
            mus.tocar_som(som_dano)
            vidas2 -= 1
                                
        '''Detecta colisao da explosao com o jogador'''                        
        dano_explo1 = pygame.sprite.spritecollide(jogador1, explosoes, False, pygame.sprite.collide_mask)
        if dano_explo1:
            vidas1 = 0
        dano_explo2 = pygame.sprite.spritecollide(jogador2, explosoes, False, pygame.sprite.collide_mask)
        if dano_explo2:
            vidas2 = 0
          
        '''Verifica se algum jogador morreu'''  
        if vidas1 == 0:
                jogador1.kill()
                rodando = GAME_OVER
                vitoria = VITORIA2        
        if vidas2 == 0:
                jogador2.kill()
                rodando = GAME_OVER
                vitoria = VITORIA1
        
        '''Verifica colisao da plataforma com o jogador 1'''
        plat1 = pygame.sprite.spritecollide(jogador1, plataformas, False, pygame.sprite.collide_mask)    
        if jogador1.speedy > 0 and plat1 and encima1:
            for plataforma in plataformas:
                jogador1.collide(plataforma.rect) 
                      
        '''Verifica colisao da plataforma com jogador 2'''            
        plat2 = pygame.sprite.spritecollide(jogador2, plataformas, False, pygame.sprite.collide_mask)    
        if jogador2.speedy > 0 and plat2 and encima2:
            for plataforma in plataformas:
                jogador2.collide(plataforma.rect)
                
        '''Atualiza Sprites'''   
        todos_sprites.update()
        
        '''Cria tela de jogo e spawna sprites'''
        janela.fill(PRETO)  
        janela.blit(plano_jogo, (0, 0))
        todos_sprites.draw(janela)
        
        '''Desenha as vidas de cada jogador'''
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
        
        '''Atualiza a tela'''
        pygame.display.update()

    '''Musica da proxima tela (FINAL)'''
    musica = path.join(DIR_SOM,MUSICA_FINAL)
    mus.tocar_musica(musica)

    '''Retorna lista com estado do jogo e o ganhador se tiver'''
    lista_gameplay = [rodando,vitoria]
    return lista_gameplay