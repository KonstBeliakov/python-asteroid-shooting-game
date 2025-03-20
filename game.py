import time

from obstacle import Obstacle
from player import Player
from bullet import Bullet
from shard import Shard
from utils import *


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

        self.shards: list[Shard] = []

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.over = True

        self.player.update(self)

        # updating
        for lst in self.bullets, self.obstacles, self.shards:
            for obj in lst:
                obj.update(self)

        # deleting not active objects
        for lst in self.bullets, self.obstacles, self.shards:
            for i in range(len(lst)-1, -1, -1):
                if not lst[i].active:
                    del lst[i]

        self.add_new_obsticles()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self)

        # drawing all objects in lists
        for lst in self.bullets, self.obstacles, self.shards:
            for obj in lst:
                obj.draw(self)

        pygame.display.flip()

    def add_new_obsticles(self):
        if time.perf_counter() - self.last_added_obsticles > self.obsticle_spawn_delay:
            self.last_added_obsticles = time.perf_counter()
            self.obstacles.append(Obstacle(self))
