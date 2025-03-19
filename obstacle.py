import pygame
from random import randrange

from object import Object


class Obstacle(Object):
    def __init__(self, game, x=None, y=None):
        super().__init__(speedY=200)

        self.y = y if y is not None else -self.sizeY+2
        self.x = x if x is not None else randrange(0, game.WIDTH - self.sizeX)

    def update(self, game):
        super().update(game)
        if self.outside_screen(game):
            self.active = False
