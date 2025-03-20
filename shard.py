import time
import pygame

from object import Object


class Shard(Object):
    def __init__(self, pos1, pos2, speedX, speedY):
        super().__init__(speedX=speedX, speedY=speedY)
        self.x1, self.y1 = pos1
        self.x2, self.y2 = pos2

        self.time_spawned = time.perf_counter()
        self.lifetime = 1.5

    def draw(self, game):
        t = time.perf_counter() - self.time_spawned
        f = (1 - (t / self.lifetime))
        color = (f * self.color[0], f * self.color[1], f * self.color[2])

        start_pos = (self.x + self.x1, self.y + self.y1)
        end_pos = (self.x + self.x2, self.y + self.y2)

        pygame.draw.line(game.screen, color, start_pos, end_pos, 2)

    def update(self, game):
        super().update(game)
        if time.perf_counter() - self.time_spawned > self.lifetime:
            self.active = False
