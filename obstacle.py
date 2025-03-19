import pygame
from random import randrange

from object import Object


class Obstacle(Object):
    def __init__(self, game, x=None, y=None):
        super().__init__(speedY=30)

        self.y = y if y is not None else -self.sizeY + 2
        self.x = x if x is not None else randrange(0, game.WIDTH - self.sizeX)

        self.hp = 100
        self.max_hp = 100

    def update(self, game):
        super().update(game)
        if self.outside_screen(game):
            self.active = False

    def draw(self, screen):
        super().draw(screen)

        f = min(1.0, max(0.0, self.hp / self.max_hp))
        full_color = (0, 50, 150)
        empty_color = (0, 150, 0)

        color = (int(f * full_color[0] + (1 - f) * empty_color[0]),
                 int(f * full_color[1] + (1 - f) * empty_color[1]),
                 int(f * full_color[2] + (1 - f) * empty_color[2]))

        pygame.draw.rect(screen, (50, 150, 250), (self.x, self.y - 10, self.sizeX * f, 7))
        pygame.draw.rect(screen,  color, (self.x + 1, self.y - 9, (self.sizeX - 2) * f, 5))
