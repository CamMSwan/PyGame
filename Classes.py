'''importa os elementos necessarios para as calsses'''
import pygame
from Configurações import DIR_IMG, DIR_SOM, DT,LARGURA, ALTURA
from os import path
from Elementos import ALTURA_ARB, ALTURA_BALA, ALTURA_DIN, ALTURA_DR, ALTURA_EX, ALTURA_FOX, ALTURA_P, ALTURA_POS_P, ANIM_DINAMITE, ARBUSTO, BALA1_IMG, BALA2_IMG, BOOM, CHAO, EXPLOSAO, INIMIGO_IMG, LARGURA_ARB, LARGURA_BALA, LARGURA_DIN, LARGURA_DR, LARGURA_EX, LARGURA_FOX, LARGURA_P, MORTE, PLATAFORMA_IMG, RAPOSA, TIRO
import Musicas as fun

'''Classe do jogador 1'''
class Player1(pygame.sprite.Sprite):
    def __init__(self, grupo):
        '''Construtor da classe mãe (Sprite).'''
        pygame.sprite.Sprite.__init__(self)
        self.imagens = []
        for i in range(0,2):
            self.image = pygame.image.load(path.join(DIR_IMG,RAPOSA,'raposa{}.png'.format(i) )).convert_alpha()
            self.image = pygame.transform.scale(self.image, (LARGURA_FOX, ALTURA_FOX))
            self.imagens.append(self.image)
            
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA - LARGURA_FOX/2
        self.rect.bottom = CHAO
        self.speedx = 0
        self.speedy = 0
        self.groups = grupo

        '''Só será possivel atirar a cada 500 milisegundos e usar especial a cada 3500 milisegundos'''
        self.last_shot = pygame.time.get_ticks()
        self.ultimo_especial = pygame.time.get_ticks()
        self.shoot_ticks = 500
        self.especial_ticks = 3500
        
        '''Define gravidade,chao, e chao da plataforma'''
        self.y_gravidade = 2
        self.chao = CHAO
        self.plataforma = ALTURA_POS_P
        
    '''Fisica de movimento vertical do jogador 1'''
    def movimento_vertical(self):
        self.speedy += self.y_gravidade
        if self.speedy > 20*DT:
            self.speedy = 20*DT
        if self.rect.bottom > self.chao:
            self.no_chao = True
            self.speedy = 0
            self.rect.bottom = self.chao
            
    '''Fisica para detectar se jogador esta em cima da plataforma'''    
    def collide(self,rect): 
        collisions = self.rect.colliderect(rect)  
        collision = abs(self.rect.bottom - rect.top) 
        tolerancia = 8
        if collisions:
            if collision < tolerancia:
                self.no_chao =True
                self.speedy = 0
                self.rect.bottom = self.plataforma+5
    
    '''Função para ele pular'''               
    def jump(self):    
        if self.no_chao:
            self.jumping = True
            self.speedy -= 20*DT
            self.no_chao = False   
             
                       
    def update(self):
        ''' Atualização da posição do jogador 1'''
        self.rect.x += self.speedx
        self.rect.bottom += self.speedy

        if self.speedx < 0:
            self.image = self.imagens[1]
        if self.speedx > 0:
            self.image = self.imagens[0]
            
        ''' Mantem dentro da tela'''
        if self.rect.right > LARGURA :
            self.rect.right = LARGURA 
        if self.rect.left < 0:
            self.rect.left = 0
        self.movimento_vertical()
           
    '''Funções para ativar seu especial, dependendo da direção que ele esteja apontando'''   
    
    def especialD(self):
        '''Tick correspondente a agora'''
        agora = pygame.time.get_ticks()
        
        '''Verifica quantos ticks se passaram desde o último tiro.'''
        elapsed_ticks = agora - self.ultimo_especial

        ''' Se já pode atirar novamente'''
        if elapsed_ticks > self.especial_ticks:
            
            '''Marca o tick do ultiom uso.'''
            self.ultimo_especial = agora
            
            '''Novo dinamite'''
            nova_dinamite = Dinamite(self.rect.x+LARGURA_FOX-10,self.rect.y+10,1,self.groups)
            self.groups['todos_sprites'].add(nova_dinamite)
            self.groups['dinamites'].add(nova_dinamite)
            
    def especialE(self):
        '''Tick correspondente a agora'''
        agora = pygame.time.get_ticks()
        
        '''Verifica quantos ticks se passaram desde o último tiro.'''
        elapsed_ticks = agora - self.ultimo_especial

        ''' Se já pode atirar novamente'''
        if elapsed_ticks > self.especial_ticks:
            
            '''Marca o tick do ultiom uso.'''
            self.ultimo_especial = agora
            
            '''Novo dinamite'''
            nova_dinamite = Dinamite(self.rect.x+10,self.rect.y+10,-1,self.groups)
            self.groups['todos_sprites'].add(nova_dinamite)
            self.groups['dinamites'].add(nova_dinamite)
            
    '''Funções para ele atirar, dependendo da sua direção'''     
        
    def atirarE(self):
        '''Tick correspondente a agora'''
        agora = pygame.time.get_ticks()
        
        '''Verifica quantos ticks se passaram desde o último tiro.'''
        elapsed_ticks = agora - self.last_shot

        ''' Se já pode atirar novamente'''
        if elapsed_ticks > self.shoot_ticks:
            
            '''Marca o tick do ultiom tiro.'''
            self.last_shot = agora
            
            '''Novo tiro'''
            nova_bala = BalaE(self.rect.left-2,self.rect.centery)
            self.groups['todos_sprites'].add(nova_bala)
            self.groups['todas_balas'].add(nova_bala)
            tiro = path.join(DIR_SOM,TIRO)
            fun.tocar_som(tiro)
            
    def atirarD(self):
        '''Tick correspondente a agora'''
        agora = pygame.time.get_ticks()
        
        '''Verifica quantos ticks se passaram desde o último tiro.'''
        elapsed_ticks = agora - self.last_shot

        ''' Se já pode atirar novamente'''
        if elapsed_ticks > self.shoot_ticks:
            
            '''Marca o tick do ultiom tiro.'''
            self.last_shot = agora
            
            '''Novo tiro'''
            nova_bala = BalaD(self.rect.right,self.rect.centery)
            self.groups['todos_sprites'].add(nova_bala)
            self.groups['todas_balas'].add(nova_bala)
            tiro = path.join(DIR_SOM,TIRO)
            fun.tocar_som(tiro)


