import pygame
from pygame import mixer
from Classes import Morte
from Configurações import ALTURA, DIR_IMG, DIR_SOM,FPS, LARGURA,QUIT,GAME,GAME_OVER
from os import path
import Funções as fun
from Elementos import FUNDO_GAME_OVER1, FUNDO_GAME_OVER2, MUSICA_JOGO, WANTEDF, WANTEDJ



mixer.init()

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
    
    while rodando == GAME_OVER:
        
        tempo_fps.tick(60)
        
        for evento in pygame.event.get():
            
            if evento.type == pygame.QUIT:
                rodando = QUIT
                

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_SPACE:
                    rodando = GAME
                    mixer.music.stop()
                    fun.tocar_musica(musica)
        
        todos_sprites.update()
        

        if vitoria == 1:
            pdf_rect = plano_fundo1.get_rect()
            janela.blit(plano_fundo1, pdf_rect)
        if vitoria == 2:
            pdf_rect = plano_fundo2.get_rect()
            janela.blit(plano_fundo2, pdf_rect)
            
        todos_sprites.draw(janela)
        

        pygame.display.update()

    return rodando