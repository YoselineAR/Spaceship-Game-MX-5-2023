import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import SKYROCKET

class Skyrocket(Enemy):
    WIDTH = 60
    HEIGTH = 80
    SPEED = 15

    def __init__(self):
        self.image = SKYROCKET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self. HEIGTH))      
        super().__init__(self.image)

    def move(self):
        self.rect.y += self.SPEED
        