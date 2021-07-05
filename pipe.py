import pygame
import os

PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))

class Pipe:
    DISTANCE = 200
    SPEED = 5
