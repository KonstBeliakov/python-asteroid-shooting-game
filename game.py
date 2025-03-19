import pygame

from player import Player
from bullet import Bullet


class Game:
    def __init__(self):
        self.over = False

        self.WIDTH, self.HEIGHT = 800, 600

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pygame game")

        self.player = Player()

        self.bullets: list[Bullet] = []

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.over = True

        self.player.update(self)

        for bullet in self.bullets:
            bullet.update(self)

        for i in range(len(self.bullets)-1, -1, -1):
            if not self.bullets[i].active:
                del self.bullets[i]

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)

        for bullet in self.bullets:
            bullet.draw(self.screen)

        pygame.display.flip()
