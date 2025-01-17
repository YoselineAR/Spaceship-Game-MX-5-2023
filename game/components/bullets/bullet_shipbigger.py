import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_SHIP_BIGGER


class BulletShipBigger(Bullet):
    WIDTH = 25
    HEIGHT = 50
    SPEED = 17
    
    def __init__(self, center):
        self.image = BULLET_SHIP_BIGGER
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)

    def update(self, player):
        self.rect.y += self.SPEED    
        super().update(player)