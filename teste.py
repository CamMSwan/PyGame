from multiprocessing import Event
import pygame
import random
from sqlalchemy import false
from sympy import fps
from Classes import player1,player2
import Elementos as El

#Andar jogador 1

game = True
clock = pygame.time.Clock()
FPS = 60
elementos = El.carregar_elementos()
todos_sprites = pygame.sprite.Group()
grupo = {}
grupo['todos_sprites'] = todos_sprites
jogador1 = player1(grupo,elementos)
jogador2 = player2(grupo,elementos)


while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = false
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jogador1.speedx += 8
            if event.key == pygame.K_RIGHT:
                jogador1.speedx += 8
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                jogador1.speedx += 8
            if event.key == pygame.K_RIGHT:
                jogador1.speedx += 8



