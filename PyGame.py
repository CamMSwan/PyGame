import pygame

pygame.init()

Largura = 960
Altura = 540
window = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Raposa Kombat')

game = True

image = pygame.image.load('Raposa_Loka.jpg').convert()
image = pygame.transform.scale(image, (960,540))

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    window.fill((0, 0, 0))  
    window.blit(image, (0,0))

    
    pygame.display.update()  


pygame.quit()  

