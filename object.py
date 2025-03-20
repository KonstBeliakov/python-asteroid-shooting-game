import time
import pygame


class Object:
    def __init__(self, x=0, y=0, sizeX=30, sizeY=30, speedX=0, speedY=0):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.speedX = speedX
        self.speedY = speedY

        self.color = (70, 170, 250)

        self.last_updated = time.perf_counter()

        self.active = True

    def draw(self, game):
        pygame.draw.rect(game.screen, self.color, (self.x, self.y, self.sizeX, self.sizeY))

    def update(self, game):
        self.time_since_updated = time.perf_counter() - self.last_updated
        self.last_updated = time.perf_counter()

        self.x += self.speedX * self.time_since_updated
        self.y += self.speedY * self.time_since_updated

    def outside_screen(self, game):
        return self.x < -self.sizeX or self.y < -self.sizeY or self.x > game.WIDTH or self.y > game.HEIGHT

    def get_polygon(self):
        return [[self.x, self.y],
                [self.x, self.y + self.sizeY],
                [self.x + self.sizeX, self.y + self.sizeY],
                [self.x + self.sizeX, self.y]]