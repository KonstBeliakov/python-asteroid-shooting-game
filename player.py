import time

import pygame

from object import Object
from bullet import Bullet


class Player(Object):
    def __init__(self):
        super().__init__()
        self.speed = 300

        self.last_shot = time.perf_counter()

    def update(self, game):
        super().update(game)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed * self.time_since_updated
        if keys[pygame.K_s]:
            self.y += self.speed * self.time_since_updated
        if keys[pygame.K_a]:
            self.x -= self.speed * self.time_since_updated
        if keys[pygame.K_d]:
            self.x += self.speed * self.time_since_updated

        if keys[pygame.K_SPACE]:
            self.shoot(game)

    def shoot(self, game):
        if time.perf_counter() - self.last_shot > 0.5:
            game.bullets.append(Bullet(self.x, self.y, 0, -500))
            self.last_shot = time.perf_counter()
