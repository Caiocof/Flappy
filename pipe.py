import pygame
import os
import random

PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))


class Pipe:
    DISTANCE = 200
    SPEED = 5

    def __init__(self, x):
        self.x = x
        self.heigth = 0
        self.position_top = 0
        self.position_bottom = 0

        # metodo flip do pygame vira a imagem (nome_img, virar_horizontal, virar_vertical)
        self.pipe_top = pygame.transform.flip(PIPE_IMAGE, False, True)
        self.pipe_bottom = PIPE_IMAGE
        self.pipe_pass = False
        self.height_define()

    # FUNÇÃO PARA REFICINIR A POSIÇÃO DOS ANOS
    def height_define(self):
        self.heigth = (random.randrange(50, 450))
        self.position_top = self.heigth - self.pipe_top.get_height()
        self.position_bottom = self.heigth + self.DISTANCE

    def move_pipe(self):
        self.x -= self.SPEED

    def draw(self, screan):
        screan.blit(self.pipe_top, (self.x, self.position_top))
        screan.blit(self.pipe_bottom, (self.x, self.position_bottom))

    def colider(self, bird):
        # pegando a mascara de pixels dos elementos
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.pipe_top)
        bottom_mask = pygame.mask.from_surface(self.pipe_bottom)

        # pegando a distancia dos canos
        distance_top = (self.x - bird.x, self.position_top - round(bird.y))
        distance_bottom = (self.x - bird.x, self.position_bottom - round(bird.y))

        # verificando se teve colisão
        point_top = bird_mask.overlap(top_mask, distance_top)
        point_bottom = bird_mask.overlap(bottom_mask, distance_bottom)
