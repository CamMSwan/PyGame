from turtle import width
from click import edit
import pygame
from pygame import mixer
from Classes import Morte
from Configurações import ALTURA, DIR_IMG, DIR_SOM,FPS, LARGURA,QUIT,GAME,GAME_OVER
from os import path
import Funções as fun
from Elementos import  FUNDO_GAME_OVER, MUSICA_JOGO


mixer.init()

def tela_final (janela):
    tempo_fps = pygame.time.Clock()
    musica = path.join(DIR_SOM,MUSICA_JOGO)
    tempo_fps = pygame.time.Clock()
    plano_fundo = pygame.image.load(path.join(DIR_IMG, FUNDO_GAME_OVER)).convert()
    plano_fundo = pygame.transform.scale(plano_fundo, (LARGURA,ALTURA))
    pdf_rect = plano_fundo.get_rect()
    corvo = Morte()
    todos_sprites = pygame.sprite.Group()
    grupo = {}
    grupo['todos_sprites'] = todos_sprites
    todos_sprites.add(corvo)
    rodando = GAME_OVER
    
    while rodando == GAME_OVER:
        
        tempo_fps.tick(FPS)
        
        for evento in pygame.event.get():
            
            if evento.type == pygame.QUIT:
                rodando = QUIT
                

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_KP_ENTER:
                    rodando = GAME
                    mixer.music.stop()
                    fun.tocar_musica(musica)
        
        todos_sprites.update()
        

        janela.blit(plano_fundo, pdf_rect)
        todos_sprites.draw(janela)
        

        pygame.display.update()

    return rodando