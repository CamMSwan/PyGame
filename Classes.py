import pygame
from Configurações import DIR_IMG,FPS,QUIT,GAME,PRETO, LARGURA, ALTURA
from os import path
from Elementos import FOX_IMG
    
class carinha(pygame.sprite.Sprite):
    def __init__(self, groups, elementos):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = elementos[FOX_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA / 2
        self.rect.bottom = ALTURA - 10
        self.speedx = 0
        self.groups = groups
        self.assets = elementos

    def update(self):
        # Atualização da posição da raposa
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0

  