# use capitals for constants, these do not change in the entire game

import pygame


# game properties

SCREEN_HEIGHT = 680
SCREEN_WIDTH = 1020
GAME_CAPTION = 'flowers for JAMIE'
GAME_ICON = pygame.image.load('assets/images/game_icon.png')

FONT = 'assets/fonts/basis33.ttf'

# specific screen properties

MARGIN = 20
TEXT_GAP = 5
TEXT_BOX_FONT_SIZE = 30
TEXT_ROWS = 3

TEXT_BOX_X = SCREEN_WIDTH + MARGIN
TEXT_BOX_Y = SCREEN_HEIGHT - MARGIN - TEXT_BOX_FONT_SIZE - TEXT_GAP * TEXT_ROWS