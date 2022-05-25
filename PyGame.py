import pygame
from Configurações import INIC, LARGURA, ALTURA, GAME, QUIT 
from os import path
import Inicialização as In
import Tela_de_jogo as Tj

pygame.init()

janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Raposa Kombat')

game = INIC
while game != QUIT:
    if game == INIC:
        game = In.tela_inicial(janela)
    elif game == GAME:
        game = Tj.gameplay(janela)
    else:
        game = QUIT

    
    pygame.display.update()  


pygame.quit()  

