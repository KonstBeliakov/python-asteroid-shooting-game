from utils import *
from object import Object


class Coin(Object):
    def __init__(self, x, y, speedX, speedY):
        super().__init__(x=x, y=y, speedX=speedX, speedY=speedY)
        self.color = (150, 150, 0)

    def update(self, game):
        super().update(game)
        if self.outside_screen(game):
            self.active = False

        if polygons_intersect(self.get_polygon(), game.player.get_polygon()):
            self.collect(game)
            self.active = False

    def collect(self, game):
        game.coin_counter += 1

