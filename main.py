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


# DEFINIÇÕES DA CLASSE PASSARO
class Bird:
    IMGS = BIRD_IMAGE

    # ANIMAÇÕES DE ROTAÇÃO
    MAX_ROTATION = 25
    SPEED_ROTATION = 20
    TIME_ANIMATION = 5

    # ATRIBUTOS DO PASSARO
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.heigth = self.y
        self.move_time = 0

        # ATRIBUTO PARA VERIFICAR EM QUAL IMG DO PASSARO ESTAMOS
        self.count_img = 0
        self.img = IMGS[0]

    # OS MOVIMENTOS NO PYGAME SÃO DEFINICOS
    # PARA CIMA É NEGATIVO NO Y E PARA BAIXO POSSITIVO
    # PARA A ESQUERTA É NEGATIVO NO X E PARA A DIREITA É POSSITIVO


class Pipe:
    pass


class Base:
    pass
