import pygame
from shapely.geometry import Polygon
import numpy as np


def draw_progress_bar(screen, x, y, volume, max_volume, sizeX, full_color=(0, 50, 150), empty_color=(0, 150, 0)):
    f = min(1.0, max(0.0, volume / max_volume))
    full_color = full_color
    empty_color = empty_color

    color = (int(f * full_color[0] + (1 - f) * empty_color[0]),
             int(f * full_color[1] + (1 - f) * empty_color[1]),
             int(f * full_color[2] + (1 - f) * empty_color[2]))

    pygame.draw.rect(screen, (50, 150, 250), (x, y - 1, sizeX * f, 7))
    pygame.draw.rect(screen, color, (x + 1, y, (sizeX - 2) * f, 5))


def polygons_intersect(poly1, poly2):
    polygon1 = Polygon(poly1)
    polygon2 = Polygon(poly2)
    return polygon1.intersects(polygon2)


def darken_surface(surface, factor):
    arr = pygame.surfarray.pixels3d(surface).astype(np.float32)

    arr[0] *= factor
    arr[1] *= factor
    arr[2] *= factor

    arr = arr.clip(0, 255).astype(np.uint8)

    new_surface = pygame.Surface(surface.get_size())
    pygame.surfarray.blit_array(new_surface, arr)

    return new_surface
