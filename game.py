import time

import pygame

from obstacle import Obstacle
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
        self.obstacles = [Obstacle(self) for _ in range(5)]

        self.obsticle_spawn_delay = 2
        self.last_added_obsticles = time.perf_counter()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.over = True

        self.player.update(self)

        for bullet in self.bullets:
            bullet.update(self)

        for obsticle in self.obstacles:
            obsticle.update(self)

        # deleting not active objects
        for lst in self.bullets, self.obstacles:
            for i in range(len(lst)-1, -1, -1):
                if not lst[i].active:
                    del lst[i]

        self.add_new_obsticles()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)

        for bullet in self.bullets:
            bullet.draw(self.screen)

        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        pygame.display.flip()

    def add_new_obsticles(self):
        if time.perf_counter() - self.last_added_obsticles > self.obsticle_spawn_delay:
            self.last_added_obsticles = time.perf_counter()
            self.obstacles.append(Obstacle(self))
