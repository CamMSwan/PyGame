from os import path
import pygame
from Configurações import DIR_SOM, INIC, LARGURA, ALTURA, GAME, QUIT, GAME_OVER
import Inicialização as In
import Tela_de_jogo as Tj
from Elementos import MUSICA_MENU,MUSICA_JOGO
import Funções as fun
import finalização as fim


pygame.init()
pygame.mixer.init()
musica = path.join(DIR_SOM,MUSICA_MENU)
fun.tocar_musica(musica)
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Raposa Kombat')

game = INIC

while game != QUIT:
    
    if game == INIC:
        game = In.tela_inicial(janela)
    if game == GAME:
        game = Tj.gameplay(janela)
    if game == GAME_OVER:
        game = fim.tela_final(janela)
    else:
        game = QUIT
    
    pygame.display.update()  


pygame.quit()  

