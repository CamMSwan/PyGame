from os import path
import pygame
from Configurações import DIR_SOM, INIC, LARGURA, ALTURA, GAME, QUIT, GAME_OVER
import Inicialização as In
import Tela_de_jogo as Tj
from Elementos import MUSICA_MENU
import Musicas as mus
import Finalização as fim

'''Inicia o Pygame e o Mixer(para tocar musicas) '''
pygame.init()
pygame.mixer.init()

'''Musica da tela de inicio'''
musica = path.join(DIR_SOM,MUSICA_MENU)
mus.tocar_musica(musica)

'''Carrega o tamanho da tela e o nome da caption'''
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Red Dead Raposa')

'''Looping principal que mostra a tela dependendo do estado do jogo'''
game = INIC
while game != QUIT:
    
    if game == INIC:
        game = In.tela_inicial(janela)
    if game == GAME:
        lista = Tj.gameplay(janela)
        game = lista[0]
        vitoria = lista[1]
    if game == GAME_OVER:
        game = fim.tela_final(janela,vitoria)
    else:
        game = QUIT
    
    pygame.display.update()  


pygame.quit()