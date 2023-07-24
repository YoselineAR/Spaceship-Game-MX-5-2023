import pygame
import math
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH, BULLET_SHIP_BIGGER_TYPE

class ShipBigger(Enemy):
    WIDTH = 150
    HEIGHT = 190
    SPEED_X = 10
    SPEED_Y = 100
    SHOOTING_TIME = 40

    def __init__(self):      
        self.image = ENEMY_2
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.direction = 1
        self.amplitude = 50 
        self.frequency = 0.02  
        self.starting_x = self.rect.x
        self.shooting_time = 0
        super().__init__(self.image)

    def update(self, bullet_handler):
        self.shoot(bullet_handler)  
        super().update(bullet_handler) 

    def move(self):
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:  
            self.direction *= -1

        self.rect.x += self.SPEED_X * self.direction
        self.rect.y = self.starting_x + self.amplitude * math.sin(self.frequency * self.rect.x)

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_SHIP_BIGGER_TYPE, self.rect.center)  

          
