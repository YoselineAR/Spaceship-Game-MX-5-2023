import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET

class BulletSpaceship(Bullet):
    WIDTH = 9
    HEIGHT = 32
    SPEED = 20
    
    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)
    
    def update(self, enemy):
        self.rect.y -= self.SPEED
        super().update(enemy)
        if not enemy.is_alive:
            enemy.is_destruyed = True