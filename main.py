import pygame
import os
import random

# CONSTANTES DO JOGO
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800

# USANDO O TRANFORMS.SCALA2X PARA DUPLICAR O TAMANHO DAS IMAGENS E OS.PATH.JOIN PARA PASSAR O CAMINHO DAS IMG

BASE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
BACKGROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pg.png')))

# PEGANDO AS FONTS DO JOGO
pygame.font.init()
SCORE_FONT = pygame.font.SysFont('arial', 50)




class Base:
    pass