'''Classe do jogador 2'''          
class Player2(pygame.sprite.Sprite):
    def __init__(self, grupo):
        '''Construtor da classe mãe (Sprite).'''
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
        self.groups = grupo
        self.speedx = 0
        self.speedy = 0
        self.rect.bottom = CHAO
        
        '''Só será possivel atirar a cada 500 milisegundos e usar especial a cada 3500 milisegundos'''
        self.last_shot = pygame.time.get_ticks()
        self.ultimo_especial = pygame.time.get_ticks()
        self.shoot_ticks = 500
        self.especial_ticks = 3500
        
        '''Define gravidade,chao, e chao da plataforma'''
        self.y_gravidade = 2
        self.chao = CHAO
        self.plataforma = ALTURA_POS_P
        
    '''Fisica de movimento vertical do jogador 2'''
    def movimento_vertical(self):
        self.speedy += self.y_gravidade
        if self.speedy > 20*DT:
            self.speedy = 20*DT
        if self.rect.bottom > self.chao:
            self.no_chao = True
            self.speedy = 0
            self.rect.bottom = self.chao
            
    '''Fisica para detectar se jogador esta em cima da plataforma'''    
    def collide(self,rect): 
        collisions = self.rect.colliderect(rect)  
        collision = abs(self.rect.bottom - rect.top) 
        tolerancia = 8
        if collisions:
            if collision < tolerancia:
                self.no_chao =True
                self.speedy = 0
                self.rect.bottom = self.plataforma+5
    
    '''Função para ele pular'''               
    def jump(self):    
        if self.no_chao:
            self.jumping = True
            self.speedy -= 20*DT
            self.no_chao = False   
             
                       
    def update(self):
        ''' Atualização da posição do jogador 2'''
        self.rect.x += self.speedx
        self.rect.bottom += self.speedy

        if self.speedx < 0:
            self.image = self.imagens[1]
        if self.speedx > 0:
            self.image = self.imagens[0]
            
        ''' Mantem dentro da tela'''
        if self.rect.right > LARGURA :
            self.rect.right = LARGURA 
        if self.rect.left < 0:
            self.rect.left = 0
        self.movimento_vertical()
           
    '''Funções para ativar seu especial, dependendo da direção que ele esteja apontando'''   
    
    def especialD(self):
        '''Tick correspondente a agora'''
        agora = pygame.time.get_ticks()
        
        '''Verifica quantos ticks se passaram desde o último tiro.'''
        elapsed_ticks = agora - self.ultimo_especial

        ''' Se já pode atirar novamente'''
        if elapsed_ticks > self.especial_ticks:
            
            '''Marca o tick do ultiom uso.'''
            self.ultimo_especial = agora
            
            '''Novo dinamite'''
            nova_dinamite = Dinamite(self.rect.x+LARGURA_FOX-10,self.rect.y+10,1,self.groups)
            self.groups['todos_sprites'].add(nova_dinamite)
            self.groups['dinamites'].add(nova_dinamite)
            
    def especialE(self):
        '''Tick correspondente a agora'''
        agora = pygame.time.get_ticks()
        
        '''Verifica quantos ticks se passaram desde o último tiro.'''
        elapsed_ticks = agora - self.ultimo_especial

        ''' Se já pode atirar novamente'''
        if elapsed_ticks > self.especial_ticks:
            
            '''Marca o tick do ultiom uso.'''
            self.ultimo_especial = agora
            
            '''Novo dinamite'''
            nova_dinamite = Dinamite(self.rect.x+10,self.rect.y+10,-1,self.groups)
            self.groups['todos_sprites'].add(nova_dinamite)
            self.groups['dinamites'].add(nova_dinamite)
            
    '''Funções para ele atirar, dependendo da sua direção'''     
        
    def atirarE(self):
        '''Tick correspondente a agora'''
        agora = pygame.time.get_ticks()
        
        '''Verifica quantos ticks se passaram desde o último tiro.'''
        elapsed_ticks = agora - self.last_shot

        ''' Se já pode atirar novamente'''
        if elapsed_ticks > self.shoot_ticks:
            
            '''Marca o tick do ultiom tiro.'''
            self.last_shot = agora
            
            '''Novo tiro'''
            nova_bala = BalaE(self.rect.left-2,self.rect.centery)
            self.groups['todos_sprites'].add(nova_bala)
            self.groups['todas_balas'].add(nova_bala)
            tiro = path.join(DIR_SOM,TIRO)
            fun.tocar_som(tiro)
            
    def atirarD(self):
        '''Tick correspondente a agora'''
        agora = pygame.time.get_ticks()
        
        '''Verifica quantos ticks se passaram desde o último tiro.'''
        elapsed_ticks = agora - self.last_shot

        ''' Se já pode atirar novamente'''
        if elapsed_ticks > self.shoot_ticks:
            
            '''Marca o tick do ultiom tiro.'''
            self.last_shot = agora
            
            '''Novo tiro'''
            nova_bala = BalaD(self.rect.right,self.rect.centery)
            self.groups['todos_sprites'].add(nova_bala)
            self.groups['todas_balas'].add(nova_bala)
            tiro = path.join(DIR_SOM,TIRO)
            fun.tocar_som(tiro)

                    
