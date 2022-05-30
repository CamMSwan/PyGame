import pygame
from Configurações import DIR_IMG,FPS,QUIT,GAME,PRETO, LARGURA, ALTURA
from os import path
from Elementos import DOUTOR_IMG, FOX_IMG
    
class Player1(pygame.sprite.Sprite):
    def __init__(self, grupo, elementos):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = elementos[FOX_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA / 2
        self.rect.bottom = ALTURA - 10
        self.speedx = 0
        self.groups = grupo
        self.elementos = elementos

    def update(self):
        # Atualização da posição da raposa
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
            
class Player2(pygame.sprite.Sprite):
    def __init__(self, grupo, elementos):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = elementos[DOUTOR_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA / 2
        self.rect.bottom = ALTURA - 10
        self.speedx = 0
        self.groups = grupo
        self.elementos = elementos

    def update(self):
        # Atualização da posição da raposa
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0

class Bala(pygame.sprite.Sprite):
    def __init__(self, img ,bottom,centerx):
        pygame.sprite.Sprite.__init__(self)

        self.image = img 
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        #definindo lugar em x e y

        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedx = 15

    def update(self):
        self.rect.x += self.speedx
        # se a sala passar do fim da tela, desaparece
        if self.rect.centerx > 960:
            self.kill()
