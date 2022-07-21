import pygame


class Entity:
    def __init__(self, x_coord, y_coord, width, height):
        self.rect = pygame.Rect(x_coord, y_coord, width, height)

    def draw(self, screen):
        pass

    def update(self):
        pass

    # reset to init position
    def reset(self):
        pass

    # record previous position
    def record(self):
        pass