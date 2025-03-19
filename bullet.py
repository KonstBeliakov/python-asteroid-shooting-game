import pygame

from object import Object
from utils import polygons_intersect


class Bullet(Object):
    def __init__(self, x, y, speedX, speedY):
        super().__init__(x=x, y=y, sizeX=5, sizeY=15, speedX=speedX, speedY=speedY)
        self.damage = 10

    def update(self, game):
        super().update(game)
        
        if self.outside_screen(game):
            self.active = False

        for obstacle in game.obstacles:
            if polygons_intersect(obstacle.get_polygon(), self.get_polygon()):
                obstacle.hp -= self.damage
                self.active = False