'''Classe das plataformas'''                   
class Plataforma(pygame.sprite.Sprite):
    def __init__(self,centerx,top):
        '''Construtor da classe mãe (Sprite).'''
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path.join(DIR_IMG, PLATAFORMA_IMG)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARGURA_P, ALTURA_P))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.top = top

'''Classes das balas para direita e esquerda'''        
class BalaE(pygame.sprite.Sprite):
    def __init__(self,right,centery):
        '''Construtor da classe mãe (Sprite).'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(DIR_IMG, BALA2_IMG)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARGURA_BALA,ALTURA_BALA))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        
        '''Definindo local de spawn e velocidade'''
        self.rect.right = right
        self.rect.centery = centery
        self.speedx = -29*DT
        
    '''Atualiza posição da bala'''
    def update(self):
        self.rect.x += self.speedx
        
        '''Se passar do fim da tela desaparece'''
        if self.rect.left < 0:
            self.kill()

class BalaD(pygame.sprite.Sprite):
    def __init__(self,left,centery):
        '''Construtor da classe mãe (Sprite).'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(DIR_IMG, BALA1_IMG)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARGURA_BALA,ALTURA_BALA))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        '''Definindo local de spawn e velocidade'''
        self.rect.left = left
        self.rect.centery = centery
        self.speedx = 29*DT
        
    '''Atualiza posição da bala'''
    def update(self):
        self.rect.x += self.speedx
        
        '''Se passar do fim da tela desaparece'''
        if self.rect.left < 0:
            self.kill()            
            
'''Animação do corvo na tela final'''           
class Morte(pygame.sprite.Sprite):
    def __init__(self):
        '''Construtor da classe mãe (Sprite).'''
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
        
        '''Intervalo das animações'''
        self.intervalo = 1000
    
    '''Atualiza frame da animação'''
    def update(self):
        agora = pygame.time.get_ticks()
        elapsed_ticks = agora - self.last_animation
        self.frame_atual += 0.9
        
        if self.frame_atual >= len(self.frames):
            self.frame_atual = 0
        
        '''Verifica se ja pode rodar animação denovo'''
        if elapsed_ticks > self.intervalo:
            self.last_animation = agora
            self.image = self.frames[int(self.frame_atual)]
        
'''Animação do mato seco na tela incial'''           
class Tumblweed(pygame.sprite.Sprite):
    def __init__(self):
        '''Construtor da classe mãe (Sprite).'''
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        for i in range(0,3):
            self.image = pygame.image.load('{}/{}/tumbleweed-{}.png'.format(DIR_IMG,ARBUSTO,i)).convert_alpha()
            self.image = pygame.transform.scale(self.image, (LARGURA_ARB, ALTURA_ARB))
            self.rect = self.image.get_rect()
            self.frames.append(self.image)
            
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect.x = 0 - LARGURA_ARB
        self.rect.y= ALTURA - 240
        self.speedx = 6*DT
        
    '''Atualiza frame da animação'''    
    def update(self):
        self.frame_atual += 0.15
        self.rect.x += self.speedx
        '''se sair da tela spawna outro'''
        if self.rect.left > LARGURA:
                self.image = self.frames[int(self.frame_atual)]
                self.rect.x = 0 - LARGURA_ARB
                self.rect.y= ALTURA - 240                
                self.speedx = 6*DT
                
        if self.frame_atual >= len(self.frames):
            self.frame_atual = 0
        
        self.image = self.frames[int(self.frame_atual)]
        
        '''Se sair da tela desaparece depois de spawnar outro'''
        if self.rect.left > LARGURA:
            self.kill()  

'''Classe da dinamite'''            
class Dinamite(pygame.sprite.Sprite):
    def __init__(self,centerx,centery,direção,grupo):
        '''Construtor da classe mãe (Sprite).'''
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        for i in range(0,4):
                self.image = pygame.image.load('{}\{}\dinamite-{}.png'.format(DIR_IMG,ANIM_DINAMITE,i)).convert_alpha()
                self.image = pygame.transform.scale(self.image, (LARGURA_DIN, ALTURA_DIN))
                self.rect = self.image.get_rect()
                self.frames.append(self.image)
                            
        self.mask = pygame.mask.from_surface(self.image)
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.speedy = -10*DT
        self.speedx = 8*DT * direção
        self.groups = grupo
        self.no_chao = False
        
        '''Define gravidade,chao, e chao da plataforma'''
        self.y_gravidade = 1
        self.chao = CHAO
        self.plataforma = ALTURA_POS_P
        
    '''Fisica de movimento vertical do dinamite'''
    def movimento_vertical(self):
        self.speedy += self.y_gravidade
        if self.speedy > 10*DT:
            self.speedy = 10*DT
        if self.rect.bottom > self.chao:
            self.no_chao = True
            self.speedy = 0
            self.rect.bottom = self.chao
            
    '''Função para explosão do dinamite'''      
    def explosao(self):
        if self.no_chao:
                explosao = Explosao(self.rect.centerx, self.chao)
                self.groups['todos_sprites'].add(explosao)
                self.groups['explosoes'].add(explosao)
                som_boom = path.join(DIR_SOM,BOOM)
                fun.tocar_som(som_boom)
                self.kill()
                self.chao = False
     
    '''Atualiza posições do dinamite'''       
    def update(self):
        self.frame_atual += 0.32
        self.rect.y += self.speedy
        self.rect.x += self.speedx
                
        if self.frame_atual >= len(self.frames):
            self.frame_atual = 0
        
        self.image = self.frames[int(self.frame_atual)]
        self.movimento_vertical()
        
        '''Explode em contato com o chão'''
        if self.no_chao:
            self.explosao()
            
'''Classe da explosão'''
class Explosao(pygame.sprite.Sprite):
    def __init__(self,centerx,bottom):
        '''Construtor da classe mãe (Sprite).'''
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        for i in range(0,6):
            self.image = pygame.image.load('{}/{}/explosão-{}.png'.format(DIR_IMG,EXPLOSAO,i)).convert_alpha()
            self.image = pygame.transform.scale(self.image, (LARGURA_EX, ALTURA_EX))
            self.rect = self.image.get_rect()
            self.frames.append(self.image)
            
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        
        '''Posição da explosão'''
        self.rect.centerx = centerx
        self.rect.bottom = bottom
    
    '''Atualiza frames da animação'''
    def update(self):
        self.frame_atual += 0.32*DT
        
        '''Terminando a animação desaparece'''
        if self.frame_atual > len(self.frames):
            self.kill()
            self.frame_atual = 0
         
        
        self.image = self.frames[int(self.frame_atual)]
        
        
        
     
