import pygame
from pygame import mixer
from Classes import Morte
from Configurações import ALTURA, DIR_IMG, DIR_SOM, INIC, LARGURA,QUIT,GAME,GAME_OVER
from os import path
import Musicas as mus
from Elementos import FUNDO_GAME_OVER1, FUNDO_GAME_OVER2, MUSICA_JOGO, MUSICA_MENU


'''Inicia o mixer para musicas'''
mixer.init()

'''Função da tela final que recebe a tela usada e quem venceu'''
def tela_final (janela,vitoria):
    tempo_fps = pygame.time.Clock()
    musica = path.join(DIR_SOM,MUSICA_JOGO)
    plano_fundo1 = pygame.image.load(path.join(DIR_IMG, FUNDO_GAME_OVER1)).convert()
    plano_fundo1 = pygame.transform.scale(plano_fundo1, (LARGURA,ALTURA))
    plano_fundo2 = pygame.image.load(path.join(DIR_IMG, FUNDO_GAME_OVER2)).convert()
    plano_fundo2 = pygame.transform.scale(plano_fundo2, (LARGURA,ALTURA))
    corvo = Morte()
    todos_sprites = pygame.sprite.Group()
    grupo = {}
    grupo['todos_sprites'] = todos_sprites
    todos_sprites.add(corvo)
    rodando = GAME_OVER
    
    '''Loop tela final'''
    while rodando == GAME_OVER:
        
        tempo_fps.tick(60)
        
        '''Checa as interações do usuario'''
        for evento in pygame.event.get():
            
            '''Se ele fechou a tela'''
            if evento.type == pygame.QUIT:
                rodando = QUIT
                
            '''Checa o botao clicado'''
            if evento.type == pygame.KEYUP:
                
                '''Se foi a barra de espaço, ele reinicia o jogo'''
                if evento.key == pygame.K_SPACE:
                    rodando = GAME
                    mixer.music.stop()
                    mus.tocar_musica(musica)
                
                '''Se foi o ESC, ele volta para a tela inicial, 
                porem esse é mais para o desenvolvedor que está mostrando, 
                para ele não ter que ficar fechando e abrindo dnv
                ''' 
                if evento.key == pygame.K_ESCAPE:
                    rodando = INIC
                    musica = path.join(DIR_SOM,MUSICA_MENU)
                    mus.tocar_musica(musica)
        
        todos_sprites.update()
        
        '''Checa qual jogador venceu e mostra na tela o ganhador'''
        if vitoria == 1:
            pdf_rect = plano_fundo1.get_rect()
            janela.blit(plano_fundo1, pdf_rect)
        if vitoria == 2:
            pdf_rect = plano_fundo2.get_rect()
            janela.blit(plano_fundo2, pdf_rect)
            
        todos_sprites.draw(janela)
        

        pygame.display.update()

    return rodando