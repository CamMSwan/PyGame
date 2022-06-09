'''Importa os elementos e pacotes necessários'''
import pygame
from pygame import mixer
from Classes import Tumblweed
from Configurações import ALTURA, DIR_IMG, DIR_SOM,FPS, LARGURA,QUIT,GAME,PRETO
from os import path
import Musicas as mus
from Elementos import MUSICA_JOGO

'''Função de tela inicial que recebe a tela com as dimensões usadas'''
def tela_inicial(janela):
    
    '''Variavel de ajuste da tempo'''
    tempo_fps = pygame.time.Clock()
    
    '''Carrega os elementos pro plano de fundo'''
    plano_de_fundo = pygame.image.load(path.join(DIR_IMG, 'fundo_inicial.jpg')).convert()
    plano_de_fundo = pygame.transform.scale(plano_de_fundo, (LARGURA,ALTURA))
    pdf_rect = plano_de_fundo.get_rect()
    fonte = pygame.font.SysFont(None, 60)
    titulo = fonte.render('Red Dead Raposa', True, (0,0,0))
    integrante1 =  fonte.render('Nina Schvartsman', True, (0,0,0))
    integrante1 = pygame.transform.scale(integrante1,(200,20))
    integrante2 =  fonte.render('Cameron Swan', True, (0,0,0))
    integrante2 = pygame.transform.scale(integrante2, (180,20))
    integrante3 = fonte.render('Mariana Albuquerque', True, (0,0,0))
    integrante3 =  pygame.transform.scale(integrante3, (210,25))
    iniciar =  fonte.render('Aperte espaço para iniciar', True, (0,0,0))
    iniciar = pygame.transform.scale(iniciar, (210,25))
    
    '''musica da tela de jogo'''
    musica = path.join(DIR_SOM,MUSICA_JOGO)
    
    '''Recursos para animação do arbusto seco'''
    arbusto_rolando = Tumblweed()
    todos_sprites = pygame.sprite.Group()
    grupo = {}
    grupo['todos_sprites'] = todos_sprites
    todos_sprites.add(arbusto_rolando)
    
    '''Estado da função'''
    rodando = True
    '''Loop da tela inicial'''
    while rodando:
        '''Velocidade da tela'''
        tempo_fps.tick(FPS)

        '''Verifica interações do usuario'''
        for evento in pygame.event.get():
            
            '''Verifica se foi fechada a tela'''
            if evento.type == pygame.QUIT:
                estado = QUIT
                rodando = False

            '''Verifica tecla apertada'''
            if evento.type == pygame.KEYUP:
                
                '''Se apertar barra de espaço inicia tela de jogo'''
                if evento.key == pygame.K_SPACE:
                    estado = GAME
                    rodando = False
                    '''Inicia musica de jogo'''
                    if estado == GAME:
                        mixer.music.stop()
                        mus.tocar_musica(musica)
        
        '''Atualiza sprites'''
        todos_sprites.update()
        
        '''Preenche a tela com plano de fundo e seus elemnetos'''
        janela.fill(PRETO)  
        janela.blit(plano_de_fundo, pdf_rect)
        janela.blit(titulo, (520,300))
        janela.blit(integrante1, (0,655))
        janela.blit(integrante2, (0,685))
        janela.blit(integrante3, (0,715))
        janela.blit(iniciar, (580,370))
        
        '''Preenche com sprites(Arbusto seco nesse caso)'''
        todos_sprites.draw(janela)
        
        '''Atualiza a tela com atualizações dos seus elementos'''
        pygame.display.update()
        
    return estado