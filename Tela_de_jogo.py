import pygame
from Classes import Dinamite, Explosao, Machado, Plataforma, Player1, Player2
from Configurações import ALTURA, ALTURA_CORE, BRANCO, CORE_IMG, DIR_IMG, DIR_SOM, DT,FPS, GAME_OVER, LARGURA, LARGURA_CORE, POSICOES_CORE1, POSICOES_CORE2,QUIT,GAME, VITORIA1, VITORIA2
from os import path
from Elementos import ALTURA_POS_P, ANIM_DINAMITE_D, ANIM_DINAMITE_E, BOOM, CHAO, DINAMITE_LOGO, DIR_IMG, MUSICA_FINAL, SOM_DANO
import Funções as fun


def gameplay(janela):
    
    tempo_fps = pygame.time.Clock()
    plano_jogo = pygame.image.load(path.join(DIR_IMG, 'fundo_jogo.png')).convert()
    plano_jogo = pygame.transform.scale(plano_jogo, (LARGURA,ALTURA))
    todos_sprites = pygame.sprite.Group()
    todas_balas = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()
    jogadores = pygame.sprite.Group()
    machados = pygame.sprite.Group()
    explosoes = pygame.sprite.Group()
    dinamites = pygame.sprite.Group()
    grupo = {}
    grupo['todos_sprites'] = todos_sprites
    grupo['todas_balas'] = todas_balas
    grupo['Machados'] = machados
    grupo['Plataformas'] = plataformas
    grupo['explosoes'] = explosoes
    grupo['dinamites'] = dinamites
    
    '''machado = Machado()
    todos_sprites.add(machado)
    machados.add(machado)'''
    som_dano = path.join(DIR_SOM,SOM_DANO)
    
    plataforma1 = Plataforma(1000,ALTURA_POS_P)
    plataforma2 = Plataforma(400,ALTURA_POS_P)
    todos_sprites.add(plataforma1)
    todos_sprites.add(plataforma2)
    plataformas.add(plataforma1)
    plataformas.add(plataforma2)
    
    jogador1 = Player1(grupo)
    jogador2 = Player2(grupo)
    direcao1 = 'E'
    direcao2 = 'D'
    
    todos_sprites.add(jogador2)
    todos_sprites.add(jogador1)
    jogadores.add(jogador1)
    jogadores.add(jogador2)

    vidas1 = 3
    vidas2 = 3
    
    encima1 = True
    encima2 = True
    
    
    tecla = {}

    vitoria = 0
    
    rodando = GAME
    while rodando != GAME_OVER and rodando != QUIT:
        tempo_fps.tick(FPS)
        plat1 = pygame.sprite.spritecollide(jogador1, todas_balas, True, pygame.sprite.collide_mask)
        for evento in pygame.event.get():
            
            if evento.type == pygame.QUIT:
                rodando = QUIT

            if rodando == GAME:
                    # Verifica se apertou alguma tecla.
                    if evento.type == pygame.KEYDOWN: #Comandos JOGADOR 1
                        # Dependendo da tecla, altera a velocidade.
                        tecla[evento.key] = True
                        if evento.key == pygame.K_LEFT:
                            jogador1.speedx -= 8*DT
                            direcao1 = 'E'
                        if evento.key == pygame.K_RIGHT:
                            jogador1.speedx += 8*DT
                            direcao1 = 'D'
                            
                        if evento.key == pygame.K_UP:
                            jogador1.jump()
                            
                        if evento.key == pygame.K_DOWN:
                            encima1 = False
                            
                        if evento.key == pygame.K_SLASH:
                            if direcao1 == 'D':
                                jogador1.atirarD()
                            if direcao1 == 'E':
                                jogador1.atirarE()
                                
                        if evento.key == pygame.K_PERIOD:
                            if direcao1 == 'D':
                                jogador1.especialD()
                            if direcao1 == 'E':
                                jogador1.especialE()
                            
                            
                    if evento.type == pygame.KEYUP:
                        if evento.key in tecla and tecla[evento.key]:
                            if evento.key == pygame.K_LEFT:
                                jogador1.speedx += 8*DT
                                
                            if evento.key == pygame.K_RIGHT:
                                jogador1.speedx -= 8*DT
                                    
                            if evento.key == pygame.K_DOWN:
                                encima1 = True
                                
                    if evento.type == pygame.KEYDOWN: #Comandos JOGADOR 2
                        tecla[evento.key] = True
                        if evento.key == pygame.K_a:
                            jogador2.speedx -= 8*DT
                            direcao2 = 'E'
                        if evento.key == pygame.K_d:
                            jogador2.speedx += 8*DT
                            direcao2 = 'D'
                        if evento.key == pygame.K_w:
                            jogador2.jump()
                        if evento.key == pygame.K_s:
                                encima2 = False
                        if evento.key == pygame.K_q:
                            if direcao2 == 'D':
                                jogador2.atirarD()
                            if direcao2 == 'E':
                                jogador2.atirarE()
                        if evento.key == pygame.K_1:
                            if direcao2 == 'D':
                                jogador2.especialD()
                            if direcao2 == 'E':
                                jogador2.especialE()
                            
                            
                    if evento.type == pygame.KEYUP:
                        if evento.key in tecla and tecla[evento.key]:
                            if evento.key == pygame.K_a:
                                jogador2.speedx += 8*DT
                            if evento.key == pygame.K_d:
                                jogador2.speedx -= 8*DT
                            if evento.key == pygame.K_s:
                                encima2 = True
         
        
        '''dano_machado1 = pygame.sprite.spritecollide(jogador1, machados, False, pygame.sprite.collide_mask)  
        dano_machado2 = pygame.sprite.spritecollide(jogador2, machados, False, pygame.sprite.collide_mask)      
                        
        if dano_machado1:
            machado.rect.top = ALTURA
            vidas1 -= 1
            fun.tocar_som(som_dano)
                    
        if dano_machado2:
            machado.rect.top = ALTURA
            vidas2 -= 1
            fun.tocar_som(som_dano)'''
        
        dano_tiro1 = pygame.sprite.spritecollide(jogador1, todas_balas, True) 
        if dano_tiro1:
            fun.tocar_som(som_dano)
            vidas1 -= 1
        dano_tiro2 = pygame.sprite.spritecollide(jogador2, todas_balas, True, pygame.sprite.collide_mask)
        if dano_tiro2:
            fun.tocar_som(som_dano)
            vidas2 -= 1
                                
                                
        dano_explo1 = pygame.sprite.spritecollide(jogador1, explosoes, False, pygame.sprite.collide_mask)
        if dano_explo1:
            vidas1 = 0
            
        
        dano_explo2 = pygame.sprite.spritecollide(jogador2, explosoes, False, pygame.sprite.collide_mask)
        if dano_explo2:
            vidas2 = 0
            
        if vidas1 == 0:
                jogador1.kill()
                rodando = GAME_OVER
                vitoria = VITORIA2
                
                
        if vidas2 == 0:
                jogador2.kill()
                rodando = GAME_OVER
                vitoria = VITORIA1
        
        plat1 = pygame.sprite.spritecollide(jogador1, plataformas, False, pygame.sprite.collide_mask)
            
        if jogador1.speedy > 0 and plat1 and encima1:
            for plataforma in plataformas:
                jogador1.collide(plataforma.rect)
                
        plat2 = pygame.sprite.spritecollide(jogador2, plataformas, False, pygame.sprite.collide_mask)
            
        if jogador2.speedy > 0 and plat2 and encima2:
            for plataforma in plataformas:
                jogador2.collide(plataforma.rect)
                
            
        todos_sprites.update()
        
        janela.fill(BRANCO)  
        janela.blit(plano_jogo, (0, 0))
        todos_sprites.draw(janela)
        
    
        coracao = pygame.image.load(path.join(DIR_IMG, CORE_IMG)).convert_alpha()
        coracao = pygame.transform.scale(coracao, (LARGURA_CORE,ALTURA_CORE))
        
        '''dinamite_logo1 = pygame.image.load(path.join(DIR_IMG,ANIM_DINAMITE_D,DINAMITE_LOGO)).convert_alpha()
        dinamite_logo1 = pygame.transform.scale(dinamite_logo1, (LARGURA_CORE,ALTURA_CORE))
        dinamite_logo2 = pygame.image.load(path.join(DIR_IMG,ANIM_DINAMITE_D,DINAMITE_LOGO)).convert_alpha()
        dinamite_logo2 = pygame.transform.scale(dinamite_logo2, (LARGURA_CORE,ALTURA_CORE))'''
        
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

    
    musica = path.join(DIR_SOM,MUSICA_FINAL)
    fun.tocar_musica(musica)


    lista_gameplay = [rodando,vitoria]
    return lista_gameplay