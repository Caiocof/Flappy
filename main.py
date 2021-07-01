import pygame
import os
import random

# CONTANTES DO JOGO
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800

# USANDO O TRANFORMS.SCALA2X PARA DUPLICAR O TAMANHO DAS IMAGENS E OS.PATH.JOIN PARA PASSAR O CAMINHO DAS IMG
PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
BASE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
BACKGROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pg.png')))

# ARRAY COM AS IMAGENS DO PASSARO
BIRD_IMAGE = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

# PEGANDO AS FONTS DO JOGO
pygame.font.init()
SCORE_FONT = pygame.font.SysFont('arial', 50)




class Pipe:
    pass


class Base:
    pass
