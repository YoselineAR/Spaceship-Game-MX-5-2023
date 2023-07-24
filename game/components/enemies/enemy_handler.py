import random
from game.components.enemies.ship import Ship
from game.components.enemies.shipbigger import ShipBigger
from game.components.enemies.skyrocket import Skyrocket

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.delay = 0
        self.number_enemies_destroyed = 0

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if enemy.is_destruyed:
                self.number_enemies_destroyed += 1
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if self.delay == 0:
            self.enemies.append(Ship())
            self.delay = random.randint(20, 60)
        if len(self.enemies) <= 6:
            self.enemies.append(Skyrocket())     
        if len(self.enemies) <= 1: 
            self.enemies.append(ShipBigger()) 

        if self.delay > 0:
            self.delay -= 1   
      
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def reset(self):
        self.enemies = []
        self.number_enemies_destroyed = 0
        