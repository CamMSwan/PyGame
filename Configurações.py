from os import path

'''Diretório de Imagens e Sons'''
DIR_IMG = path.join(path.dirname(__file__), 'imagens')
DIR_SOM = path.join(path.dirname(__file__), 'sons')

'''Delta  de tempo para não conseguir diminuir o FPS preservando o movimento'''
DT = 1.5

'''Largura e Altura da tela'''
LARGURA = 1400
ALTURA = 780

'''Frames por segundo'''
FPS = 40

'''Cor preta'''
PRETO = (0, 0, 0)

'''Estados do jogo'''
INIC = 0
GAME = 1
GAME_OVER = 2
QUIT = 3

'''Imagem e dimensões da vida'''
CORE_IMG = 'coracao.png'    
LARGURA_CORE = 50
ALTURA_CORE = 40

'''Posições das vidas'''
POSICOES_CORE1 = [(20, 20), (90, 20), (160, 20)]
POSICOES_CORE2 = [(LARGURA - 210, 20), (LARGURA - 140, 20), (LARGURA - 70, 20)]


'''Condição de qual jogador venceu'''
VITORIA1 = 1
VITORIA2 = 2