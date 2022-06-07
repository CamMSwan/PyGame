import pygame
from Configurações import DIR_IMG, DIR_SOM,FPS,QUIT,GAME,PRETO, LARGURA, ALTURA
from os import path
from Elementos import ALTURA_ARB, ALTURA_BALA, ALTURA_DR, ALTURA_FOX, ALTURA_M, ALTURA_P, ARBUSTO, BALA1_IMG, BALA2_IMG, BARULHO_M, EXPLOSAO, INIMIGO_IMG, LARGURA_ARB, LARGURA_BALA, LARGURA_DR, LARGURA_FOX, LARGURA_M, LARGURA_P, MACHADO, MORTE, PLATAFORMA_IMG, RAPOSA, TIRO
import random
from pygame import mixer
import Funções as fun

machado = path.join(DIR_SOM,BARULHO_M)
    
class Player1(pygame.sprite.Sprite):
    def __init__(self, grupo):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.imagens = []
        for i in range(0,2):
            self.image = pygame.image.load(path.join(DIR_IMG,RAPOSA,'raposa{}.png'.format(i) )).convert_alpha()
            self.image = pygame.transform.scale(self.image, (LARGURA_FOX, ALTURA_FOX))
            self.imagens.append(self.image)
            
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA - LARGURA_FOX/2
        self.rect.bottom = ALTURA - 178
        self.speedx = 0
        self.speedy = 0
        self.groups = grupo

        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500
        
        self.y_gravidade = 1
        self.y_saltomax = 20
        self.y_velocidade = self.y_saltomax
        self.jumping = False
        

    def get_input(self):
        key_pressed = pygame.key.get_pressed()
        self.rect.y += self.speedy
        
        if key_pressed[pygame.K_UP]:
            self.jumping = True
        if self.jumping:
            self.rect.y -= self.y_velocidade
            self.y_velocidade -= self.y_gravidade
            if self.y_velocidade <-(self.y_saltomax):
                self.jumping = False
                self.y_velocidade = self.y_saltomax        
            

    def update(self):
        # Atualização da posição da raposa
        self.rect.x += self.speedx

        if self.speedx < 0:
            self.image = self.imagens[1]
        if self.speedx > 0:
            self.image = self.imagens[0]
            
        # Mantem dentro da tela
        if self.rect.right > LARGURA :
            self.rect.right = LARGURA 
        if self.rect.left < 0:
            self.rect.left = 0
        self.get_input()    
        
    
    def atirarD(self):
        # Verifica se pode atirar
        agora = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = agora - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = agora
            nova_bala = BalaD(self.rect.right-2,self.rect.centery)
            self.groups['todos_sprites'].add(nova_bala)
            self.groups['todas_balas'].add(nova_bala)
            tiro = path.join(DIR_SOM,TIRO)
            fun.tocar_som(tiro)
            
    def atirarE(self):
        # Verifica se pode atirar
        agora = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = agora - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = agora
            nova_bala = BalaE(self.rect.left-2,self.rect.centery)
            self.groups['todos_sprites'].add(nova_bala)
            self.groups['todas_balas'].add(nova_bala)
            tiro = path.join(DIR_SOM,TIRO)
            fun.tocar_som(tiro)
               
class Plataforma(pygame.sprite.Sprite):
    def __init__(self,centerx,bottom):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path.join(DIR_IMG, PLATAFORMA_IMG)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARGURA_P, ALTURA_P))
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom



class Player2(pygame.sprite.Sprite):
    def __init__(self, grupo):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.imagens = []
        for i in range(0,2):
            self.image = pygame.image.load(path.join(DIR_IMG,INIMIGO_IMG,'jacare-{}.png'.format(i) )).convert_alpha()
            self.image = pygame.transform.scale(self.image, (LARGURA_DR, ALTURA_DR))
            self.imagens.append(self.image)
            
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.image = self.imagens[0]
        self.rect.centerx = LARGURA_DR/2
        self.rect.bottom = ALTURA - 178
        self.speedx = 0
        self.speedy = 0
        self.groups = grupo

        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500
        
        self.y_gravidade = 1
        self.y_saltomax = 20
        self.y_velocidade = self.y_saltomax
        self.jumping = False
        

    def get_input(self):      
            key_pressed = pygame.key.get_pressed()
            
            if key_pressed[pygame.K_w]:
                self.jumping = True
            if self.jumping:
                self.rect.y -= self.y_velocidade
                self.y_velocidade -= self.y_gravidade
                if self.y_velocidade <-(self.y_saltomax):
                    self.jumping = False
                    self.y_velocidade = self.y_saltomax
        

    def update(self):
        # Atualização da posição da raposa
        self.rect.x += self.speedx
        
        if self.speedx < 0:
            self.image = self.imagens[1]
        if self.speedx > 0:
            self.image = self.imagens[0]
            
        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
        
        self.get_input()

    def atirarE(self):
        # Verifica se pode atirar
        agora = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = agora - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = agora
            nova_bala = BalaE(self.rect.left-45,self.rect.centery+35)
            self.groups['todos_sprites'].add(nova_bala)
            self.groups['todas_balas'].add(nova_bala)
            tiro = path.join(DIR_SOM,TIRO)
            fun.tocar_som(tiro)
            
    def atirarD(self):
            # Verifica se pode atirar
            agora = pygame.time.get_ticks()
            # Verifica quantos ticks se passaram desde o último tiro.
            elapsed_ticks = agora - self.last_shot

            # Se já pode atirar novamente...
            if elapsed_ticks > self.shoot_ticks:
                # Marca o tick da nova imagem.
                self.last_shot = agora
                nova_bala = BalaD(self.rect.right-45,self.rect.centery+35)
                self.groups['todos_sprites'].add(nova_bala)
                self.groups['todas_balas'].add(nova_bala)
                tiro = path.join(DIR_SOM,TIRO)
                fun.tocar_som(tiro)
                    
