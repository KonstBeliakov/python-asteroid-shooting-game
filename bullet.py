import pygame

from object import Object


class Bullet(Object):
    def __init__(self, x, y, speedX, speedY):
        super().__init__(x=x, y=y, sizeX=5, sizeY=15, speedX=speedX, speedY=speedY)

    def update(self, game):
        super().update(game)
        
        if self.x < -self.sizeX or self.y < -self.sizeY or self.x > game.WIDTH or self.y > game.HEIGHT:
            self.active = False
