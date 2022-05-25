from os import path

DIR_IMG = path.join(path.dirname(__file__), 'imagens', 'img')
DIR_SOM = path.join(path.dirname(__file__), 'sons', 'snd')
DIR_FONT = path.join(path.dirname(__file__), 'fontes', 'font')

LARGURA = 960
ALTURA = 540 
FPS = 60 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

INIT = 0
GAME = 1
QUIT = 2