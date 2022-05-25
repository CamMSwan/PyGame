import pygame
from Configurações import DIR_IMG,FPS,QUIT,GAME,PRETO
from os import path

def gameplay(janela):
    tempo_fps = pygame.time.Clock()
    imagem_raposa = pygame.image.load(path.join(DIR_IMG, 'imagem_humberto.png')).convert()
    imagem_raposa = pygame.transform.scale(imagem_raposa, (600, 400))
    rodando = True
    while rodando:
        tempo_fps.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                estado = QUIT
                rodando = False

            if evento.type == pygame.KEYUP:
                estado = GAME
                rodando = False

        janela.fill(PRETO)  
        janela.blit(imagem_raposa, (0, 0))
        pygame.display.flip()

    return estado
