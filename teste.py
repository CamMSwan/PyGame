from multiprocessing import Event
import pygame
import random

from sqlalchemy import false

#Andar jogador 1

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        game = false
    if event.type==pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.speedx += 8
        if event.key == pygame.K_RIGHT:
            player.speedx += 8
    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            player.speedx += 8
        if event.key == pygame.K_RIGHT:
            player.speedx += 8