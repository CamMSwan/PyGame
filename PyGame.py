from os import path
import pygame
from Configurações import DIR_SOM, INIC, LARGURA, ALTURA, GAME, QUIT 
import Inicialização as In
import Tela_de_jogo as Tj
from Elementos import MUSICA_MENU,MUSICA_JOGO
import Funções as fun


pygame.init()
pygame.mixer.init()
musica = path.join(DIR_SOM,MUSICA_MENU)
fun.tocar_musica(musica,-1)
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

