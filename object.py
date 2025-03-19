import time
import pygame


class Object:
    def __init__(self, x=0, y=0, sizeX=100, sizeY=100, speedX=0, speedY=0):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.speedX = speedX
        self.speedY = speedY

        self.color = (70, 170, 250)

        self.last_updated = time.perf_counter()

        self.active = True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.sizeX, self.sizeY))

    def update(self, game):
        self.time_since_updated = time.perf_counter() - self.last_updated
        self.last_updated = time.perf_counter()

        self.x += self.speedX * self.time_since_updated
        self.y += self.speedY * self.time_since_updated
