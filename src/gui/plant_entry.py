# each plant book entry:

import pygame

from src.entities.entity_base_class import Entity
from src.gui.button_base_class import Button

hover_outline = pygame.image.load('assets/images/plant_book/highlighted_box.png').convert_alpha()


class PlantEntry(Button):
    def __init__(self, x_coord, y_coord, width, height):
        super().init_(x_coord, y_coord, width, height)
        self.state = 'seedling'
        self.hover_outline = hover_outline

    def set_entry(self, linked_entry):
        self.linked_entry = linked_entry