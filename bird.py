import pygame
import os


# DEFINIÇÕES DA CLASSE PASSARO
class Bird:


    IMGS = [
        pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
        pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
        pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
    ]

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
        self.img = self.IMGS[0]

    # OS MOVIMENTOS NO PYGAME SÃO DEFINICOS
    # PARA CIMA É NEGATIVO NO Y E PARA BAIXO POSSITIVO
    # PARA A ESQUERTA É NEGATIVO NO X E PARA A DIREITA É POSSITIVO

    def jumpe(self):
        # função de pular
        self.speed = -10.5
        self.move_time = 0
        self.heigth = self.y

    def move(self):
        # calculo do deslocamento (S = SO + VOT + AT²/2)
        self.move_time += 1
        displacement = 1.5 * (self.move_time ** 2) + self.speed * self.move_time

        # delimitando o deslocamento do passaro
        if displacement > 16:
            displacement = 16
        elif displacement < 0:
            # essa parte faz o passaro subir mais quando aperta espaço
            displacement -= 2

        self.y += displacement

        # delimitando o angulo do passaro
        if displacement < 0 or self.y < (self.heigth + 50):
            # verifico se o deslocamento do passaro esta subindo e se a posição dele esta acima da posição anterior
            if self.angle < self.MAX_ROTATION:
                # se o angulo for menor que a rotação maxima atribui rotação maxima ao angulo
                self.angle = self.MAX_ROTATION
        else:
            # verifico se o angulo do passaro esta acima de -90 graus se estiver eu giro ele para o maximo
            if self.angle > -90:
                self.angle -= self.SPEED_ROTATION

    def draw(self, screen):

        # mudar as imagens do passaro para dar movimento (sempre verificando a contagem imagem)
        """index = [0,1,2,1,0]
        for i in index:
            self.img = self.IMGS[i]"""

        self.count_img += 1

        if self.count_img < self.TIME_ANIMATION:
            self.img = self.IMGS[0]
        elif self.count_img < self.TIME_ANIMATION * 2:
            self.img = self.IMGS[1]
        elif self.count_img < self.TIME_ANIMATION * 3:
            self.img = self.IMGS[2]
        elif self.count_img < self.TIME_ANIMATION * 4:
            self.img = self.IMGS[1]
        elif self.count_img > self.TIME_ANIMATION * 4 + 1:
            self.img = self.IMGS[0]
            self.count_img = 0

        # verificar se o passaro esta caindo, caso sim colocar imagem fixa
        if self.angle <= -80:
            self.img = self.IMGS[1]
            self.count_img = self.TIME_ANIMATION * 2

        # desenhar a imagem do passaro, (pegamos o angulo da imagem depois o centro dela para plotar na tela
        image_rotate = pygame.transform.rotate(self.img, self.angle)
        center_image = self.img.get_rect(topleft=(self.x, self.y)).center
        rectangle = image_rotate.get_rect(center=center_image)

        screen.blit(image_rotate, rectangle.topleft)

    # FUNÇÃO PARA PEGAR A MASCARA DO PASSARO (OS PIXELS DO OBJETO E NÃO DO RETANGULO DA IMAGEM)
    def get_mask(self):
        pygame.mask.from_surface(self.img)
