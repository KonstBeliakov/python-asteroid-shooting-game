import pygame
from game import Game

pygame.init()

game = Game()
while not game.over:
    game.update()
    game.draw()
pygame.quit()
