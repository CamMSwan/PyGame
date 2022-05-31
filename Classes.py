from turtle import delay
import pygame
from Configurações import DIR_IMG,FPS,QUIT,GAME,PRETO, LARGURA, ALTURA
from os import path
from Elementos import DOUTOR_IMG, FOX_IMG, LARGURA_M, MACHADO
import random
    
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
        self.speedy = 0
        self.groups = grupo
        self.elementos = elementos

    def get_input(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed==[pygame.K_LEFT]:
            self.speedx -= 8
        if key_pressed==[pygame.K_RIGHT]:
            self.speedx += 8
            
    def update(self):
        # Atualização da posição da raposa
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
        self.get_input()    

class Player2(pygame.sprite.Sprite):
    def __init__(self, grupo, elementos):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = elementos[DOUTOR_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA / 8
        self.rect.bottom = ALTURA - 20
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
            
class Machado(pygame.sprite.Sprite):
    def __init__(self,elementos):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.machado_anim = elementos[MACHADO]
         # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.machado_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        
        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50
        
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA-LARGURA_M)
        self.rect.y = random.randint(-100, -LARGURA_M)
        self.speedx = 3
        self.speedy = 3

    def update(self):
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > ALTURA or self.rect.right < 0 or self.rect.left > LARGURA:
            delay(2000)
            self.rect.x = random.randint(0, LARGURA-LARGURA_M)
            self.rect.y = random.randint(-100, -LARGURA)
            self.speedx = 3
            self.speedy = 3
          
            