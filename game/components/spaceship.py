import pygame
import random
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPACESHIP_TYPE
from game.components.bullets.bullet_handler import BulletHandler

class Spaceship:
    WIDTH = 40
    HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500

    def __init__(self, bullet_handler):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.bullet_handler = bullet_handler

    def update(self, user_input, bullet_handler):
        if user_input[pygame.K_LEFT]:
            self.move_left()

        elif user_input[pygame.K_RIGHT]:
            self.move_right()

        elif user_input[pygame.K_UP]:
            self.move_up()

        elif user_input[pygame.K_DOWN]:
            self.move_down()

        if user_input[pygame.K_SPACE]:
            self.shoot(bullet_handler)
            

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullet_handler.draw(screen)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10

    def move_up(self):
        if self.rect.top > (SCREEN_HEIGHT // 2):
            self.rect.y -= 10
    
    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10

    def shoot(self, bullet_handler):
       bullet_handler.add_bullet(BULLET_SPACESHIP_TYPE, self.rect.center)      