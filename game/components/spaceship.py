import pygame
from game.utils.constants import SPACESHIP

class Spaceship:
    WIDTH = 40
    HEIGTH = 60

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self. rect = self.image.get_rect()

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
                