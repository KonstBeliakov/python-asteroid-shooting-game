import pygame
from random import randrange, randint
from math import pi, sin, cos

from object import Object
from utils import *


class Obstacle(Object):
    def __init__(self, game, x=None, y=None):
        super().__init__(speedY=30)

        self.y = y if y is not None else -self.sizeY + 2
        self.x = x if x is not None else randrange(0, game.WIDTH - self.sizeX)

        self.hp = 100
        self.max_hp = 100

        self.vertex_number = 10
        self.d = [randint(1, 3) * 10 for _ in range(self.vertex_number)]

        self.not_active_color = (0, 50, 120)

    def update(self, game):
        super().update(game)
        if self.outside_screen(game) or self.hp <= 0:
            self.active = False

        if polygons_intersect(self.get_polygon(), game.player.get_polygon()):
            game.player.hp -= 100

    def draw(self, screen):
        #super().draw(screen)

        points = self.get_polygon()
        inner_points = self.get_inner_polygon()

        point_number = int(self.vertex_number * (self.hp / self.max_hp))

        points1 = points[:point_number]
        if len(points1) >= 2:
            pygame.draw.lines(screen, self.color, False, points1, 2)

        points2 = points[point_number-1:] + [points[0]]
        if len(points2) >= 2:
            pygame.draw.lines(screen, self.not_active_color, False, points2, 2)

        pygame.draw.polygon(screen, self.color, inner_points, 2)

    def get_polygon(self):
        points = []

        for i in range(self.vertex_number):
            angle = 2 * pi / self.vertex_number * i
            points.append([self.x + sin(angle) * (self.d[i] + 5),
                           self.y + cos(angle) * (self.d[i] + 5)])

        return points

    def get_inner_polygon(self):
        inner_points = []

        for i in range(self.vertex_number):
            angle = 2 * pi / self.vertex_number * i
            inner_points.append([self.x + sin(angle) * self.d[i],
                                 self.y + cos(angle) * self.d[i]])

        return inner_points
