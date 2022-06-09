'''Importa os elementos e pacotes necessários'''
import pygame
from pygame import mixer
from Classes import Morte
from Configurações import ALTURA, DIR_IMG, DIR_SOM, INIC, LARGURA,QUIT,GAME,GAME_OVER
from os import path
import Musicas as mus
from Elementos import FUNDO_GAME_OVER1, FUNDO_GAME_OVER2, MUSICA_JOGO, MUSICA_MENU


'''Inicia o mixer para musicas'''
mixer.init()

'''Função da tela final que recebe o tela com as dimensões usadas e quem venceu'''
def tela_final (janela,vitoria):
    
    '''Variavel de ajuste da tempo'''
    tempo_fps = pygame.time.Clock()
    
    '''Arquivo da musica do jogo'''
    musica = path.join(DIR_SOM,MUSICA_JOGO)
    
    '''Elementos do plano de fundo'''
    plano_fundo1 = pygame.image.load(path.join(DIR_IMG, FUNDO_GAME_OVER1)).convert()
    plano_fundo1 = pygame.transform.scale(plano_fundo1, (LARGURA,ALTURA))
    plano_fundo2 = pygame.image.load(path.join(DIR_IMG, FUNDO_GAME_OVER2)).convert()
    plano_fundo2 = pygame.transform.scale(plano_fundo2, (LARGURA,ALTURA))
    
    '''ELementos da animação do corvo'''
    corvo = Morte()
    todos_sprites = pygame.sprite.Group()
    grupo = {}
    grupo['todos_sprites'] = todos_sprites
    todos_sprites.add(corvo)
    
    '''Estado do jogo'''
    rodando = GAME_OVER
    
    '''Loop tela final'''
    while rodando == GAME_OVER:
        
        tempo_fps.tick(60)
        
        '''Checa as interações do usuario'''
        for evento in pygame.event.get():
            
            '''Verifica se foi fechada a tela'''
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
        
        
        '''Atualiza os sprites'''
        todos_sprites.update()
        
        '''Checa qual jogador venceu e mostra na tela o ganhador'''
        if vitoria == 1:
            pdf_rect = plano_fundo1.get_rect()
            janela.blit(plano_fundo1, pdf_rect)
        if vitoria == 2:
            pdf_rect = plano_fundo2.get_rect()
            janela.blit(plano_fundo2, pdf_rect)
            
            
        '''Desenha os sprites na tela'''
        todos_sprites.draw(janela)
        
        '''Atualiza a tela com atualização dos seus elementos'''
        pygame.display.update()

    return rodando