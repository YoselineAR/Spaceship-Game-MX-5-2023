import pygame
import math
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH

class ShipBigger(Enemy):
    WIDTH = 150
    HEIGHT = 190
    SPEED_X = 10
    SPEED_Y = 100
    def __init__(self):      
        self.image = ENEMY_2
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.direction = 1
        self.amplitude = 50 
        self.frequency = 0.02  
        self.starting_x = self.rect.x
        super().__init__(self.image)

    def move(self):
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:  
            self.direction *= -1

        self.rect.x += self.SPEED_X * self.direction
        self.rect.y = self.starting_x + self.amplitude * math.sin(self.frequency * self.rect.x)
    
          
