from multiprocessing import Event
import pygame
import random

from sqlalchemy import false
from sympy import fps

from Elementos import FOX_IMG

#Andar jogador 1

game = True
clock = pygame.time.Clock()
FPS = 60

while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = false
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                FOX_IMG.speedx += 8
            if event.key == pygame.K_RIGHT:
                FOX_IMG.speedx += 8
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                FOX_IMG.speedx += 8
            if event.key == pygame.K_RIGHT:
                FOX_IMG.speedx += 8