class BalaE(pygame.sprite.Sprite):
    def __init__(self,right,centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(DIR_IMG, BALA2_IMG)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARGURA_BALA,ALTURA_BALA))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        
        #definindo lugar em x e y

        self.rect.right = right
        self.rect.centery = centery
        self.speedx = -30

    def update(self):
        self.rect.x += self.speedx
        # se a sala passar do fim da tela, desaparece
        if self.rect.left < 0:
            self.kill()

class BalaD(pygame.sprite.Sprite):
    def __init__(self,left,centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(DIR_IMG, BALA1_IMG)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARGURA_BALA,ALTURA_BALA))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        
        #definindo lugar em x e y

        self.rect.left = left
        self.rect.centery = centery
        self.speedx = 30

    def update(self):
        self.rect.x += self.speedx
        # se a sala passar do fim da tela, desaparece
        if self.rect.left < 0:
            self.kill()
            
class Machado(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        for i in range(1,5):
            self.image = pygame.image.load('{}/{}/axe-{}.png'.format(DIR_IMG,MACHADO,i)).convert_alpha()
            self.image = pygame.transform.scale(self.image, (LARGURA_M, ALTURA_M))
            self.frames.append(self.image)
            
        self.mask = pygame.mask.from_surface(self.image)
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0+LARGURA_M,LARGURA-LARGURA_M)
        self.rect.y = 0-ALTURA_M
        self.speedy = 8
        
    def update(self):
        self.frame_atual += 0.14
        self.rect.y += self.speedy
        
        if self.rect.top > ALTURA or self.rect.right < 0 or self.rect.left > LARGURA:
            self.rect.x = random.randint(0+LARGURA_M,LARGURA-LARGURA_M)
            self.rect.y = 0-ALTURA_M
            self.speedy = 8
            
        if self.frame_atual >= len(self.frames):
            self.frame_atual = 0
        
        self.image = self.frames[int(self.frame_atual)]
        
        if self.rect.bottom < 0:
            self.kill()
            
            
class Morte(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        for i in range(1,5):
            self.image = pygame.image.load('{}/{}/original-{}.png.png'.format(DIR_IMG,MORTE,i)).convert_alpha()
            self.image = pygame.transform.scale(self.image, (300, 300))
            self.frames.append(self.image)
            
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA - 190
        self.rect.centery= ALTURA - 100
        self.last_animation = pygame.time.get_ticks()
        self.intervalo = 1000
        
    def update(self):
        agora = pygame.time.get_ticks()
        elapsed_ticks = agora - self.last_animation
        self.frame_atual += 0.9
        
        if self.frame_atual >= len(self.frames):
            self.frame_atual = 0
            
        if elapsed_ticks > self.intervalo:
            self.last_animation = agora
            self.image = self.frames[int(self.frame_atual)]
        
            
class Tumblweed(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        for i in range(0,3):
            self.image = pygame.image.load('{}/{}/tumbleweed-{}.png'.format(DIR_IMG,ARBUSTO,i)).convert_alpha()
            self.image = pygame.transform.scale(self.image, (LARGURA_ARB, ALTURA_ARB))
            self.frames.append(self.image)
            
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect()
        
        self.rect.x = 0 - LARGURA_ARB
        self.rect.y= ALTURA - 240
        self.speedx = 5
        
        self.last_animation = pygame.time.get_ticks()
        
    def update(self):
        self.frame_atual += 0.13
        self.rect.x += self.speedx
    
        if self.rect.left > LARGURA:
            pygame.time.wait(3500)
            self.image = self.frames[int(self.frame_atual)]
            self.rect.x = 0 - LARGURA_ARB
            self.rect.y= ALTURA - 240                
            self.speedx = 5
            
        if self.frame_atual >= len(self.frames):
            self.frame_atual = 0
        
        self.image = self.frames[int(self.frame_atual)]
        
        if self.rect.left > LARGURA:
            self.kill()  

class Explosao(pygame.sprite.Sprite):
    def __init__(self,centerx):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        for i in range(0,6):
            self.image = pygame.image.load('{}/{}/explosão-{}.png'.format(DIR_IMG,EXPLOSAO,i)).convert_alpha()
            self.image = pygame.transform.scale(self.image, (LARGURA_ARB, ALTURA_ARB))
            self.frames.append(self.image)
            
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect()
        
        self.rect.centerx = centerx
        self.rect.bottom = ALTURA - 178
        
    def update(self):
        self.frame_atual += 0.32
        
        if self.frame_atual > len(self.frames):
            self.frame_atual = 0
        
        self.image = self.frames[int(self.frame_atual)]
        
     
